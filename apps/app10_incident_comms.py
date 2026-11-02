"""Major Incident Communications

Task: Email service outage affecting 5,000 users.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'incident_comms'
TITLE = 'Major Incident Communications'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Email service outage affecting 5,000 users.'

# (key, role, instruction)
AGENTS = [
    ('impact_assessor', 'Impact Assessor', 'Scope impact.'),
    ('message_drafter', 'Message Drafter', 'Write the internal notice.'),
    ('executive_briefer', 'Executive Briefer', 'Brief executives.'),
    ('customer_notifier', 'Customer Notifier', 'Draft customer notice.'),
    ('timeline_keeper', 'Timeline Keeper', 'Keep the timeline.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
