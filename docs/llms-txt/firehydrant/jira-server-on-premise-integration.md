# Source: https://docs.firehydrant.com/docs/jira-server-on-premise-integration.md

# Jira Server (On-Premise)

> 🚧 Note:
>
> FireHydrant supports Jira Server/Datacenter 8.x versions up through 8.3 out of box. If you are using Jira 8.4+ versions, please [reach out to support](https://firehydrant.zendesk.com/hc/en-us/requests/new?ticket_form_id=10839851937684) and ask to have it enabled for your organization, as this will impact some of your configuration.

FireHydrant can create tickets in Jira for each incident, with linked tickets for follow-ups to prioritize after the incident. This way, all actions proposed during an incident are tracked in your existing project management workflows for estimation and scheduling.

Please know that all steps in this document are required unless otherwise noted.

## Prerequisites

* You'll need to be an <Glossary>Owner</Glossary> in FireHydrant to configure integrations
* You need a **service account**/**user** in Jira with the following permissions:
  * **Project Permissions**
    * Browse Projects
  * **Issue Permissions**
    * Assign Issues
    * Close Issues
    * Create Issues
    * Edit Issues
    * Link Issues
    * Move Issues
    * Schedule Issues

> 📘 Note:
>
> FireHydrant recommends using a generic Jira Server service account rather than an individual named user to avoid problems if the named employee were to depart the organization.
>
> If you are using SSO with Jira Server, make sure that the Jira service account you use to authorize the integration is exempted from SSO (i.e. configured to authenticate with username and password instead).

### IP Access

We have static IP addresses from which we make all requests. If your Jira Server instance is behind a network perimeter or firewall, you can add the following two IPs to the allowed list so FireHydrant can access your Jira:

* **34.150.247.118**
* **35.185.58.206**

## Installing Jira Server integration

<Image alt="Jira Server tile in integrations" align="center" width="650px" src="https://files.readme.io/9b4a1f9-Screenshot_2024-01-08_at_4.33.59_PM.png">
  Jira Server tile in integrations
</Image>

1. Go to the [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for the Jira Server integration. Click the '+'.
2. On this page, you will have three inputs:
   1. **API Base URL** - The URL + port (if applicable) to your Jira server instance.
   2. **Username** - The username of the Jira service account you are using for this integration
   3. **Password** - The value for the API token associated with that user.
3. Click **Authorize Application**.

<Image alt="Filling in details for Jira Server" align="center" width="650px" src="https://files.readme.io/3861ac7-image.png">
  Filling in details for Jira Server
</Image>

### Configuring webhook to FireHydrant

To see updates to your tickets reflected in FireHydrant, you must configure an outbound webhook from Jira back to FireHydrant.

<Image alt="Jira integration settings page with generated webhook URL" align="center" width="400px" src="https://files.readme.io/6d5a405-Screenshot_2024-01-08_at_4.36.25_PM.png">
  Jira integration settings page with generated webhook URL
</Image>

1. Once you finish installing Jira, you should be taken back to the Jira integrations page, where you should see a **Webhook URL**. Copy this URL.
2. In Jira, configure a Webhook listener for FireHydrant using the copied URL. You can find this under **Settings> System > WebHooks**. On this screen, click "+
3. Set this webhook for the projects you plan to use with FireHydrant (or all issues), and then check the **Issue created** and **Issue updated** boxes.

<Image alt="Creating a new webhook in Jira" align="center" width="650px" src="https://files.readme.io/2195717-image.png">
  Creating a new webhook in Jira
</Image>

## Configuring Projects

<Image alt="Creating a project mapping for Jira Server" align="center" width="400px" src="https://files.readme.io/145c5d6-Screenshot_2024-01-08_at_4.39.08_PM.png">
  Creating a project mapping for Jira Server
</Image>

Before using the Jira integration, you'll need to configure a mapping for each Jira project you'd like FireHydrant to interact with so it knows what types of issues, issue states, or relationships to use when creating Jira tickets.

1. From the Jira integration page in FireHydrant, scroll down to the **Projects** section and click '+ Add Project.'
2. A modal will pop up for you to select which Jira project to configure. Once you've chosen one, the project will be created, and you'll be taken to the project settings page with the following tabs.

### Incident Tickets

These settings will be necessary to [create incident tickets](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) in this Jira project but can be ignored if you only plan to use this project for Follow-Ups.

1. **Incident Default Issue Type** - This is the issue type we'll use for incident tickets. Many FireHydrant users may create specific "Incident" issue types in Jira.
2. **Milestone Mappings** - You can configure different Jira ticket states and map them according to any of your <Glossary>Milestone</Glossary>mappings. For more information about Milestones in FireHydrant, visit [Lifecycle Phases](https://docs.firehydrant.com/docs/lifecycle-phases) and [Custom Milestones](https://docs.firehydrant.com/docs/custom-milestones) docs.

### Follow Ups

These settings will be necessary for [creating Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups) in this Jira project but can be ignored if you only plan to use this project for incident tickets.

For example, many FireHydrant organizations will have a specific "Incidents" project where FireHydrant creates incident tickets. Then, they may configure separate projects for different engineering teams to create Follow-Ups.

These are the available fields:

* **Default follow-up relationship to incident ticket** - This is the type of relationship to associate the new follow-up ticket to your incident ticket if one exists. The relationship originates with the new task (outward relationship in Jira parlance).
* **Follow-up default issue type** - The type of issue we'll create in your Jira project for Follow-Ups
* **Follow-up status mappings** - Maps the FireHydrant Follow-Up status to selected Jira issue statuses. FireHydrant's terminology uses "Open," "In Progress," and "Done" to refer to a ticket's overall state.

### Field Mapping

Jira is complex and highly configurable, so sometimes custom mappings need to be made between FireHydrant's incident fields and Jira's ticket fields.

If you have any ***custom required fields***, you will need to configure field mappings. Otherwise, FireHydrant cannot create tickets for your project(s).

To learn more about field mapping, visit [Jira Field Mapping](https://docs.firehydrant.com/docs/jira-field-mapping).

## Removing projects

To avoid unexpected problems, before you delete a configured Jira project, ensure that you have accounted for any Runbook steps and linked incidents and action items that reference the project.

Go to the Jira Server integration settings to remove a configured Jira project from the integration. Under **Projects**, click **Edit** next to the project you wish to remove, then select **Delete Project** tab and then **Delete permanently**. Confirm the action.

> 🚧 Note:
>
> If you delete a Jira project configuration, this will impact any Runbook steps that were pointing toward that project. Even if you re-add the same project in a new configuration, those Runbook steps will need to be removed and re-added, as each "connection" or "project" is unique and does not carry over between deletions/recreations.

## Default Ticketing Project

For any operations that require creating a Jira ticket, FireHydrant will use the Project selected (e.g., in the Runbook step, in the dropdown when creating a Follow-Up, etc.).

But if those don't exist or are not specified, FireHydrant can/will fall back to a **Default Project** you configure. In addition, if you are [creating Follow-Ups via emoji in Slack](/docs/managing-follow-ups#using-emojis-from-slack), this **Default Project** will also be used.

This can be configured in **Settings> Ticketing settings > Default project**.

<Image alt="Setting a default project in ticketing settings" align="center" width="650px" src="https://files.readme.io/7777305-Screenshot_2024-01-08_at_3.50.40_PM.png">
  Setting a default project in ticketing settings
</Image>

## Next Steps

* Review how to [automate creating Jira incident tickets](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) via Runbooks
* See how you can [create action items/follow-ups](https://docs.firehydrant.com/docs/managing-follow-ups) that create linked Jira tickets
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)