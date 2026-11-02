"""Employee Onboarding

Task: Onboard a new data scientist starting Monday.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'employee_onboarding'
TITLE = 'Employee Onboarding'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Onboard a new data scientist starting Monday.'

# (key, role, instruction)
AGENTS = [
    ('account_provisioner', 'Account Provisioner', 'Plan accounts.'),
    ('hardware_coordinator', 'Hardware Coordinator', 'Order equipment.'),
    ('buddy_matcher', 'Buddy Matcher', 'Pick a mentor.'),
    ('training_scheduler', 'Training Scheduler', 'Schedule training.'),
    ('compliance_trainer', 'Compliance Trainer', 'Assign mandatory courses.'),
    ('day_one_concierge', 'Day-One Concierge', 'Write the day-one plan.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
