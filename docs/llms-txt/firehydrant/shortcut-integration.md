# Source: https://docs.firehydrant.com/docs/shortcut-integration.md

# Shortcut

> 🚧 Effective September 1, 2024, this integration has entered maintenance mode.
>
> We will continue to support and maintain its current capabilities as described in our documentation. While we remain committed to the integration's stability and performance, please note that no new features or enhancements will be added.

Integrating FireHydrant with Shortcut lets you create and sync incidents and action items created in FireHydrant with stories in Shortcut.

## Prerequisites

* You'll need to be an <Glossary>Owner</Glossary> in FireHydrant to configure integrations
* You'll need a **service account**/**user** in Shortcut with owner permissions/role

> 📘 Note:
>
> FireHydrant recommends creating the Shortcut integration using a generic service/owner account rather than an individual named user to avoid problems if the named user were to depart the organization.

## Installing Shortcut integration

<Image alt="**Account profile \> Settings \> API Tokens**" align="center" width="650px" src="https://files.readme.io/6b3fed7-Screenshot_2024-01-08_at_5.19.02_PM_copy.png">
  **Account profile> Settings > API Tokens**
</Image>

1. Logged into the Shortcut as the **service account**, go to **Account profile> Settings > API Tokens**.
2. Fill in the input for Token Name and then click **Generate Token** to create a new token. Copy that token after it is generated.
3. Go to the [Integrations page](https://app.firehydrant.io/organizations/integrations) on FireHydrant and search for the Shortcut integration.
4. Click the '+' and then on the next page, fill in the API token you copied from step #2. Click **Authorize Application**.

### Configuring webhook to FireHydrant

You must configure a webhook with Shortcut to set up bi-directional integration.

1. On the Shortcut integration page, copy the webhook URL FireHydrant generated when you first installed Shortcut.

<Image alt="Generated webhook for Shortcut" align="center" width="650px" src="https://files.readme.io/5b74df9-Screenshot_2024-01-08_at_5.25.17_PM.png">
  Generated webhook for Shortcut
</Image>

2. In Shortcut, navigate to **Integrations** > **Webhooks**.
3. Click **Add New Webhook** and then insert the URL copied from above into the **Payload URL**. Leave **Secret** blank.
4. Paste the URL you copied from FireHydrant into the **Payload URL** section and then click **Add New Webhook**.

Once this webhook is configured, FireHydrant will receive updates whenever a ticket in Shortcut changes, including its status, and this will update with the linked Follow-Up in FireHydrant accordingly.

## Project Configuration

Before using the Shortcut integration, you'll need to configure a mapping for each Shortcut project you'd like FireHydrant to interact with so it knows what types of stories and story states to use when creating Shortcut stories.

1. From the Shortcut integration page in FireHydrant, scroll down to the **Projects** section and click '+ Add Project.'
2. A modal will pop up for you to select which Shortcut project to configure. Once you've chosen one, the project will be created, and you'll be taken to the project settings page with the following tabs.

### Incident Tickets

These settings will be necessary to [create incident tickets](https://docs.firehydrant.com/docs/runbook-step-create-a-shortcut-issue) in the Shortcut project but can be ignored if you only plan to use this project for Follow-Ups.

1. **Incident Default Issue Type** - This is the story type we'll use for incident tickets in Shortcut.

### Follow Ups

These settings will be necessary for [creating Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups) in this Shortcut project but can be ignored if you only plan to use this project for incident tickets.

These are the available fields:

* **Follow-up default issue type** - The type of story we'll create in your Shortcut project for Follow-Ups
* **Follow-up status mappings** - Maps the FireHydrant Follow-Up status to selected Shortcut story states. FireHydrant's terminology uses "Open," "In Progress," and "Done" to refer to a ticket's overall state.

### (Optional) Field Mapping

FireHydrant's incidents have [numerous out-of-box fields](https://docs.firehydrant.com/docs/incident-fields) as well as [custom fields](https://docs.firehydrant.com/docs/incident-custom-fields) of information you can track. Subsequently, it may be crucial for organizations to map these FireHydrant fields to specific fields in the created Shortcut stories, and FireHydrant's field mapping allows for this.

If you do need to map fields, proceed with the following steps:

1. Click '+ Add mapping' to create a new mapping.
2. A drawer will come out on the right where you can select between two choices:
   1. **Basic mapping** allows you to always set fields in Shortcut stories to the same values.
   2. **Advanced mapping** allows conditional logic to map different fields to different values in Shortcut stories based on various parameters within FireHydrant.

<Image alt="Mapping fields for Shortcut" align="center" width="650px" src="https://files.readme.io/6451e2d-image.png">
  Mapping fields for Shortcut
</Image>

3. You can select a Shortcut field once you've selected between basic vs. advanced mapping.
   1. If **Basic**, you can set the field's value, and this will apply each time you create the ticket and whenever any detail on the incident is updated.
   2. If **Advanced**, you can select conditions and values that should apply when those conditions are met, along with an **Else** default value if no conditions are met.

> 📘 Note:
>
> Field mappings for a project and its tickets are evaluated and applied upon every incident update. For example, if you have a condition to "set Short ticket Severity field to `SEV1` whenever the incident is is `SEV1`, otherwise default to `SEV3`," this will evaluate each time you make updates on the incident so that if the severity is escalated/de-escalated, the field in Shortcut will change accordingly.

## Removing a Configured Project

To avoid unexpected problems, before you delete a configured Shortcut project, ensure that you have accounted for any Runbook steps and linked incidents and action items that reference the project.

Go to the Shortcut integration settings to remove a configured Shortcut project from the integration.  Under **Projects**, click **Edit** next to the project you wish to remove, then select the **Delete Project** tab and **Delete permanently** button.  Confirm the action.

## Default Ticketing Project

When creating either incident tickets or follow-up action items, FireHydrant will use the Shortcut Project selected at that time (e.g., in the Runbook step, in the dropdown when creating a Follow-Up, etc.).

But if those don't exist or are not specified, FireHydrant can/will fall back to a **Default Project** you configure. In addition, if you are [creating Follow-Ups via emoji in Slack](/docs/managing-follow-ups#using-emojis-from-slack), this **Default Project** will also be used.

This can be configured in **Settings> Ticketing settings > Default project**.

<Image alt="Setting a default project in ticketing settings" align="center" width="650px" src="https://files.readme.io/7777305-Screenshot_2024-01-08_at_3.50.40_PM.png">
  Setting a default project in ticketing settings
</Image>

## Next Steps

* See how you can [automate creating a Shortcut story](https://docs.firehydrant.com/docs/runbook-step-create-a-shortcut-issue) as part of Runbook automation
* Learn more about [Managing Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups)
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)