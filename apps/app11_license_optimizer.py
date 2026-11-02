"""Software License Optimizer

Task: Reduce unused SaaS licenses across the company.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'license_optimizer'
TITLE = 'Software License Optimizer'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Reduce unused SaaS licenses across the company.'

# (key, role, instruction)
AGENTS = [
    ('usage_collector', 'Usage Collector', 'Gather usage.'),
    ('waste_finder', 'Waste Finder', 'Find unused seats.'),
    ('contract_reader', 'Contract Reader', 'Check renewal terms.'),
    ('savings_calculator', 'Savings Calculator', 'Estimate savings.'),
    ('action_planner', 'Action Planner', 'Propose actions.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
