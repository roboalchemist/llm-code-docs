# Source: https://docs.firehydrant.com/docs/jira-cloud-integration.md

# Jira Cloud

FireHydrant can create tickets in Jira for each incident, with linked tickets for follow-ups to prioritize after the incident. This way, all actions proposed during an incident are tracked in your existing project management workflows for estimation and scheduling.

Please know that all steps in this document are required unless otherwise noted.

## Prerequisites

* You'll need to be an **Owner** in FireHydrant to configure integrations
* You need a service account/user in Jira with the following permissions:
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

<Callout icon="📘" theme="info">
  **Note**:

  FireHydrant recommends using a generic Jira Cloud service account rather than an individual named user to avoid problems if the named employee were to depart the organization.
</Callout>

## Installing Jira Cloud integration

<Image align="center" alt="Integrations page Jira cloud" border={false} caption="Finding the Jira tile in integration" src="https://files.readme.io/ac7e8030bafbc3134e07ca81edcc862b16fbe4eaeba70173ddf26b376b921cc4-CleanShot_2025-09-11_at_12.26.402x.jpg" width="650px" />

<Callout icon="🚧" theme="warn">
  **Note**:

  Ensure you are currently logged into Jira as the service account and not in your personal account, otherwise the connection will be established with your personal account.
</Callout>

