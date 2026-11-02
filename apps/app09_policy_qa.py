"""Corporate Policy Q&A

Task: Can I expense a 120 EUR team dinner during travel?
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'policy_qa'
TITLE = 'Corporate Policy Q&A'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Can I expense a 120 EUR team dinner during travel?'

# (key, role, instruction)
AGENTS = [
    ('question_router', 'Question Router', 'Find the policy area.'),
    ('policy_retriever', 'Policy Retriever', 'Recall relevant policy.'),
    ('answer_drafter', 'Answer Drafter', 'Answer with citations.'),
    ('escalation_judge', 'Escalation Judge', 'Decide if HR must review.'),
    ('compliance_checker', 'Compliance Checker', 'Check the answer against legal constraints.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
