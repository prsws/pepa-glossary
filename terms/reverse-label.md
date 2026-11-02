---
term: "reverse label"
category: "pipeline and runtime"
status: "current"
aliases: ["reverse"]
summary: "A Home Assistant label declaring that an entity's actions can be undone; without it, the house scope asks a person before acting."
sources: ["Project working session, 1 Nov 2026"]
---

## Definition

A Home Assistant label on an entity. Present: the entity's actions can be undone, and the house scope acts at once. Absent: the entity is not reversible, which is Pepa's default, so a new or forgotten device fails closed. The action is held and Pepa asks a yes-or-no question; only a person's yes, from the same satellite or conversation, within a set wait (1 to 60 seconds, default 10), runs exactly the held action. Code decides what counts as a yes, from fixed Spanish and English word lists, not the model. A request through the integration's own service, where nobody can answer, is refused.

The house catalog shows it as a `reverse` column (true or false), which only informs the model.

A first, two-valued step toward the four reversibility tiers proposed earlier. Built in `pepa-sensory-arm-house`; not deployed.

## History

- 2026-11-01: Decided by José: true means reversible; false, missing or null means not reversible. The column and the confirmation were built the same day.
