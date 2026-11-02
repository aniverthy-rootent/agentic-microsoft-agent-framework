"""IT Helpdesk

Task: User cannot connect to the corporate VPN after a password change.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'it_helpdesk'
TITLE = 'IT Helpdesk'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'User cannot connect to the corporate VPN after a password change.'

# (key, role, instruction)
AGENTS = [
    ('intake_agent', 'Intake Agent', 'Capture the issue.'),
    ('diagnostics_agent', 'Diagnostics Agent', 'Run the checks.'),
    ('knowledge_agent', 'Knowledge Agent', 'Find the runbook.'),
    ('fix_agent', 'Fix Agent', 'Provide steps.'),
    ('ticket_closer', 'Ticket Closer', 'Summarize and close.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
