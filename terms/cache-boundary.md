---
term: "Cache boundary"
category: "pipeline and runtime"
status: "current"
aliases: ["cacheable prefix"]
summary: "The prompt is split so everything above the boundary (HEAD instructions + custom additions + DEVICE CATALOG CSV) is byte-identical turn to turn and the inference server reuses the cached…"
sources: []
---

## Definition

The prompt is split so everything above the boundary (HEAD instructions + custom additions + DEVICE CATALOG CSV) is byte-identical turn to turn and the inference server reuses the cached prefix; LIVE STATES onward is rebuilt per utterance.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 5.
