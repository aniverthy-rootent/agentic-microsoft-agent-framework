"""Payroll Audit

Task: Check the monthly payroll run for errors.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'payroll_audit'
TITLE = 'Payroll Audit'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Check the monthly payroll run for errors.'

# (key, role, instruction)
AGENTS = [
    ('data_gatherer', 'Data Gatherer', 'Collect inputs.'),
    ('calculation_verifier', 'Calculation Verifier', 'Recompute pay.'),
    ('tax_checker', 'Tax Checker', 'Verify deductions.'),
    ('variance_analyst', 'Variance Analyst', 'Compare with last month.'),
    ('exception_reporter', 'Exception Reporter', 'List exceptions.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
