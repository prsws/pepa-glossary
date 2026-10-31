---
term: "68 °F incident"
category: "failure mode"
status: "current"
aliases: []
summary: "A temporary \"set the A/C to 81\" request was recorded as a standing 68 °F preference, then promoted into trusted retrieval as if it were ground truth."
sources: []
---

## Definition

The project's poster-child failure. A *temporary* "set the A/C to 81" request was executed correctly but mis-recorded as a standing temperature *preference* at the wrong value of 68 °F (the most common value), then self-reinforced until it promoted into authoritative top-k retrieval as if it were ground truth. Motivating case for provenance-at-write, corroboration-gated promotion, and the anti-climb gate.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 3.
