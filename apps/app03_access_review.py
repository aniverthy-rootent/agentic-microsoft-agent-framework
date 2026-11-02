"""Access Review

Task: Quarterly review of admin permissions in Azure.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'access_review'
TITLE = 'Access Review'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Quarterly review of admin permissions in Azure.'

# (key, role, instruction)
AGENTS = [
    ('entitlement_collector', 'Entitlement Collector', 'List entitlements.'),
    ('role_analyzer', 'Role Analyzer', 'Compare to job roles.'),
    ('risk_scorer', 'Risk Scorer', 'Score risky access.'),
    ('manager_liaison', 'Manager Liaison', 'Draft questions to managers.'),
    ('report_builder', 'Report Builder', 'Produce attestation report.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