1. Go to the [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for the Jira Cloud integration. You can also view our [Jira Marketplace listing](https://marketplace.atlassian.com/apps/1227095/firehydrant), which lists the same instructions.
2. Click the '+', and then click **Authorize Application**. This will take you to Jira where you can authorize FireHydrant's application. Follow through the on-screen prompts.

### Configuring webhook to FireHydrant

To see updates to your tickets reflected in FireHydrant, you must configure an outbound webhook from Jira back to FireHydrant.

<Image align="center" alt="Jira integration settings page with generated webhook URL" border={false} caption="Jira integration settings page with generated webhook URL" src="https://files.readme.io/c820e23b1d5511ab9f1d45c714e2f498c0d60e61cb85d0a347b7dd47f18e2cf6-CleanShot_2025-09-11_at_12.40.092x.jpg" width="400px" />

1. Once you finish installing Jira, you should be taken back to the Jira integrations page, where you should see a **Webhook URL**. Copy this URL.
2. In Jira, configure a Webhook listener for FireHydrant using the copied URL. This is under **Settings > System > Webhooks**. On this screen, click "+".
3. Set the JQL for the projects you plan to use with FireHydrant (or leave empty for all issues), and then check the **Issue created** and **Issue updated** boxes.

<Image align="center" alt="Creating a new webhook in Jira" border={false} caption="Creating a new webhook in Jira" src="https://files.readme.io/2195717-image.png" width="650px" />

### Individual account linking

When creating Incident tickets [via Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue), the Reporter of the Jira ticket will be set to the default authorized user on the account (e.g., whichever account was logged in when setting up the Jira integration).

However, for individual [Follow-Up tickets](https://docs.firehydrant.com/docs/managing-follow-ups) created during incidents, FireHydrant will try to set the Reporter to the person who created the Follow-Up. To correctly do this, users must authorize FireHydrant to create tickets as them in their settings. If users do not link their Jira and FireHydrant accounts, they can still create Follow-Ups, but FireHydrant will fall back to the default authorized user as the Reporter in that instance.

<Image align="center" alt="Linking a user's FireHydrant account with their Jira account" border={false} caption="Linking a user's FireHydrant account with their Jira account" src="https://files.readme.io/3aad72aa2d916c857518436eaa109c4c9d7a0a2d5eb02a0855a463dc1126b543-CleanShot_2025-09-11_at_12.46.312x.jpg" width="650px" />

To connect FireHydrant and Jira accounts, each individual will need to:

1. Go to their [User Settings](https://web.archive.org/web/20250803201327mp_/https://app.firehydrant.io/account/edit) and click on their organization.
2. Click **Link Jira Cloud**.
3. The next page that opens gives you the option to let FireHydrant access your Atlassian account. After you click **Accept**, FireHydrant can correctly associate action items and tickets that you have created with your user ID in Jira Cloud.

<Callout icon="📘" theme="info">
  **Note**:

  Once a user has linked their FireHydrant account to Jira account, creating Follow-Ups linked to Jira projects will set the user as the Reporter. Subsequently, the user will need appropriate permissions for the Jira project in which they're trying to create a ticket.
</Callout>

## Configuring projects

<Image align="center" alt="Creating a Jira mapping in Jira Cloud settings" border={false} caption="Creating a Jira mapping in Jira Cloud settings" src="https://files.readme.io/4a12cb52949eeb0e052257cbf67c1c222d950c11676e511b411f58c75778b4d7-CleanShot_2025-09-11_at_13.13.452x.jpg" width="400px" />

Before using the Jira integration, you'll need to configure a mapping for each Jira project you'd like FireHydrant to interact with so it knows what types of issues, issue states, or relationships to use when creating Jira tickets.

1. From the Jira integration page in FireHydrant, scroll down to the **Projects** section and click '+ Add Project.'
2. A modal will pop up for you to select which Jira project to configure. Once you've chosen one, the project will be created, and you'll be taken to the project settings page with the following tabs.

### Incident tickets

<Image align="center" border={false} caption="Incident tickets configuration" src="https://files.readme.io/3fc880c599ac74762641bb23ec7508de74bcd0c9b8e738fb1d5481c331085d04-CleanShot_2025-09-11_at_13.15.442x.jpg" width="650px" />

These settings will be necessary to [create incident tickets](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) in a Jira project but can be ignored if you only plan to use this project for [follow-ups](https://docs.firehydrant.com/docs/managing-follow-ups).

1. **Incident Default Issue Type** - This is the issue type we'll use for incident tickets. Many FireHydrant users may create specific "Incident" issue types in Jira.
2. **Milestone Mappings** - You can map different Jira ticket states to any of your FireHydrant Milestones. For more information about Milestones in FireHydrant, visit [Lifecycle Phases](https://docs.firehydrant.com/docs/lifecycle-phases) and [Custom Milestones](https://docs.firehydrant.com/docs/custom-milestones) docs.

### Follow-ups

<Image align="center" border={false} caption="Follow-up tickets configuration" src="https://files.readme.io/87290f3d49397da0524c24f5a3b199834765a0f54be7c7158dce361592691168-CleanShot_2025-09-11_at_13.25.012x.jpg" width="650px" />

These settings will be necessary for creating [follow-up tickets](https://docs.firehydrant.com/docs/managing-follow-ups) in this Jira project but can be ignored if you only plan to use this project for [creating incident tickets](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue).

For example, many FireHydrant organizations will have a specific "Incidents" project where FireHydrant creates incident tickets. Then they may configure separate projects for different engineering teams to create Follow-Ups.

These are the available fields:

1. **Default follow-up relationship to incident ticket** - This is the type of relationship to associate the new follow-up ticket to your incident ticket if one exists. The relationship originates with the new task (outward relationship in Jira parlance).
2. **Follow-up default issue type** - The type of issue we'll create in your Jira project for Follow-Ups
3. **Follow-up status mappings** - Maps the FireHydrant Follow-Up status to selected Jira issue statuses. FireHydrant's terminology uses "Open," "In Progress," and "Done" to refer to a ticket's overall state.

### Field Mapping

Jira is complex and highly configurable, so sometimes custom mappings need to be made between FireHydrant's incident fields and Jira's ticket fields.

You will need to configure field mappings if you have any custom required fields, otherwise FireHydrant will not be able to create tickets in your project(s).

To learn more about field mapping, visit [Jira Field Mapping](https://docs.firehydrant.com/docs/jira-field-mapping).

## Removing projects

To avoid unexpected problems, before you delete a configured Jira project, ensure that you have accounted for any Runbook steps and linked incidents and action items that reference the project.

Go to the Jira Cloud integration settings to remove a configured Jira project from the integration. Under **Projects**, click **Edit** next to the project you wish to remove, then select **Delete Project** tab and then **Delete permanently**. Confirm the action.

<Callout icon="🚧">
  **Note**:

  If you delete a Jira project configuration, this will impact any Runbook steps that were pointing toward that project. Even if you re-add the same project in a new configuration, those Runbook steps will need to be removed and re-added, as each "connection" or "project" is unique and does not carry over between deletions/recreations.
</Callout>

## Default Ticketing Project

For any operations that require creating a Jira ticket, FireHydrant will use the explicit Project selected (e.g., in the Runbook step, in the dropdown when creating a Follow-Up, etc.).

But if those don't exist or are not specified somehow, FireHydrant can/will fall back to a **Default Project** you configure. In addition, if you are creating follow-ups via emoji in Slack, this Default Project will also be used.

This can be configured in **Settings > Ticketing settings > Default project**.

<Image align="center" border={false} caption="Setting a default project in ticketing settings" src="https://files.readme.io/a0d4de8849efbf674225a05c0191e37d40fd77f50842aaf131a90fcc7f98d519-CleanShot_2025-09-11_at_13.29.372x.jpg" width="650px" />

## Alert Routing

Jira has "alert routing" capabilities, which allow FireHydrant to take action on inbound webhooks from the Jira instance automatically.

This allows, for example, the creation of Jira tickets in certain projects or matching specific parameters to start incidents in FireHydrant or notify certain Slack channels automatically.

To learn more about how it works, visit our [Alert Routing](https://docs.firehydrant.com/docs/alert-routing) documentation. Below is an example showing a typical use case where any ticket created in an "Incidents" project automatically starts an incident on FireHydrant.

<Callout icon="🚧">
  **Note**:

  Alert Routing should not be confused for [Signals](https://docs.firehydrant.com/docs/signals-introduction), as they are separate systems.
</Callout>

<Image align="center" alt="ACIR = Acme Company Incident Response" border={false} caption="Example alert routing config to open a FireHydrant incident ticket's project key is ACIR" src="https://files.readme.io/a737242e3dbd3b3a591a6bdc1cf633d6b0ee1187f720dd2c87958c491a534061-CleanShot_2025-09-11_at_14.24.242x.jpg" width="650px" />

### Parameter Mappings

The table below shows the available parameters you can filter on and how to access them via Liquid templating.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter Name
      </th>

      <th>
        Jira Webhook Body
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Jira: Status Category
      </td>

      <td>
        `request.body.issue.fields.status.statusCategory.key`
      </td>

      <td>
        The key of the status category for the issue's status
      </td>
    </tr>

    <tr>
      <td>
        Jira: Status
      </td>

      <td>
        `request.body.issue.fields.status.name`
      </td>

      <td>
        The Jira status of the created issue.
      </td>
    </tr>

    <tr>
      <td>
        Jira: Project Type Key
      </td>

      <td>
        `request.body.issue.fields.project.projectTypeKey`
      </td>

      <td>
        Project type key of the project the issue was created in. For example, `software`.
      </td>
    </tr>

    <tr>
      <td>
        Jira: Project Key
      </td>

      <td>
        `request.body.issue.fields.project.key`
      </td>

      <td>
        Key of project issue was created in
      </td>
    </tr>

    <tr>
      <td>
        Jira: Project Name
      </td>

      <td>
        `request.body.issue.fields.project.name`
      </td>

      <td>
        Name of project issue was created in
      </td>
    </tr>

    <tr>
      <td>
        Jira: Priority
      </td>

      <td>
        `request.body.issue.fields.priority.name`
      </td>

      <td>
        Priority of created issue
      </td>
    </tr>

    <tr>
      <td>
        Jira: Description
      </td>

      <td>
        `request.body.issue.fields.description`
      </td>

      <td>
        Description or body of the Jira issue
      </td>
    </tr>

    <tr>
      <td>
        Jira: Created At
      </td>

      <td>
        `request.body.issue.fields.created`
      </td>

      <td>
        When the ticket was created in ISO 8601 formatted datetime. For example:
        `2024-01-23T14:25:05.774-0700`
      </td>
    </tr>

    <tr>
      <td>
        Jira: Summary
      </td>

      <td>
        `request.body.issue.fields.summary`
      </td>

      <td>
        The **Summary** field within Jira (usually the title)
      </td>
    </tr>

    <tr>
      <td>
        Jira: API URL
      </td>

      <td>
        `request.body.issue.self`
      </td>

      <td>
        The URL for this specific Jira ticket included as the `self` parameter. Usually comes in the format of: `https://[your-workspace].atlassian.net/ rest/api/2/[issue_id]`
      </td>
    </tr>

    <tr>
      <td>
        Jira: ID
      </td>

      <td>
        `request.body.issue.id`
      </td>

      <td>
        The Jira issue ID. Number is generated and assigned by Jira on issue creation.
      </td>
    </tr>
  </tbody>
</Table>

The following table maps our overall Alert Routing mapping object - these parameters are standard across all Alerting/Monitoring integrations and are derived from above parameters.