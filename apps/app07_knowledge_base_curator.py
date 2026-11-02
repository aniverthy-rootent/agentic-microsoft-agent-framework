"""Knowledge Base Curator

Task: Clean up 200 stale internal wiki pages.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'knowledge_base_curator'
TITLE = 'Knowledge Base Curator'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Clean up 200 stale internal wiki pages.'

# (key, role, instruction)
AGENTS = [
    ('staleness_detector', 'Staleness Detector', 'Find stale content.'),
    ('duplicate_merger', 'Duplicate Merger', 'Merge duplicates.'),
    ('rewriter', 'Rewriter', 'Rewrite unclear pages.'),
    ('taxonomy_designer', 'Taxonomy Designer', 'Restructure tags.'),
    ('publisher', 'Publisher', 'Prepare the change list.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
