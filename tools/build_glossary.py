#!/usr/bin/env python3
"""Build GLOSSARY.md from the per-term files in terms/.

Standard library only.
  python3 tools/build_glossary.py           write GLOSSARY.md
  python3 tools/build_glossary.py --check   fail if GLOSSARY.md is out of date
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / "terms"
OUT = ROOT / "GLOSSARY.md"
STATUSES = {"current", "proposed", "superseded", "open"}


def read_value(raw, filename, key):
    """Front matter values are JSON: "text", ["a", "b"] or []. Empty means none."""
    if raw in ("", "null", "~"):
        return ""
    if raw[0] in '"[':
        try:
            return json.loads(raw)
        except ValueError:
            raise SystemExit(f"{filename}: '{key}' is not valid JSON-style text: {raw[:60]}")
    raise SystemExit(f"{filename}: '{key}' must be in double quotes or a [\"list\"]: {raw[:60]}")


def parse(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"{path.name}: missing front matter")
    head, _, _body = text[4:].partition("\n---\n")
    meta = {}
    for line in head.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = read_value(value.strip(), path.name, key.strip())
    meta["slug"] = path.stem
    for required in ("term", "status", "summary"):
        if not meta.get(required):
            raise SystemExit(f"{path.name}: '{required}' is empty")
    if meta["status"] not in STATUSES:
        raise SystemExit(f"{path.name}: unknown status '{meta['status']}'")
    return meta


def link(m):
    return f"[history](terms/{m['slug']}.md)"


def main():
    paths = [p for p in sorted(TERMS.glob("*.md")) if not p.stem.startswith("_")]
    terms = {m["slug"]: m for m in map(parse, paths)}
    for m in terms.values():
        for ref in (m.get("supersedes"), m.get("superseded_by")):
            if ref and ref not in terms:
                raise SystemExit(f"{m['slug']}: points to '{ref}', which has no file")

    entries = []  # (sort key, line)
    for m in terms.values():
        name = m["term"]
        exp = m.get("expansion", "")
        full = f" ({exp})" if exp and exp != name else ""
        if m["status"] == "superseded":
            new = terms[m["superseded_by"]]["term"] if m.get("superseded_by") else "nothing yet"
            line = f"- ~~{name}~~{full}: replaced by **{new}**. {link(m)}"
        else:
            tag = "" if m["status"] == "current" else f" _({m['status']})_"
            line = f"- **{name}**{full}{tag}: {m['summary']} {link(m)}"
        entries.append((name.lower(), line))
        for alias in m.get("aliases", []):
            target = name if m["status"] != "superseded" else terms[m["superseded_by"]]["term"]
            entries.append((alias.lower(), f"- **{alias}**: see **{target}**. {link(m)}"))

    entries.sort(key=lambda e: e[0])
    lines = [
        "# Pepa Glossary",
        "",
        "<!-- Built by tools/build_glossary.py from terms/. Do not edit by hand. -->",
        "",
        "One line per term. Struck-through names have been replaced; the replacement is named. "
        "Open a term's history link for the full story.",
    ]
    letter = None
    for key, line in entries:
        first = key[0].upper() if key[0].isalpha() else "#"
        if first != letter:
            letter = first
            lines += ["", f"## {letter}", ""]
        lines.append(line)
    lines.append("")
    result = "\n".join(lines)

    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != result:
            raise SystemExit("GLOSSARY.md is out of date. Run: python3 tools/build_glossary.py")
        print("GLOSSARY.md is up to date.")
    else:
        OUT.write_text(result, encoding="utf-8")
        print(f"Wrote {OUT.name}: {len(terms)} term files, {len(entries)} lines.")


if __name__ == "__main__":
    main()
