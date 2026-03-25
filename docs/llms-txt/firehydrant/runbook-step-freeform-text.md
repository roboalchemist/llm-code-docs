# Source: https://docs.firehydrant.com/docs/runbook-step-freeform-text.md

# Freeform Text

Freeform Text steps don't directly execute any actions but allow you to provide information and resources that responders can access during an incident.

## Configuration

To add a freeform text Runbook step:

1. Go to Runbooks > Create/Edit a Runbook > "+ Add step" 
2. Search for "freeform text" and select the Freeform Text step.

![](https://files.readme.io/1df7de8-image.png)

3. Fill in the information you'd like to display if a user opens this step.
4. (Optional) After providing the step details, click the Conditions & Scheduling tab to add rules and define repeat scheduling for the step. If you add a repeat, this means a new copy of this step will be appended to the end of the Runbook at the interval you specify.

When the Runbook with this step executes, you will be able to find this step in both the Command Center and from Slack.

<Image alt="Via `/fh runbooks` in Slack" align="center" width="400px" src="https://files.readme.io/06d76e0-image.png">
  Via `/fh runbooks` in Slack
</Image>

<Image alt="From the Runbooks tab in Command Center" align="center" width="400px" src="https://files.readme.io/ed256c9-image.png">
  From the Runbooks tab in Command Center
</Image>