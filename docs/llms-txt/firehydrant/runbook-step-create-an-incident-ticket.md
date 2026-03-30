# Source: https://docs.firehydrant.com/docs/runbook-step-create-an-incident-ticket.md

# Create an Incident Ticket

> ❗️ Note:
>
> This step is deprecated. Please use the respective Runbook steps for each of our supported ticketing providers:
>
> * [Create an Asana Task](https://docs.firehydrant.com/docs/runbook-step-create-an-asana-task)
> * [Create a Linear Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-linear-issue)
> * [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue)
> * [Create a ServiceNow Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-servicenow-incident)
> * [Create a Shortcut Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-shortcut-issue)

## Prerequisites

<Image alt="Setting ServiceNow as the default project in settings" align="center" width="650px" src="https://files.readme.io/d50482c-image.png">
  Setting ServiceNow as the default project in settings
</Image>

* You must have configured the [ServiceNow](https://docs.firehydrant.com/docs/servicenow-integration) integration.
* You will need to set the ServiceNow instance as the "default project" in **Settings> Incidents > Ticketing settings > Default project.**

## Adding the step

<Image alt="Create an Incident Ticket (largely used for ServiceNow only)" align="center" width="650px" src="https://files.readme.io/e6f0b4a-image.png">
  Create an Incident Ticket (largely used for ServiceNow only)
</Image>

1. In a Runbook, edit, click "+ Add step," and then search for "Create an Incident Ticket."
2. In this step, fill in the details for the ticket summary and description (both fields support [template variables](https://docs.firehydrant.com/docs/template-variables).
3. When finished, click "Add step" and save the Runbook.

> 📘 Note:
>
> **Assign ticket to role** field does not currently work for ServiceNow. Setting a value there will not assign the ServiceNow incident record to any users.