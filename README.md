# Pepa Glossary

Every Pepa word, name and abbreviation in one place, with its history.

Pepa is a self-hosted, octopus-inspired cognitive infrastructure blueprint to help the elderly preserve memory, organize knowledge and maintain agency. It is documented at [ai4aging.org](https://ai4aging.org).

> **Draft, under correction.** Do not cite this as settled vocabulary yet. See [OPEN-ITEMS.md](OPEN-ITEMS.md).

- **Looking something up?** Open [GLOSSARY.md](GLOSSARY.md). One line per term, alphabetical. Abbreviations and alternative names are listed too and point to the full name.
- **Want the story of a term?** Each line links to its file in [terms/](terms/): the full definition and a dated history of how it changed.
- **Something unsettled?** See [OPEN-ITEMS.md](OPEN-ITEMS.md).

## What is in scope

Pepa-specific vocabulary: coined terms, project abbreviations, named principles, named failure modes, node names, and external references as Pepa uses them. Generic AI terms are left out unless Pepa gives them a different meaning.

## How the files fit together

The files in `terms/` are the source. `GLOSSARY.md` is built from them by `tools/build_glossary.py`, so the two can never disagree. Do not edit `GLOSSARY.md` by hand.

## Rules

1. **Spell it out.** A term's `expansion` gives the full words behind an abbreviation.
2. **Never delete a term.** When a name is replaced, mark the old one `superseded` and point it at the new one with `superseded_by`. The imperfect evolution is the point.
3. **History is append-only.** Corrections go in as new dated lines under `## History`. Earlier lines are not rewritten.
4. **One sentence for the summary.** It becomes the line in `GLOSSARY.md`. Longer explanation goes in the body.
5. **Say where it came from.** List sources in the front matter. If a date is not known, write "date to confirm" instead of guessing.

## Adding or changing a term

1. Copy `terms/_template.md` to `terms/<slug>.md` and fill it in. The slug is the term in lowercase with dashes.
2. Run `python3 tools/build_glossary.py`.
3. Commit the term file and the rebuilt `GLOSSARY.md` together.

`python3 tools/build_glossary.py --check` fails if `GLOSSARY.md` is out of date, or if a term points to a replacement that has no file.

Front matter values are written in double quotes, and lists as `["a", "b"]`, so the files stay valid YAML and display correctly on GitHub.

## Status values

| Status | Meaning |
| --- | --- |
| `current` | In use today. |
| `proposed` | Suggested, not decided. |
| `superseded` | Replaced by another term; kept for history. |
| `open` | Used in documents but never properly defined; needs a source. |

## Where the first entries came from

The first 164 term files were migrated on 31 Oct 2026 from earlier private drafts of this glossary. Version 0.1 (4 Sep 2026) was compiled from the project's private working documents. Version 0.2 (31 Oct 2026) added what the September terms became and the terms introduced since, from ai4aging.org and project chats. Each term's history says which version recorded it.

## License

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0). See [LICENSE](LICENSE).
