# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-shortcut-issue.md

# Create a Shortcut Issue

<Image alt="Create a Shortcut Issue step" align="center" width="650px" src="https://files.readme.io/d3d7158-image.png">
  Create a Shortcut Issue step
</Image>

Like the Jira issue creation steps, FireHydrant supports integration with [Shortcut](https://docs.firehydrant.com/docs/shortcut-integration) and creating incident tickets.

> 📘 Note:
>
> Currently, FireHydrant only allows one top-level incident Shortcut ticket per FireHydrant incident.

## Prerequisites

You must have [Shortcut](https://docs.firehydrant.com/docs/shortcut-integration) integrated and at least one project configured.

## Adding the step

To add the step, go to a Runbook's edit page, and then when adding a step, search for "Shortcut."

The step allows filling in a few fields:

* **Project** - The Shortcut project you'd like to create a ticket in
* **Ticket Summary** - The title of the ticket
* **Ticket Description** - Description of ticket

Both ticket summary and description fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables)