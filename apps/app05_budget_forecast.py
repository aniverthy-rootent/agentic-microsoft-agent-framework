"""Budget Forecasting

Task: Forecast next year's department budgets.
Framework: Microsoft Agent Framework
"""
from runtime import run_app

SLUG = 'budget_forecast'
TITLE = 'Budget Forecasting'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = "Forecast next year's department budgets."

# (key, role, instruction)
AGENTS = [
    ('actuals_analyst', 'Actuals Analyst', 'Summarize actuals.'),
    ('driver_modeler', 'Driver Modeler', 'Model drivers.'),
    ('scenario_builder', 'Scenario Builder', 'Build scenarios.'),
    ('variance_explainer', 'Variance Explainer', 'Explain deltas.'),
    ('narrative_writer', 'Narrative Writer', 'Write the narrative.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
