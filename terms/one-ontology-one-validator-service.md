---
term: "One ontology, one validator service"
category: "principle"
status: "current"
aliases: []
summary: "Arms hold a link to one central validator that the Head also calls; version-stamped results; fail closed if unreachable."
supersedes: "shared-spec-local-enforcement"
sources: []
---

## Definition

Contract discipline for the Head↔Arm seam. Arms hold a *link* to a single central validator; the Head calls the same service; results are version-stamped; fail-closed when the validator is unreachable. Rationale: centralizing *enforcement* in the Head would leak domain knowledge upward and break the Octopus model — centralizing it in a dedicated deterministic validator does not.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 2, as the replacement for "Shared spec, local enforcement".
