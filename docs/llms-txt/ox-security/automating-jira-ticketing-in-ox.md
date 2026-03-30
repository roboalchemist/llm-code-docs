# Source: https://docs.ox.security/ticketing-and-messaging/ticket-management/jira/automating-jira-ticketing-in-ox.md

# Automating Jira Ticketing

In addition to [creating Jira tickets from OX](https://docs.ox.security/ticketing-and-messaging/ticket-management/jira), you can automate several aspects of how security issues are tracked and updated in Jira. These automations help you sync key information between platforms, reduce manual updates, and ensure consistency across issue workflows.

You can automatically add comments to Jira tickets based on actions taken in OX, set due dates aligned with your SLAs or custom rules, and map issue severity to Jira priorities. These capabilities improve collaboration between security and development teams by keeping Jira issues accurate and up to date.

You can also dynamically populate Jira ticket fields using contextual values from OX issues. This allows required Jira custom text fields and labels to be automatically filled with issue-specific data when a ticket is created, instead of using static values.

The following automated capabilities are available:

* [Adding comments to Jira tickets](https://docs.ox.security/ticketing-and-messaging/ticket-management/jira/page-1)
* [Mapping default due dates](#mapping-default-due-dates)
* [Mapping Jira priorities](#mapping-jira-priorities)
* [Closing Jira tickets](#closing-jira-tickets)

## Mapping default Due Dates

You can add to a Jira ticket a custom field named Due Date and then configure a default Due Date value in OX platform based on the OX issue severity. This helps ensure that tickets align with your SLA expectations without requiring manual date entry.

> **Note:** Jira ticket must include the Due Date field for this mapping to work. If you manually change the value of the Due Date parameter in Jira while creating the ticket, that value overrides the default defined in OX.

For example, if a critical issue has a 3-day SLA, the Due Date parameter in Jira will automatically be set to 3 days from the ticket creation date, unless manually overridden.

**To map default Due Dates:**

1. Go to **Settings > TICKETING AND MESSAGING**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3c6575683bfd218ab99736023ac2c74f640e4fe3%2FDue_Dates.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Enable **Add Due Dates to Jira tickets**.
2. Set the **Due Date** parameter in Jira in one of the following ways:

* **Use Due Dates from OX SLA Settings**: The **Due Date** is automatically taken from the **Settings > SLA** definitions in OX.
* **Set default Due Dates**: Define manually SLA for each severity level. These settings override all the other SLA settings for the selected issues.

## Mapping Jira Priorities

You can map issue severity levels in OX to the Priority parameter values in Jira. This ensures that each ticket created reflects the appropriate level of urgency within your existing Jira workflows.

For example, mappings might include:

* `Critical` severity → `Highest` Jira priority
* `High` severity → `High` Jira priority
* `Medium` severity → `Medium` Jira priority

After you configure these settings, all the they are applied automatically for all the new when tickets created for OX issues.

**To map priorities:**

1. Go to **Settings > TICKETING AND MESSAGING**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-71df66e9286eff61b7b7a32e949899d8e8dda468%2FPrioritization.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Enable **Map severity to Jira Priority field**.
2. Enable the severity levels that you want to map and define the **Priority** value in Jira associated with each severity level in OX.

## Closing Jira tickets

You can configure automatic Jira ticket closure when an issue is resolved or excluded.

Depending on your organization's Jira status settings, you can select the status that is applied to closed tickets.

The process runs automatically once configured.

**To set automatic status updates:**

1. Go to **Settings > TICKETING AND MESSAGING**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-94203faac73c3dc7a11696019e7b6b8024473e48%2Fclose%20issues.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Enable the automatic Jira ticket closure option(s).
2. For each closure option, set the status that you want to appear in Jira when the ticket is closed.

## Mapping Dynamic Jira Fields

You can configure Jira ticket fields to be populated dynamically using contextual values from OX issues.

Instead of entering static text, you can insert dynamic parameters that are resolved automatically when the Jira ticket is created. Each ticket will contain values specific to the issue that triggered it.

Dynamic parameters are supported for required Jira custom fields of type String (Text), as well as for the Labels field.

When configuring ticket creation in a workflow or during manual ticket creation, type `@` in a supported text field to select an available issue attribute.

Supported parameters include:

• License\
• Application name\
• Library name\
• Library version\
• CVSS score\
• Repository name\
• Tags

When a ticket is created:

• Static values remain identical across all tickets.\
• Dynamic parameters are resolved per issue before the ticket is sent to Jira.

Field Support Rules

Dynamic parameters are supported only when:

• The Jira field is defined as Required.\
• The field type is String (Text).

If a required field is not of type String, it appears in the configuration but does not support dynamic parameters.

If a field is not defined as Required in Jira, it does not appear in OX for mapping.

The list of available custom fields is synchronized with the Jira project configuration.

Supported Flows

Dynamic parameters are supported in:

• Workflow-based Jira ticket creation\
• Manual Jira ticket creation
