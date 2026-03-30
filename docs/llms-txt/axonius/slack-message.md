# Source: https://docs.axonius.com/docs/slack-message.md

# Slack Message

Axonius supports **Slack Message** as an event in a Workflow.

You can configure a Workflow with a **Slack Message** event, provided that you have configured any of the following Enforcement Actions:

* <Anchor label="**Slack - Send Direct Message to Assets**" target="_blank" href="/docs/slack-send-dm-to-assets">**Slack - Send Direct Message to Assets**</Anchor>

* <Anchor label="**Slack - Send Message to Channel**" target="_blank" href="/docs/en/slack-send-message-to-channel?highlight=slack">**Slack - Send Message to Channel**</Anchor>

Before Slack can begin sending **Slack Message** events to Axonius (or after the URL or Private Secure Key has changed), <Anchor label="integrate Slack with Axonius on both the Axonius and Slack sides" target="_blank" href="integrating-slack-with-axonius-for-workflows">integrate Slack with Axonius on both the Axonius and Slack sides</Anchor> .

## Adding the Slack Message Event to the Workflow

You can add **Slack Message** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Slack Message event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Message Received**, click the **Slack Message** tile. This event retrieves **Users** who sent the Slack message.

<Image alt="SlackMessageTriggerEvent.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SlackMessageTriggerEvent.png" />

2. Click **View configuration** and in the **Webhook Configuration Details** screen that opens, check that a URL and Signing Secret are configured for Slack.

3. If you generated a new **Signing Secret** in Slack, enter it, and then click **Enable Webhook**.

The Workflow is triggered each time a user sends a Slack message. The next node runs on the retrieved user.

**To select Slack Message as a non-triggering event**

1. In the **Event** pane, under **Message Received**, click the **Slack Message** tile.

   <Image alt="SlackMessageNonTriggerEvent.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SlackMessageNonTriggerEvent.png" />

In this case, when a Slack Message is sent on a device retrieved from the previous node (in the above example, an added device), an event occurs and the Workflow continues running and checks the Team ID event field equals 3.

## Viewing the Event Fields

After you select the event, you can view the fields of the Events that the Slack webhook delivers to the Axonius Webhook URL. You can then use these fields to follow up on **Slack Message** events in a Workflow; for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Slack Message** event (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

<Image alt="SlackEventFields.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SlackEventFields.png" />

The following describes these Event fields:

* **Team ID** - The unique identifier for the Slack workspace (or "team") where the message event occurred.
* **Api App ID** - The unique identifier for the Slack App that generated or received the event.
* **User ID** - The unique identifier for the Slack user who sent or was directly involved with the message event. For a standard message, this is the ID of the sender.
* **Text** - The content of the Slack message that triggered the event.
* **Channel ID** - The unique identifier for the Slack channel where the message was sent.
* **Authed Teams** - The Team ID of the workspace where the event occurred.
* **Event ID** - A unique identifier for the specific event that Slack is sending.
* **Event TimeStamp** - Indicates when the event was received and processed by Axonius. This is distinct from when the event occurred in Slack.
* **Channel Type** - Indicates the type of channel where the message originated. For example, public channel, direct message
* **Event date** - The date when the message event occurred in Slack. It's likely a human-readable format derived from an internal timestamp.
* **Event timestamp** - The Unix timestamp (number of seconds since January 1, 1970, 00:00:00 UTC) when the message event originally occurred in Slack.