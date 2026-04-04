# Source: https://docs.rootly.com/integrations/slack/workflows/send-slack-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Slack Blocks

## Overview

Sometimes a simple Slack message isn’t enough—especially during a fast-moving incident when responders need structured actions, rich context, and guided workflows.\
The **Send Slack Blocks** workflow action allows you to build complete interactive Slack experiences using [Slack’s Block Kit ](https://api.slack.com/reference/block-kit)framework.

With this action, you can:

* Send richly formatted messages to Slack channels, users, or user groups
* Provide responders with buttons that open Rootly modals or workflows
* Thread updates under existing messages
* Pin important updates
* Run custom workflows or present custom forms
* Mirror in-product toolbars directly inside Slack

This action is foundational for teams that want incident responders to take meaningful action without leaving Slack.

## Action Attributes

<Frame>
    <img src="https://mintcdn.com/rootly/6qP0tS1GNk4jbxrs/images/integrations/slack/workflows/send-slack-blocks/images-1.webp?fit=max&auto=format&n=6qP0tS1GNk4jbxrs&q=85&s=37f23093282d6a21ee23be11b44e739b" alt="Document Image" width="925" height="2126" data-path="images/integrations/slack/workflows/send-slack-blocks/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Slack Users

Specify the Slack user(s) you wish to send the custom Slack block to.

### Slack User Groups

Specify which Slack user group(s) you wish to send the custom Slack block to. All users part of the specified user group(s) will be sent the block. You can read more about Slack user groups [here](https://slack.com/help/articles/212906697-Create-a-user-group).

### Channels

This field specifies which Slack channels to send the Slack block to.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will send the block to the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be used for sub incidents and it will send the block to the Slack channel of the parent incident.
* You can also send blocks to static channel (e.g. `#general`, `#alerts`)

### Send as Ephemeral

If selected, your message will be sent as a **hidden** message visible only to the specified users.

A value must be set for the `Slack Users` or `Slack User Groups` and `Channels` when this field is selected. Additionally, the selected users need to be in the specified channels.

### Pin to Channel

If selected, your message will pinned to the specified channel(s).

### Message Threading Options

If you want to thread the block under an existing block/message that Rootly has previously sent, you can do so by selecting a parent block/message to be threaded under.

#### Filter Tasks by Workflow

This field is used to filter for the workflow that contains the specific action responsible for sending the parent message. The value in this field will not persist once the workflow is saved, as the `Select a Task` field is what ultimately determines the parent message to thread under.

#### Select a Task

This field is used to select the specific action that's responsible for sending the parent block/message. This field determines which block/message is the parent block/message to thread under.

#### Update Parent Message

If this field is selected, the workflow will update the original parent block/message, instead of threading underneath it.

#### Broadcast Thread Reply to Channel

If this field is selected, the threaded block will also be broadcasted as a new block in the specified channels.

### Notification Preview

Content in this field will be displayed in the push notifications. This field supports [Liquid variables](/liquid/incident-variables).

### Blocks

The blocks field consist of the payload that will be send in Slack. Customizing this payload will allow you to build custom messaging. The payload follows the same restrictions as Slack's block elements do. You can preview and check if your payload is valid by clicking the `Preview` button. This button will route you to [Slack's Block Kit builder](https://app.slack.com/block-kit-builder/).

<Warning>
  The [Block Kit builder](https://app.slack.com/block-kit-builder/) is a Slack-built application. So, it will not be able to recognize any Liquid variables that you might have referenced in your payload. You will need to use [Rootly's Incident Variable Explorer](https://rootly.com/account/help/liquid-explorer) in conjunction with Slack's Block Kit builder.
</Warning>

#### Select a Template Dropdown

You can choose any pre-built blocks from the `Select a template dropdown` field. This is a great starting point to get familiarized with Slack's Block Kit syntax.

#### Section

Selecting a section will append a pre-built section to your existing payload.

**Sample text block with markdown enabled**

```
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "Allows for *markdown formatting*: <https://api.slack.com/reference/surfaces/formatting#basics| Slack Markdown Formatting Guide>"
  }
}
```

**Sample image block**

```
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "Some *text* here with markdown support"
  },
  "accessory": {
    "type": "image",
    "image_url": "https://picsum.photos/200",
    "alt_text": "placeholder_image"
  }
}
```

#### Rootly Action IDs

Rootly provides a rich set of interactive actions that can be triggered directly from Slack messages using Block Kit buttons. Each action is identified by an `action_id`, which tells Rootly what modal, dialog, or workflow should open when a user clicks a button. These actions allow responders to manage incidents, assign roles, update forms, escalate through on-call systems, publish to status pages, trigger workflows, and more—all without leaving Slack.

Selecting an action will append a pre-built action element to your existing payload. Each block option here is customizable. The `action_id` field must be set to one of the following available values.

**Incident Editing and Toolbar Actions**

These actions mirror the primary controls available in the incident toolbar within the Rootly web interface. They allow responders to update key incident attributes directly from Slack, enabling fast and seamless adjustments during active incident response.

| Action ID                              | Description                                                                                                                                                             |
| :------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **toolbar\_update\_incident\_summary** | Opens the incident summary modal, allowing responders to refine or rewrite the customer-facing summary that appears across Slack, the web UI, and status pages.         |
| **toolbar\_update\_status**            | Launches the incident status update modal. This is the primary way to transition an incident through its lifecycle (e.g., In Triage → Mitigated → Resolved) from Slack. |
| **toolbar\_update\_incident**          | Opens the full incident editing modal, enabling responders to adjust severity, impacted services, environments, incident type, and any organization-specific fields.    |
| **toolbar\_available\_commands**       | Displays the Rootly “available commands” modal, giving responders a quick reference to the Slack commands and actions supported in the incident channel.                |
| **archive\_incident**                  | Archives the incident. This action should be used when the incident is no longer active and has been formally closed out of your operational workflow.                  |

These actions are most frequently used in workflow-generated Slack messages that serve as toolbars during incident response.

**Roles, Custom Fields, and Action Items**

These actions provide access to the deeper, structured metadata associated with an incident. They are helpful when you want responders to supply additional detail, update responsibilities, or manage follow-up work directly from Slack.

| Action ID                                       | Description                                                                                                                                                                        |
| :---------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **manage\_incident\_role\_assignments\_dialog** | Opens the role management modal, allowing assignment or reassignment of incident roles (e.g., Incident Commander, Communications Lead, Liaison).                                   |
| **manage\_form\_field\_selections**             | Opens the custom fields modal where responders can update any additional metadata your organization configures—such as customer segment, region, or incident classification.       |
| **manage\_incident\_action\_items**             | Provides an interface for creating, updating, or reviewing incident action items. This includes tasks assigned during the incident or added during retrospectives.                 |
| **todo\_dialog**                                | Shows the logged-in user a consolidated view of all action items assigned to them across the incident. This is particularly valuable for follow-up and ensuring nothing is missed. |
| **add\_feedback**                               | Opens a modal for submitting incident feedback. Teams typically use this after resolution to collect input from responders while context is still fresh.                           |

These actions ensure that critical metadata and structured follow-up work can be captured in real time.

**PagerDuty, Opsgenie, and VictorOps Responders**

If your team uses an on-call provider such as PagerDuty, Opsgenie, or VictorOps, these actions allow responders to request additional help directly from Slack. Rootly opens the appropriate native dialog based on the integration installed.

| Action ID                        | Description                                                                                                         |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| **pagerduty\_responders**        | Opens the PagerDuty responders dialog, allowing responders to bring additional on-call resources into the incident. |
| **opsgenie\_responders**         | Opens the Opsgenie responders dialog with equivalent functionality.                                                 |
| **victor\_ops\_responders**      | Opens the VictorOps responder dialog.                                                                               |
| **add\_pagerduty\_responders**   | Alias for the PagerDuty responders dialog; present in some workflows and payload schemas.                           |
| **add\_opsgenie\_responders**    | Alias for the Opsgenie responders dialog.                                                                           |
| **add\_victor\_ops\_responders** | Alias for the VictorOps responders dialog.                                                                          |

Action IDs in this category only function if the corresponding integration is installed and configured.

**Escalation Flow Navigation**

Rootly’s escalation modal consists of multiple steps, particularly when working with PagerDuty. These internal `action_id` values allow navigation between different screens within the escalation dialog.

| Action ID                                                      | Description                                                                                              |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| **escalate\_dialog**                                           | Opens the primary escalation dialog in Slack. This is the entry point for escalation during an incident. |
| **update\_pagerduty\_escalate\_dialog\_responders**            | Navigates to the step where responders are selected.                                                     |
| **update\_pagerduty\_escalate\_dialog\_escalate**              | Moves to the escalation decision page, where responders may be paged or re-paged.                        |
| **update\_pagerduty\_escalate\_dialog\_reassign**              | Opens the reassignment step, enabling teams to shift ownership or responsibility.                        |
| **update\_pagerduty\_escalate\_dialog\_create\_new\_incident** | Navigates to the page for initiating a new PagerDuty incident from Slack.                                |

These action IDs are mostly used internally by Rootly during modal interactions, but they are documented here for completeness and for teams that build highly customized Slack experiences.

**Status Page Publishing**

These actions open the modal used to publish incident updates to a Rootly status page. The difference between the two is primarily contextual: one is designed for general use, and the other appears when triggered from the incident overview toolbar.

| Action ID                                  | Description                                                                                                |
| :----------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **update\_status\_page\_dialog**           | Opens the modal for composing and publishing a status page event (e.g., Identified, Monitoring, Resolved). |
| **overview\_update\_status\_page\_dialog** | Opens the same modal, but from the context of the incident overview toolbar.                               |

Either may be used depending on where your Slack block resides.

**Workflow Reminder Controls**

Repeating workflow reminders—commonly used for prompting updates, stakeholder communications, or periodic status checks—can be controlled directly from Slack using these actions.

| Action ID             | Description                                                                                                 |
| :-------------------- | :---------------------------------------------------------------------------------------------------------- |
| **pause\_reminder**   | Pauses a repeating workflow reminder so that it no longer sends notifications.                              |
| **snooze\_reminder**  | Snoozes the reminder temporarily, allowing responders to quiet a notification stream during intense triage. |
| **restart\_reminder** | Restarts a previously paused workflow reminder and resumes its normal schedule.                             |

These actions are useful in time-based or scheduled periodic reminder workflows.

**Custom Workflows and Custom Forms**

These action IDs enable deep integration with your team’s automation and custom forms. They allow responders to invoke tailored, organization-specific actions directly from Slack messages.

| Action ID                     | Description                                                                                                                                                                       |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **trigger\_custom\_workflow** | Runs a custom workflow. This action requires that the Block Kit JSON include a `value` matching the workflow’s Slack command (found under *Advanced Settings* for that workflow). |
| **open\_custom\_form**        | Opens a custom Rootly form in Slack. Requires the `value` to correspond to a form slug configured in your workspace.                                                              |

These actions allow teams to design highly specialized Slack-driven workflows that reflect their internal processes.

**Example: Triggering a Custom Workflow**

```
  {
    "type": "actions",
    "elements": [
      {
        "type": "button",
        "style": "primary",
        "text": {
          "type": "plain_text",
          "emoji": true,
          "text": "Show Incomplete Action Items"
        },
        "value": "incident-list-out-incomplete-action-items",
        "action_id": "trigger_custom_workflow"
      }
    ]
  }
```

#### Attachments

Attach secondary content to your main message. Use this for content that adds further context or additional information but isn't vital. Please note attachments are a legacy part of the Slack messaging functionality. You should understand that they might change in the future, in ways that reduce their visibility or utility. See [Slack documentation for more details](https://api.slack.com/messaging/composing/layouts#attachments).

#### Troubleshooting

<AccordionGroup>
  <Accordion title="Message did not appear in Slack">
    * Confirm the workflow ran successfully\
      Check the workflow run history in Rootly to ensure the action was executed and did not fail validation.
    * Verify channels and recipients\
      Ensure the **Channels** field is set (for example, `{{ incident.slack_channel_id }}` or a valid `#channel` name) and that the Slack app has access to that channel.
    * Check Slack app permissions\
      Confirm that the Rootly Slack app is installed in the workspace and added to the target channels.
  </Accordion>

  <Accordion title="Ephemeral message is not visible">
    * Validate required targeting\
      For ephemeral messages, you must specify **Slack Users** or **Slack User Groups** and **Channels**.
    * Confirm channel membership\
      The targeted users must be members of the specified channels; Slack will silently drop ephemeral messages for non-members.
    * Test with a direct tag\
      Try sending an ephemeral block to a single known user and channel to isolate whether the issue is configuration or targeting.
  </Accordion>

  <Accordion title="Block Kit validation or rendering issues">
    * Use Block Kit Builder for structure\
      Copy the JSON (without Liquid) into Slack’s Block Kit Builder to validate structure and layout.
    * Add Liquid cautiously\
      After validation, reintroduce Liquid variables in Rootly. If a block suddenly fails, temporarily remove or simplify Liquid expressions to identify the culprit.
    * Avoid unsupported elements\
      Ensure you are only using Block Kit components that are supported in the surfaces where the message will appear.
  </Accordion>

  <Accordion title="Buttons do nothing when clicked">
    * Verify `action_id` values\
      Confirm that the `action_id` matches a supported Rootly action (for example, `toolbar_update_status`, `manage_form_field_selections`, `trigger_custom_workflow`).
    * Check integration prerequisites\
      Responder-related actions (such as `pagerduty_responders`, `opsgenie_responders`, `victor_ops_responders`) require the corresponding integration to be installed and configured.
    * Confirm permissions\
      Some modals (like status updates or role management) require the user to have permission to update the incident. If they do not, the click will not perform the expected action.
  </Accordion>

  <Accordion title="Custom workflow or form does not open">
    * Confirm the `value` field
      * For `trigger_custom_workflow`, the `value` must equal the workflow’s Slack command (under Advanced Settings).
      * For `open_custom_form`, the `value` must equal the custom form’s slug.
    * Check workflow state\
      Ensure the targeted workflow is enabled and not restricted by conditions that prevent it from running in this context.
    * Review logs or run history\
      If the workflow runs but does not behave as expected, inspect workflow logs for validation errors or unmet conditions.
  </Accordion>

  <Accordion title="Threading does not behave as expected">
    * Ensure “Select a Task” points to the correct parent\
      If the wrong parent action is selected, messages may thread under an unexpected Rootly message or appear as new root messages.
    * Check “Update Parent Message” vs. “Reply in Thread”\
      If you set “Update Parent Message”, no new thread reply will appear; the original message will be replaced.
    * Review “Broadcast Thread Reply to Channel”\
      If a reply appears both in thread and as a new root message, this option is enabled; disable it if you only want threaded responses.
  </Accordion>

  <Accordion title="Workflow did not run or message did not send">
    * Verify trigger conditions\
      Check that the workflow’s trigger and conditions (severity, type, environment, status, etc.) match the incident state when you expected it to fire.
    * Inspect workflow run history\
      Look for failed runs or validation errors related to Slack fields (for example, missing channels, invalid JSON, or failing Liquid).
    * Test with a simplified version\
      Temporarily simplify the workflow to a minimal “Send Slack Blocks” step with a static Block Kit payload to confirm that the basic action works, then reintroduce complexity incrementally.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).