# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-follow-up-jira-cloud-issue.md

# Create a Follow-Up Jira Cloud Issue

This Runbook step will automatically create a Follow-Up in the incident along with a corresponding Jira Cloud issue and link the two items together. [Learn more about managing Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups).

This is not to be confused with [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue), which creates an **incident ticket** representing the FireHydrant incident in Jira.

> 📘 Note:
>
> This is currently supported for Jira Cloud only.

## Prerequisites

* Ensure you have configured [Jira Cloud](https://docs.firehydrant.com/docs/jira-cloud-integration) integration and configured a project to create the issue in

## Configuration

<Image alt="Create a Follow-up Jira Cloud issue step" align="center" width="650px" src="https://files.readme.io/ad209ee-CleanShot_2024-08-09_at_15.37.53.png">
  Create a Follow-up Jira Cloud issue step
</Image>

This Runbook step supports all of the same fields as [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue):

* **Name** - A name for the step, which will be seen when browsing the Runbook and its steps on incidents
* **Project** - Which Jira project to create the ticket in. You'll need to have configured the project in FireHydrant. To learn more, see [Jira Cloud](https://docs.firehydrant.com/docs/jira-cloud-integration) docs.
* **Ticket Summary** - The name of the follow-up issue\*
* **Ticket Description** - A longer description and more detail for the issue\*
* **Assign Ticket to a Role** - Assign the ticket to the user assigned to a specific FireHydrant incident role. This step requires that users have linked their Jira and FireHydrant accounts

*\*These steps support[Template Variables](https://docs.firehydrant.com/docs/template-variables)*