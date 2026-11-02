# agentic-microsoft-agent-framework

**11 multi-agent applications built with Microsoft Agent Framework.**  
Theme: _Enterprise IT, HR & finance operations (Microsoft Agent Framework)_

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) is Microsoft's unified successor to Semantic Kernel and AutoGen for building agents and **graph workflows**. These apps are enterprise IT, HR and finance operations.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_it_helpdesk   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

Each role is an `agent_framework.Agent`. `WorkflowBuilder` connects them: `add_chain` for sequential apps; `add_fan_out_edges` -> `Join` executor (`add_fan_in_edges`) -> merger agent for fan-out apps. An offline `BaseChatClient` replaces the model.

## Using a real model

Swap `OfflineChatClient` for a real client from the framework, e.g. `OpenAIChatClient`, `AzureOpenAIChatClient` or a Foundry client (install `agent-framework` for the full set of providers) and configure the matching endpoint/key.

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | IT Helpdesk | 5 | Intake Agent, Diagnostics Agent, Knowledge Agent, Fix Agent, Ticket Closer |
| 2 | Employee Onboarding | 6 | Account Provisioner, Hardware Coordinator, Buddy Matcher, Training Scheduler, Compliance Trainer, Day-One Concierge |
| 3 | Access Review | 5 | Entitlement Collector, Role Analyzer, Risk Scorer, Manager Liaison, Report Builder |
| 4 | Payroll Audit | 5 | Data Gatherer, Calculation Verifier, Tax Checker, Variance Analyst, Exception Reporter |
| 5 | Budget Forecasting | 5 | Actuals Analyst, Driver Modeler, Scenario Builder, Variance Explainer, Narrative Writer |
| 6 | Vendor Risk Management | 5 | Questionnaire Agent, Security Reviewer, Financial Reviewer, Compliance Reviewer, Risk Rater |
| 7 | Knowledge Base Curator | 5 | Staleness Detector, Duplicate Merger, Rewriter, Taxonomy Designer, Publisher |
| 8 | Facilities & Room Booking | 5 | Request Parser, Room Finder, Catering Planner, Calendar Coordinator, Confirmation Writer |
| 9 | Corporate Policy Q&A | 5 | Question Router, Policy Retriever, Answer Drafter, Escalation Judge, Compliance Checker |
| 10 | Major Incident Communications | 5 | Impact Assessor, Message Drafter, Executive Briefer, Customer Notifier, Timeline Keeper |
| 11 | Software License Optimizer | 5 | Usage Collector, Waste Finder, Contract Reader, Savings Calculator, Action Planner |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
