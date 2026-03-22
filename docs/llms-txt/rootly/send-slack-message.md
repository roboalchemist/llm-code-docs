# Source: https://docs.rootly.com/integrations/slack/workflows/send-slack-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Slack Message

## Description

This action sends a message to Slack channels, users, and user groups.

## Action Attributes

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/kMnLuRjX9XFq2H7j/images/integrations/slack/workflows/send-slack-message/images-1.webp?fit=max&auto=format&n=kMnLuRjX9XFq2H7j&q=85&s=250d6ea4a382323d1a0677d6d81d6467" width="920" height="1299" data-path="images/integrations/slack/workflows/send-slack-message/images-1.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Slack Users

Specify the Slack user(s) you wish to send the custom Slack message to.

### Slack User Groups

Specify which Slack user group(s) you wish to send the custom Slack message to. All users part of the specified user group will be sent the message. You can read more about Slack user groups [here](https://slack.com/help/articles/212906697-Create-a-user-group "here").

### Channels

This field specifies which Slack channel(s) to send the Slack message to.

Some common selections:

* Setting to `{{ incident.slack_channel_id }}` will send the message to the Slack channel of the triggering incident.
* The Liquid syntax `{{ parent_incident.slack_channel_id }}` can be used for sub incidents and it will send the message to the Slack channel of the parent incident.
* You can also send messages to static channel (e.g. `#general`, `#alerts`)

### Actions

Slack messages can also be sent with buttons that are linked to actions. The current available actions are listed below.

| Action                      | Description                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Update Summary`            | Surfaces a Slack modal that allows you to update the incident's summary.                                                                                           |
| `Manage Incident Roles`     | Surfaces a Slack modal that allows you to manage your incident's role assignments.                                                                                 |
| `Update Incident`           | Surfaces a Slack modal that allows you to edit your incident's attributes.                                                                                         |
| `All Commands`              | Surfaces the help toolbar.                                                                                                                                         |
| `Leave Feedback`            | Surfaces a Slack modal for incident feedback.                                                                                                                      |
| `Manage Custom Fields`      | Surfaces a Slack modal for managing your custom fields.                                                                                                            |
| `Manage Action Items`       | Surfaces a checklist for managing the incident's action items.                                                                                                     |
| `View Tasks`                | Surfaces a checklist for managing action items assigned to your user.                                                                                              |
| `Add Pagerduty Responders`  | Escalation modal for adding [PagerDuty responders](/integrations/pagerduty). This action requires that the PagerDuty integration is already set up for your team.  |
| `Add Opsgenie Responders`   | Escalation modal for adding [Opsgenie responders](/integrations/opsgenie). This action requires that the Opsgenie integration is already set up for your team.     |
| `Add Victor Ops Responders` | Escalation modal for adding [VictorOps responders](/integrations/victor-ops). This action requires that the VictorOps integration is already set up for your team. |

### Text

This field contains sets content of the message you wish to send. [Incident variables](/liquid/incident-variables), [Liquid syntax](https://shopify.github.io/liquid/ "Liquid syntax"), and [Slack markdown](https://api.slack.com/reference/surfaces/formatting "Slack markdown") are all supported in this field.

### Message Threading Options

If you want to thread the message under an existing block/message that Rootly has sent, you can do so by selecting a parent block/message to be threaded under.

#### Filter Tasks by Workflow

This field is used to filter for the workflow contains the specific action responsible for sending the parent message. The value in this field will not persist once the workflow is saved, as the `Select a Task` field is what ultimately determines the parent message to thread under.

#### Select a Task

This field is used to select the specific action that's responsible for sending the parent message. This field determines which message is the parent message to thread under.

#### Update Parent Message

If this field is selected, the workflow will update the original parent message, instead of thready underneath it.

#### Broadcast Thread Reply to Channel

If this field is selected, the threaded message will also be broadcasted as a new message in the specified channels.

### Send as Ephemeral

If selected, your message will be sent as a **hidden** message visible only to the specified users.

A value must be set for the `Slack Users` or `Slack User Groups` and `Channels` when this field is selected. Additionally, the selected users need to be in the specified channels.

### Pin to Channel

If selected, your message will pinned to the specified channels.


Built with [Mintlify](https://mintlify.com).