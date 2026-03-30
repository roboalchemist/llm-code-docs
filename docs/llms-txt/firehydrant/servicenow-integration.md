# Source: https://docs.firehydrant.com/docs/servicenow-integration.md

# ServiceNow

ServiceNow is a cloud-based workflow automation platform. It enables users to optimize workflows by automating repetitive tasks across platforms.

Integrating FireHydrant with ServiceNow enables you to create and manage incidents using best practices from FireHydrant while keeping ServiceNow as a source of all your teams’ work.

## Available Features

* Automatically create and link ServiceNow incident records when FireHydrant incidents are created (via [Create a ServiceNow Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-servicenow-incident) runbook step)
* Automatically create and link a FireHydrant incident when a ServiceNow incident record is created (via [ServiceNow Business Rules](https://docs.firehydrant.com/docs/servicenow-business-rules))
* Automatically create and link a ServiceNow ticket when FireHydrant [Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups) are created
* Automatically post FireHydrant incident updates as ServiceNow Work Notes on the incident record (via [Create a ServiceNow Work Note](https://docs.firehydrant.com/docs/runbook-step-create-a-servicenow-work-note) runbook step)
* [Custom status and field mapping](https://docs.firehydrant.com/docs/servicenow-field-mapping) between FireHydrant and ServiceNow
* Automatically [synchronize services](https://docs.firehydrant.com/docs/servicenow-cmdb) between FireHydrant and ServiceNow

## Prerequisites

* You'll need <Glossary>Owner</Glossary> permissions on FireHydrant
* You need administrative permissions in ServiceNow. This can be any admin account, but the user configuring ServiceNow with FireHydrant must have permissions to:
  * Create and manage OAuth applications
  * Create and manage User accounts
* You'll also need to create a generic service account in SNOW.
  * This account needs the following API access:
    * Table API access
    * CMDB Instance API access
    * Permissions to create and update records in your incident tables
  * We recommend using `web_service_admin`, `rest_api_explorer`, and `itil` roles as a starting point.

> 📘 Note: Use a generic ServiceNow service account
>
> FireHydrant recommends using a generic ServiceNow service account rather than an individual named user to avoid problems if the named employee were to depart the organization.

## Installing the ServiceNow integration in FireHydrant

### OAuth Application Setup:

<Image alt="ServiceNow connection setup" align="center" src="https://files.readme.io/f80242931f23a1b2aa37272cb7bf33f2a712b668c165e921149253cc66c790ab-servicenow-connection.png">
  ServiceNow connection setup
</Image>

1. Log into ServiceNow with your admin account
2. Navigate to **System OAuth → Application Registry**
3. Click 'New' and select 'Create an OAuth API endpoint for external clients'
4. Configure the OAuth application:
   1. **Name**: FireHydrant Integration
   2. **Grant Type**: Resource Owner Password Credentials
   3. **OAuth Application User**: Look up and select the generic service account configured in the Prerequisites section.
   4. **Redirect URL**: `https://app.firehydrant.io/auth/service_now/callback`
5. Click 'Submit' and save the generated Client ID and Client Secret
6. Go to the FireHydrant Integrations page (**Settings > Integrations list**) and search for ServiceNow. Click the **'+'.**
7. Enter your Instance URL, ServiceNow Username/Password, Client Id,  and Client Secret on this page and click **Continue to Table Selection**.

### Configure ServiceNow Tables

#### Ticketing Tables

<Image alt="ServiceNow table configuration" align="center" width="650px" src="https://files.readme.io/830c4c780579f59ccc4baefcb07619969e2e5e982cee4ad1dd1717cf53844268-servicenow-configure-table.png">
  ServiceNow table configuration
</Image>

* Select the ServiceNow tables that FireHydrant should create tickets in. We've pre-populated common ServiceNow tables, but you can add custom tables if needed.
* Type a table name and press enter to add it as a Ticketing table.

#### Services Tables (Optional)

<Image alt="Example CMDB service table to include" align="center" width="650px" src="https://files.readme.io/af9aabdedfa16ebd2793e9dd18deefa97472391e1f9662934ba7dbd92c77256d-service-now-cmdb.png">
  Example CMDB service table to include
</Image>

* Select tables that contain service-related data. FireHydrant will import these as services, mapping the name field from each table entry to create corresponding services in FireHydrant.
* Type a table name and press enter to add it as a Service table.

> 🚧 Note:
>
> You must add the CMDB service table now at setup if you want to incorporate your CMDB services. FireHydrant currently doesn't supporting updating which tables sync to FireHydrant at a later date.

#### Authorize ServiceNow

* After you have configured ServiceNow tables click **Authorize ServiceNow**

### Ticketing Project

<Image alt="ServiceNow ticketing project" align="center" width="650px" src="https://files.readme.io/0f28da01a2464d054aded73948e2bfe284a153d58d00124a9011370e1f69e4e4-servicenow-project.png">
  ServiceNow ticketing project
</Image>

Before using the ServiceNow integration with incidents and follow ups, you will need to configure a mapping for each ServiceNow project you would like FireHydrant to interact with so we know what types of issue states to use when creating ServiceNow tickets. To start, select a project to integrate with.

* Select Ticketing Project from the dropdown menu and click **Use this Project**
* Click **Continue** to begin setting up issue types and statuses for incident tickets and follow ups.

### Incident Tickets

These settings will be necessary to create incident tickets in ServiceNow but can be ignored if you only plan to use this project for Follow-Ups.

<Image align="center" width="550px" src="https://files.readme.io/11cd0aee0a441c31824565879ad44ec9e3873cd655c03612ce43b3b192e8b65a-servicenow-milestones.png" />

1. **Milestone Mappings** - These are the ServiceNow ticket statuses we'll use in ServiceNow to correspond to the FireHydrant incident's <Glossary>Milestone</Glossary>.
   1. Any **Active** incident in FireHydrant corresponds to milestones in the "Active" Lifecycle phase. The default milestones are: **Started**, **Detected**, **Acknowledged**, **Investigating**, **Identified**, and **Mitigated**.
   2. Any **Inactive** incident in FireHydrant corresponds to the "Post-Incident" Lifecyle phase. The default milestones are: **Resolved**, **Retrospective Started**, and **Retrospective Completed**.

### Follow Ups

These settings will be necessary for creating Follow-Ups in this ServiceNow but can be ignored if you only plan to use this project for incident tickets.

For example, many FireHydrant organizations will have a specific "Incidents" project where FireHydrant creates incident tickets. Then they may configure separate projects for different engineering teams to create Follow-Ups.

The available field:

* **Follow-up status mappings** - Maps the FireHydrant Follow-Up status to selected ServiceNow issue statuses. FireHydrant's terminology uses "**Open**," "**In Progress**," and "**Done**" to refer to a ticket's overall state.

### Testing

<Image alt="Testing the ServiceNow integration" align="center" width="500px" src="https://files.readme.io/dda6b0014dbaa4e9f7e088237d6b1129f00642ca6265125de3e3f6e67c28a9e2-servicenow-testing.png">
  Testing the ServiceNow integration
</Image>

Your project is now configured for one way sync to ServiceNow.  Next, we will add this project to a runbook and test the connection.

* Select a runbook from the dropdown or choose **New runbook** to create a new runbook to test. Click **Add and test**
  * A new incident with `GAMEDAY` severity, will be created it will have the runbook selected attached with both a ServiceNow incident and follow-up ticket

## Setting ServiceNow as the default ticketing project

<Image alt="Selecting ServiceNow as the default project" align="center" width="650px" src="https://files.readme.io/c67d75e-image.png">
  Selecting ServiceNow as the default project
</Image>

1. Go to **Settings> Ticketing settings**.
2. Under **Default project**, select the ServiceNow project you just configured.
3. Click **Save settings**.

## Creating a ServiceNow incident from a Runbook step

You can create a ServiceNow incident from the Create a ServiceNow Incident step. This allows you to create an incident record in ServiceNow automatically any time you create an incident in FireHydrant.

## Next Steps

* Learn about [ServiceNow Field Mapping](https://docs.firehydrant.com/docs/servicenow-field-mapping) and how to map FireHydrant values and Jira issue fields
* Set up a [ServiceNow Business Rule](https://docs.firehydrant.com/docs/servicenow-business-rule)
* View the [ServiceNow Business Rule Recipe](https://docs.firehydrant.com/recipes/servicenow-business-rule)
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)
* Look at the [full library of available Runbook steps](https://docs.firehydrant.com/docs/runbook-steps)