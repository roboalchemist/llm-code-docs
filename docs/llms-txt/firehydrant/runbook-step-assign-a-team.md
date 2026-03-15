# Source: https://docs.firehydrant.com/docs/runbook-step-assign-a-team.md

# Assign a Team

Assigning the right teams in an incident can be critical to getting the right eyes on the issue. See how FireHydrant can automate this via Runbooks.

<Image alt="Assign a Team Runbook step" align="center" src="https://files.readme.io/cd617e3-image.png">
  Assign a Team Runbook step
</Image>

In addition to [assigning roles](https://docs.firehydrant.com/docs/runbook-step-assign-a-role), you can also assign entire teams of people to an incident via Runbook automation.

## Prerequisites

This requires having [at least one team configured](https://docs.firehydrant.com/docs/team-configuration).

## Adding the step

To add the step, edit a Runbook and look up the "assign a team" step.

This step has a single field to select which team should be assigned to this incident. When executed, this will pull in all the designated individuals on the team and assign them to any default roles if configured.

This will also automatically pull all these people into the incident Slack channel.