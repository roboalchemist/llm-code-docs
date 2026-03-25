# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-servicenow-incident.md

# Create a ServiceNow Incident

> ℹ️ Need to install in the ServiceNow integration?
>
> [Learn how](https://docs.firehydrant.com/docs/servicenow-copy).

FireHydrant's ServiceNow integration enables automatic ticket creation at the start of an incident, streamlining your incident management workflow.

## Prerequisites

Before you begin, ensure you have:

* Configured the ServiceNow integration in FireHydrant
* Set up at least one project within your ServiceNow integration

> 📘 Note:
>
> FireHydrant currently supports creating one ServiceNow incident ticket per FireHydrant incident.

## Creating a ServiceNow Ticket

<Image alt="Create a Jira Cloud issue step. Jira Cloud and Jira Server Runbook steps look identical." align="center" src="https://files.readme.io/6dbda98fec89c2c89bf8ad53855f294fef7f3f3e33387297b802c63788e0631e-servicenow-runbook.png">
  Create a ServiceNow incident step.
</Image>

1. Navigate to the Runbook step menu
2. Search for and select **"Create a ServiceNow Incident"**
3. Configure the ticket settings:
   1. Select your target ServiceNow project
   2. Review and modify the auto-populated fields:
      1. Summary (defaults to Incident Name)\
         Description (defaults to Incident Description)
   3. Customize additional fields as needed

### Template Variables

You can enhance your ServiceNow tickets using FireHydrant's template variables. These allow you to dynamically insert incident-specific information into your tickets. For detailed guidance on available variables and usage, refer to our Template Variables documentation.

### Automation

Once configured in your Runbook, the ServiceNow ticket creation process becomes fully automated. Whenever an incident is initiated with this Runbook:

1. FireHydrant automatically creates a ServiceNow ticket
2. The ticket is linked to your FireHydrant incident
3. All relevant incident information is populated according to your configuration

<Image alt="Jira runbook step example" align="center" src="https://files.readme.io/7f22984a4f1d85ace0324571f3a9b3a466cbfb9a2b271fcc68ea1095029111cb-servicenow-incident-ticket.png">
  ServiceNow ticket created on an incident
</Image>