# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-servicenow-work-note.md

# Create a ServiceNow Work Note

> ℹ️ Need to install in the ServiceNow integration?
>
> [Learn how](https://docs.firehydrant.com/docs/servicenow-copy).

This Runbook step automatically posts updates to your ServiceNow incident tickets as work notes, helping keep your ServiceNow tickets synchronized with FireHydrant incident activities.

## Prerequisites

Before you begin, ensure you have:

* Configured the ServiceNow integration in FireHydrant
* Set up at least one project within your ServiceNow integration

## Basic Configuration

1. Navigate to the Runbook step menu
2. Search for and select **"Create a ServiceNow Work Note"**
3. Configure the work note content using plain text or template variables

## Automating Incident Updates

A common use case is automatically synchronizing incident updates between FireHydrant and ServiceNow. Here's how to set this up:

**Template Configuration**

* Use the template variable \{\{ incident.last\_note.body }} to capture the latest incident note
* This will automatically include the content of new incident updates in your ServiceNow work notes

**Execution Settings**\
To ensure the step runs for every new incident update:

* Add the "Incident Note is added" condition
* Enable "Rerun on every transition" in the condition settings
* This configuration ensures the step executes each time a new note is added

<Image alt="Example conditions for re-executing on every new update" align="center" width="650px" src="https://files.readme.io/e94b63d9d268a161951bbc5422fd8c8e97f38f417ccc70498bbbf76bf4b2f58e-servicenow-worknote.png">
  Example conditions for re-executing on every new update
</Image>

## Result

With this configuration:

* Every incident note posted in FireHydrant (via chat or UI) automatically creates a work note in ServiceNow
* Your ServiceNow tickets stay current with all incident communications
* Team members in both systems have access to the latest information