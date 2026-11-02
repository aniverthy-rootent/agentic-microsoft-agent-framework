"""Vendor Risk Management

Task: Assess a new payment processor vendor.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'vendor_risk'
TITLE = 'Vendor Risk Management'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Assess a new payment processor vendor.'

# (key, role, instruction)
AGENTS = [
    ('questionnaire_agent', 'Questionnaire Agent', 'Build the questionnaire.'),
    ('security_reviewer', 'Security Reviewer', 'Assess security.'),
    ('financial_reviewer', 'Financial Reviewer', 'Assess stability.'),
    ('compliance_reviewer', 'Compliance Reviewer', 'Assess certifications.'),
    ('risk_rater', 'Risk Rater', 'Rate overall risk.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
