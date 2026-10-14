# Design decisions

[Project](../README.md) · [Architecture](architecture.md) · [Code tour](code-tour.md)

## Validate before acting

A legible extraction can still contain inconsistent amounts. Missing values, total arithmetic and VAT arithmetic produce distinct error reasons. [Inspect the source](../evidence/E03.md).

## Treat matching as evidence

Historical supplier descriptions inform cosine-similarity matching. This is a matching component, not a retrieval-augmented generation system. [Inspect the source](../evidence/E05.md).

## Keep accounting context

Line identity, accounting accounts and tax mappings remain explicit when preparing the Holded operation. [Inspect the source](../evidence/E04.md).

