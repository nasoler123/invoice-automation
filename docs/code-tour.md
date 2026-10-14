# Code tour

[Project](../README.md) · [Architecture](architecture.md) · [Design decisions](decisions.md)

## Start with executable code

1. Read [invoice_controls.py](../source/invoice_controls.py).
2. Inspect the synthetic inputs and assertions in [demo.py](../demo.py).
3. Compare [verification.json](../verification.json) with a fresh local run.

## Selected source from the wider system

| Component | Inspect | Form |
|---|---|---|
| Google OCR entry point | [Open excerpt](../evidence/E01.md) | Código |
| Azure OCR retry policy | [Open excerpt](../evidence/E02.md) | Código |
| Line amount and VAT validation | [Open excerpt](../evidence/E03.md) | Código |
| Holded accounting preparation | [Open excerpt](../evidence/E04.md) | Código |
| Bank-description similarity | [Open excerpt](../evidence/E05.md) | Código |

These excerpts retain original commit references. Incomplete classes, functions or integrations are presented as excerpts; the bounded executable module is separate. Redactions protect identifiers and are recorded in [provenance.json](../provenance.json).
