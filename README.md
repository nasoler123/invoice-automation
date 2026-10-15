# Invoice Automation

**Invoice processing automation still used monthly by two restaurants**

*A Chals AI case study — built by Ignacio Soler.*

<a id="the-project"></a>

I built an invoice-processing workflow that combines document extraction, financial validation and accounting preparation for Holded.

I built this project end to end on my own, using AI tools for all programming. My work covered product definition, technical decisions, implementation, integration and validation.

[See the workflow](#see-the-workflow) · [Explore the implementation](#explore-the-implementation) · [Run the component sample](#run-the-component-sample) · [Español](docs/LEEME.md)

## What I built

- OCR extraction and normalization of invoice information.
- Checks for tax amounts, totals and required fields.
- Supplier and account mapping, preparation for Holded registration, and bank-description matching to support reconciliation.

**Status:** Built in 2024–2025; active as of October 2026. **Two restaurants use it every month.**

Usage reported by the founder on 15 October 2026. Invoice volumes and time savings have not been quantified.

## See the workflow

**Invoice → extraction → validation → accounting preparation → reconciliation support.**

![Invoice Automation illustrated architecture](docs/overview.svg)

## Explore the implementation

The runnable component contains the original line-level tax and total checks. Selected source excerpts document the wider work: OCR, normalization, BigQuery, Holded integration and bank-description matching.

| Entry | What to look at |
|---|---|
| [invoice_controls.py](source/invoice_controls.py) | Original executable component |
| [demo.py](demo.py) | Synthetic fixtures and 5 checked behaviors |
| [Architecture](docs/architecture.md) | The wider system and the sample boundary |
| [Design decisions](docs/decisions.md) | Tradeoffs with source links |
| [Code tour](docs/code-tour.md) | 5 selected excerpts from the wider construction |
| [Provenance](provenance.json) | Original paths, commits, hashes and documented redactions |

**Stack across the project:** Python · Google Document AI · Azure Document Intelligence · BigQuery · Holded · embeddings.

This public case study includes selected original code and an isolated runnable sample with synthetic data. Production integrations and customer data remain private. Original paths, commits, hashes and redactions are recorded in [provenance.json](provenance.json).

<a id="run-the-sample"></a>

## Run the component sample

Run the original line-level tax and total checks locally with synthetic data. Requires **Python 3.10+**, with no package installation or account setup.

```sh
git clone https://github.com/nasoler123/invoice-automation.git
cd invoice-automation
python3 -I demo.py
python3 verify.py
```

Expected observations:

- A coherent line passes.
- Incorrect VAT, an incorrect total and missing fields fail with different reasons.
- Zero amounts are valid inputs.

The sample runs offline and rejects network connections and external subprocesses. `verify.py` checks local links, instruction parity, the source hash, credential patterns and the recorded results of the component checks. [Recorded local results](verification.json).

## More from Chals AI

These projects cover my work across business automation, financial software, AI agents and data infrastructure.

[Data Platform and MCP](https://github.com/nasoler123/data-platform-mcp) · [Financial Modeling SaaS](https://github.com/nasoler123/financial-modeling-saas) · [AI Agent Harness](https://github.com/nasoler123/ai-agent-harness)

[Ignacio Soler](https://github.com/nasoler123) · [LinkedIn](https://www.linkedin.com/in/ignacio-soler-esteban/)
