# Source: https://docs.ox.security/automate-with-ox-workflows/ox-automations/workflows-troubleshooting.md

# Workflows Troubleshooting

* If a workflow doesn’t appear to work, first check whether the trigger, condition, or action is scoped too narrowly.
* Review your organization selection. If you’re in a demo org or test space, workflows may not behave as expected.
* Developers often miss that some options (like PR type) depend on full repo indexing. Make sure you've selected all relevant repositories.
* When defining conditions like "maximum number of admins," remember that this is just a default. You can override the value if your security policy is stricter.
* Use Slack and email actions in tandem when urgency is high. If you're on vacation, a Slack alert can still reach you.
* Hover over any term or field in the workflow builder for a tooltip explanation. These hints clarify field usage and help identify less obvious logic.
* If you expect certain applications or issues to trigger a workflow and nothing happens, verify the inputs and filters one by one. Misconfigurations often hide in small toggles like repo selection or visibility filters.

## Edge Case Scenarios

* **Naming Conflicts**: If your production app is called "test-app" and filtered out due to its name, adjust the inclusion/exclusion logic to reflect reality.
* **False Priority Downgrades**: If a policy marks something as low severity but you know it’s exposed to the internet, you can increase its business priority to elevate its urgency in workflows.
* **Timeout Behavior**: Customers requested visual feedback during long workflow executions. If you’re unsure whether a workflow completed, recheck your application scope or toggle options to refresh visibility.

## What to Do When a Workflow Doesn’t Work

* Check if the repository or application is actually selected and visible.
* Confirm that the issue matches all trigger and condition requirements.
* Review whether pipeline-specific actions (like "Block pipeline") are used in a regular scan workflow, these won't trigger outside pipeline context.
* Verify that your organization context is correct. If you're in a demo org, workflows may not behave as expected.
