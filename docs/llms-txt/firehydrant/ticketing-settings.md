# Source: https://docs.firehydrant.com/docs/ticketing-settings.md

# Ticketing Settings

In addition to the settings for specific [ticketing providers](/docs/integrations-overview#ticketing-integrations), FireHydrant has some additional settings users can configure for Incidents and Follow-Ups that are configurable at **Settings> Ticketing settings** in the UI.

## Follow-Up Ticket Priorities

<Image align="center" border={true} caption="Example Priority Settings for Tickets" src="https://files.readme.io/7c37fc7561b3ca514fd408cf315a33aec205aecfa195864448f44344866a3b86-image.png" width="80% " />

When creating Follow-Up tickets, users can specify the Priority. Combined with custom field mapping for specific ticketing providers, these priorities can then be mapped to an external ticketing provider's priority values, ensuring that tickets created in external systems are set to correct values for prioritization of work.

<Image align="center" alt="Example mapping of FireHydrant Priority to Jira Priority" border={false} caption="Example mapping of FireHydrant Priority to Jira Priority" src="https://files.readme.io/7586621-image.png" />

Visit the documentation for your respective ticketing provider for more information on field mapping.

## General Ticketing Settings

### Default project for incident tickets

This chooses a default external ticketing integration project for two items:

* [Create an Incident Ticket](https://docs.firehydrant.com/docs/runbook-step-create-an-incident-ticket) Runbook step
* [Creating a Follow-Up](https://docs.firehydrant.com/docs/managing-follow-ups) with an emoji

Most users will not use the "Create an incident ticket" Runbook step. FireHydrant recommends using the specific Runbook steps for their respective ticketing providers:

* [Create an Asana Task](https://docs.firehydrant.com/docs/runbook-step-create-an-asana-task)
* [Create a Jira Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue)
* [Create a Shortcut Issue](https://docs.firehydrant.com/docs/runbook-step-create-a-shortcut-issue)

The only exception to this is for organizations using [ServiceNow](https://docs.firehydrant.com/docs/servicenow-integration), who will need to use this step since there is no dedicated "Create a ServiceNow ticket" Runbook step.

### Follow-up Title Template & Description Template

Organizations can fill in pre-templated content for Follow-up tickets. When creating a Follow-up ticket from either Slack or the Command Center web UI, this content will be prefilled in the input boxes, making it easier to quickly create tickets.

> 📘 Note:
>
> These fields support Liquid templating.

<Image align="center" alt="Example of pre-filled Liquid templating for Follow-ups" border={false} caption="Example of pre-filled Liquid templating for Follow-ups" src="https://files.readme.io/a126111-image.png" width="650px" />

<Image align="center" alt="How this looks pre-filled when creating a Follow-up" border={false} caption="How this looks pre-filled when creating a Follow-up" src="https://files.readme.io/49295c7-image.png" width="400px" />

<Image align="center" alt="How the Follow-up looks when it's created" border={false} caption="How the Follow-up looks when it's created" src="https://files.readme.io/99c5aac-Screenshot_2023-12-13_at_5.51.10_PM.png" />

## Ticketing Custom Fields

> 📘 Note:
>
> Modifying ticketing custom fields settings requires **Manage Incident Settings** permission within your organization.

Ticketing custom fields allow you to create custom fields specifically for Follow-Up tickets that can then be mapped to fields in your ticketing integration providers. This is useful when you need to collect additional information for tickets that isn't available in FireHydrant's standard follow up fields.

<Image align="center" border={false} caption="Follow Up Custom Fields Table" src="https://files.readme.io/7badeaaa9fdf35d451d75776f9ac7252ac8e3b13ca036bca2b15421ef4587a52-image.png" width="80% " />

### Why use ticketing custom fields?

The primary use case for ticketing custom fields is to enable Follow-Ups in FireHydrant to mimic your ticketing integration configuration (such as Jira). By configuring Follow-Up ticket fields to match your ticketing system's structure, you can:

* **Ensure consistency**: Follow-Up tickets in FireHydrant will have the same fields and requirements as tickets in your external ticketing system (e.g., Jira)
* **Collect required information upfront**: If your Jira project has custom required fields, you can create matching ticketing custom fields in FireHydrant so responders provide all necessary information before the ticket is created
* **Reduce errors**: By collecting information in FireHydrant first, you reduce the chance of missing required fields or data when tickets are created in your external system
* **Streamline workflows**: Responders can fill out all ticket information in one place (FireHydrant) rather than having to add missing fields after the ticket is created in your ticketing system

For example, if your organization uses Jira with custom required fields or specific field structures, you can create matching ticketing custom fields in FireHydrant. This ensures that when responders create Follow-Up tickets, they're prompted to provide the same information that your Jira configuration requires, creating a consistent experience and ensuring all necessary data is captured before tickets are created in Jira.

### Creating ticketing custom fields

<Image border={false} src="https://files.readme.io/95246edc8f8046705f024ddbdcb2fd9e3d777b7abfec40a672b40f5b5b1056d5-image.png" />

In the FireHydrant UI navigation, select **Settings** and then **Ticketing settings** and select the **Form fields** tab. On the top right, click "+ Add custom field".

In the custom field modal, you'll have the following fields:

1. **Display name** (required): The name as it will appear on forms and in the UI. The display name must be unique across the currently configured ticketing custom fields.
2. **Type** (required): The type of value for the field which can be one of the following: `String`, `Single-select`, `Multi-select`, and `DateTime`.
   * Single- and multi-select fields require at least one specified option, and you can change the order in which the options are displayed.
   * DateTime fields will store the values in ISO 8601 format (e.g., `2024-08-02T11:02:00.000Z`).
3. **Help Text**: A helpful description for completing the field that appears in tooltips for your responders.
4. **Visbility/Requirement Settings**: Specifies how the field appears when creating Follow-Up tickets. You can set the field to one of the following:
   * **Not Required: Visible**: The field is optional and will be visible on the form when creating a Follow-Up ticket.
   * **Not Required: Hidden**: The field will not appear on the form when creating a Follow-Up ticket, but can still be used in field mappings for ticketing integrations.
   * **Required**: The field must be filled in when creating a Follow-Up ticket and will be visible on the form.

### Editing ticketing custom fields

In the FireHydrant UI navigation, select **Settings**, **Ticketing settings**, and select the **Form fields** tab. In the table of ticketing custom fields, find the custom field you wish to edit and click the **Edit icon**.

You will be able to modify the display name, help text, field settings (required, available, or hidden), and for single- and multi-select fields, you will also be able to modify the options available in those fields. You cannot convert the field to a different type (e.g., string to single-select) - you will need to create a new field.

### Removing ticketing custom fields

In the FireHydrant UI navigation, select **Settings**, **Ticketing settings**, and select the **Form fields** tab. In the table of ticketing custom fields, find the custom field you wish to remove and select the **Delete icon**.

> 🚧 Note:
>
> Field removals cannot be undone. You will need to create a new field to "re-add" a deleted ticketing custom field.