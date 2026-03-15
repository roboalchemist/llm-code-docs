# Source: https://docs.firehydrant.com/docs/runbook-step-assign-a-role.md

# Assign a Role

<Image alt="Assign a Role Runbook Step" align="center" width="650px" src="https://files.readme.io/cc7f7e866cce5f0b04084804d078951c5f66a81fbaf2c12a4b09d380d7c31b34-CleanShot_2025-06-20_at_16.14.022x.jpg">
  Assign a Role Runbook Step
</Image>

Assigning roles during your incidents allows you to give responders specific responsibilities to ensure consistency. This Runbook step allows automatically assigning these roles as part of automation.

## Prerequisites

* If you'd like to assign people from on-call schedules, you will need to have configured an [alerting provider](/docs/integrations-overview#alerting-integrations)
* Otherwise, the user(s) you'd like to assign need to have FireHydrant accounts

> 📘 Note:
>
> If Slack is integrated with your FireHydrant instance, assigning an incident role to a user also automatically pulls that user into the incident Slack channel if they have a FireHydrant account.

## Adding the step

To add the step, edit a Runbook and then look for "Assign a Role" step. The step has two dropdown fields.

* **Role:** This is a dynamically populated dropdown with the roles that you have customized for you account. You can learn more about roles, the default roles provided, and how to customize them [here](https://docs.firehydrant.com/docs/incident-roles).
* **User:** The user dropdown contains multiple sections:
  1. **Incident Opener:** Whoever opened or created the incident, if they have a FireHydrant account
  2. **Active Escalation Policy or On-Call User (Signals):** The current active user for a specific [On-Call Schedule](https://docs.firehydrant.com/docs/signals-on-call-schedules) or [Escalation Policy](https://docs.firehydrant.com/docs/signals-escalation-policies) configured in FireHydrant.
  3. **Schedules (3rd-party):** The current on-call user from an escalation policy or on-call schedule from a 3rd-party provider. To see these, you must have such [alerting provider](/docs/integrations-overview#alerting-integrations) configured.
  4. **Users:** FireHydrant users within your organization

To persist changes, click "Add step" and "Save Runbook."