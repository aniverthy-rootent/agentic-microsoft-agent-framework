"""Facilities & Room Booking

Task: Schedule a 12-person offsite for 2 days.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'meeting_room_booking'
TITLE = 'Facilities & Room Booking'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Schedule a 12-person offsite for 2 days.'

# (key, role, instruction)
AGENTS = [
    ('request_parser', 'Request Parser', 'Parse needs.'),
    ('room_finder', 'Room Finder', 'Find rooms.'),
    ('catering_planner', 'Catering Planner', 'Plan catering.'),
    ('calendar_coordinator', 'Calendar Coordinator', 'Block calendars.'),
    ('confirmation_writer', 'Confirmation Writer', 'Send confirmations.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
