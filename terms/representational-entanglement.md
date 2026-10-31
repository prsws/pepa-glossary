---
term: "Representational entanglement"
category: "failure mode"
status: "current"
aliases: ["the functor problem"]
summary: "In a transformer, a token's meaning, context, and apparent purpose are blended into one vector; there is no architectural seam separating content from intent, so the model must infer intent."
sources: []
---

## Definition

In a transformer, a token's meaning, context, and apparent purpose are blended into one vector; there is no architectural seam separating content from intent, so the model must *infer* intent. The architectural answer is to carry intent **out-of-band**.

## History

- 2026-09-04: Recorded in Glossary v0.1, section 3.
