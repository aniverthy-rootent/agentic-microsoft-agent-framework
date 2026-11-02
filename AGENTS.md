# Agent roster: agentic-microsoft-agent-framework

_Enterprise IT, HR & finance operations (Microsoft Agent Framework)_


## 1. IT Helpdesk (`apps/app01_it_helpdesk.py`)

Task: User cannot connect to the corporate VPN after a password change.

- **Intake Agent** (`intake_agent`): Capture the issue.
- **Diagnostics Agent** (`diagnostics_agent`): Run the checks.
- **Knowledge Agent** (`knowledge_agent`): Find the runbook.
- **Fix Agent** (`fix_agent`): Provide steps.
- **Ticket Closer** (`ticket_closer`): Summarize and close.

## 2. Employee Onboarding (`apps/app02_employee_onboarding.py`)

Task: Onboard a new data scientist starting Monday.

- **Account Provisioner** (`account_provisioner`): Plan accounts.
- **Hardware Coordinator** (`hardware_coordinator`): Order equipment.
- **Buddy Matcher** (`buddy_matcher`): Pick a mentor.
- **Training Scheduler** (`training_scheduler`): Schedule training.
- **Compliance Trainer** (`compliance_trainer`): Assign mandatory courses.
- **Day-One Concierge** (`day_one_concierge`): Write the day-one plan.

## 3. Access Review (`apps/app03_access_review.py`)

Task: Quarterly review of admin permissions in Azure.

- **Entitlement Collector** (`entitlement_collector`): List entitlements.
- **Role Analyzer** (`role_analyzer`): Compare to job roles.
- **Risk Scorer** (`risk_scorer`): Score risky access.
- **Manager Liaison** (`manager_liaison`): Draft questions to managers.
- **Report Builder** (`report_builder`): Produce attestation report.

## 4. Payroll Audit (`apps/app04_payroll_audit.py`)

Task: Check the monthly payroll run for errors.

- **Data Gatherer** (`data_gatherer`): Collect inputs.
- **Calculation Verifier** (`calculation_verifier`): Recompute pay.
- **Tax Checker** (`tax_checker`): Verify deductions.
- **Variance Analyst** (`variance_analyst`): Compare with last month.
- **Exception Reporter** (`exception_reporter`): List exceptions.

## 5. Budget Forecasting (`apps/app05_budget_forecast.py`)

Task: Forecast next year's department budgets.

- **Actuals Analyst** (`actuals_analyst`): Summarize actuals.
- **Driver Modeler** (`driver_modeler`): Model drivers.
- **Scenario Builder** (`scenario_builder`): Build scenarios.
- **Variance Explainer** (`variance_explainer`): Explain deltas.
- **Narrative Writer** (`narrative_writer`): Write the narrative.

## 6. Vendor Risk Management (`apps/app06_vendor_risk.py`)

Task: Assess a new payment processor vendor.

- **Questionnaire Agent** (`questionnaire_agent`): Build the questionnaire.
- **Security Reviewer** (`security_reviewer`): Assess security.
- **Financial Reviewer** (`financial_reviewer`): Assess stability.
- **Compliance Reviewer** (`compliance_reviewer`): Assess certifications.
- **Risk Rater** (`risk_rater`): Rate overall risk.

## 7. Knowledge Base Curator (`apps/app07_knowledge_base_curator.py`)

Task: Clean up 200 stale internal wiki pages.

- **Staleness Detector** (`staleness_detector`): Find stale content.
- **Duplicate Merger** (`duplicate_merger`): Merge duplicates.
- **Rewriter** (`rewriter`): Rewrite unclear pages.
- **Taxonomy Designer** (`taxonomy_designer`): Restructure tags.
- **Publisher** (`publisher`): Prepare the change list.

## 8. Facilities & Room Booking (`apps/app08_meeting_room_booking.py`)

Task: Schedule a 12-person offsite for 2 days.

- **Request Parser** (`request_parser`): Parse needs.
- **Room Finder** (`room_finder`): Find rooms.
- **Catering Planner** (`catering_planner`): Plan catering.
- **Calendar Coordinator** (`calendar_coordinator`): Block calendars.
- **Confirmation Writer** (`confirmation_writer`): Send confirmations.

## 9. Corporate Policy Q&A (`apps/app09_policy_qa.py`)

Task: Can I expense a 120 EUR team dinner during travel?

- **Question Router** (`question_router`): Find the policy area.
- **Policy Retriever** (`policy_retriever`): Recall relevant policy.
- **Answer Drafter** (`answer_drafter`): Answer with citations.
- **Escalation Judge** (`escalation_judge`): Decide if HR must review.
- **Compliance Checker** (`compliance_checker`): Check the answer against legal constraints.

## 10. Major Incident Communications (`apps/app10_incident_comms.py`)

Task: Email service outage affecting 5,000 users.

- **Impact Assessor** (`impact_assessor`): Scope impact.
- **Message Drafter** (`message_drafter`): Write the internal notice.
- **Executive Briefer** (`executive_briefer`): Brief executives.
- **Customer Notifier** (`customer_notifier`): Draft customer notice.
- **Timeline Keeper** (`timeline_keeper`): Keep the timeline.

## 11. Software License Optimizer (`apps/app11_license_optimizer.py`)

Task: Reduce unused SaaS licenses across the company.

- **Usage Collector** (`usage_collector`): Gather usage.
- **Waste Finder** (`waste_finder`): Find unused seats.
- **Contract Reader** (`contract_reader`): Check renewal terms.
- **Savings Calculator** (`savings_calculator`): Estimate savings.
- **Action Planner** (`action_planner`): Propose actions.
