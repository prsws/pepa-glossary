---
term: "volatile / verify flags"
category: "pipeline and runtime"
status: "current"
aliases: []
summary: "Entity-metadata columns."
sources: []
---

## Definition

Entity-metadata columns. As of the 2026-08-26 code pin, `verify` **has no consumers** — the preprocessor publishes it and the prompt renders it, but no code path reads it, so nothing can enforce it.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 5.
- 2026-11-01: In the rebuilt house-scope code (`pepa-sensory-arm-house`, not deployed), `verify` now has a consumer: after a command, the entity must reach the state the command implies within 60 seconds, or the failure is spoken on the satellite that asked and a notification is raised. A ninth catalog column, `reverse`, was added; see [reverse label](reverse-label.md).
