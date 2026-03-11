# Source: https://docs.axonius.com/docs/slack-message-response.md

# Slack Message Response

Axonius supports **Slack Message Response** as an event in a Workflow.

You can configure a Workflow with a **Slack Message Response** event, provided that you have configured any of the following Enforcement Actions as interactive with a list of predefined Responses (in the **Create list of predefined responses** field):

* [**Slack - Send Direct Message to Assets**](/docs/slack-send-dm-to-assets)

* [**Slack - Send Message to Channel**](/docs/slack-send-message-to-channel?highlight=slack)

Before Slack can begin sending **Slack Message Response** events to Axonius (or after the URL or Private Secure Key has changed), integrate Slack with Axonius on both the Axonius and Slack sides.

## Adding the Slack Message Response Event to the Workflow

You can add **Slack Message Response** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

When this event is not the triggering event, this event must be preceded in the workflow by an interactive Slack Send Message enforcement action, which is configured with a list of predefined responses (in the **Create list of predefined responses** field).

When a user clicks a Response button in an interactive Slack message sent with a Slack Send Message enforcement action, the Axonius incoming webhook URL configured for Slack in the System Settings is automatically sent to the **Slack - Send Message** enforcement action, which in turn sends a Response event to that URL.

**To select the Slack Message Response event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Message Response**, click the **Slack Message Response** tile.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SlackMessageResponseTriggerEvent.png)

2. In the dropdown, select the type of asset to be retrieved. The next workflow nodes will run on the selected asset type.

3. Click **View configuration** and in the **Webhook Configuration Details** screen that opens, check that a URL and Signing Secret are configured for Slack.

4. If you generated a new **Signing Secret** in Slack, enter it, and then click **Enable Webhook**.

The Workflow is triggered each time a user sends a response to a Slack message. The next node runs on the retrieved asset (in this case, a device).

<Image alt="WFMessageResponse.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WFMessageResponse.png" />

**To select Slack Message Response as a non-triggering event**

1. In the **Event** pane, under **Message Response**, click the **Slack Message Response** tile.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WFSlackNonTriggerResponseEvent.png)

<Callout icon="📘" theme="info">
  Note

  This event must be preceded by an interactive Send Slack message enforcement action.
</Callout>

In this case, when a response is received to a Send Slack message in a previous node of the workflow, an event occurs and the Workflow continues running.

## Viewing the Event Fields

After you select the event, you can view the fields of the Events that the Slack webhook delivers to the Axonius Webhook URL. You can then use these fields to follow up on the **Slack Message Response** event in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Slack Message Response** event (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

<Image alt="SlackMessageResponseEventFields.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SlackMessageResponseEventFields.png" />

The following describes these Event fields:

* **Event Timestamp** - The Unix timestamp (number of seconds since January 1, 1970, 00:00:00 UTC) representing when the response event originally occurred in Slack (i.e., when the user clicked the button or made a selection).
* **Workspace ID** - The unique identifier for the Slack workspace (or "team") where the user performed the interaction and sent the response.
* **User ID** - The unique identifier for the Slack user who interacted with the message component (e.g., clicked the button) and thus "sent the response."
* **Response** - Contains the actual data or value associated with the user's interaction. Its content depends on the type of interactive component (button, select menu, etc.).
* **Event date** - The date when the Slack message response event occurred. It's likely a human-readable format derived from an internal timestamp, representing the date the user interacted with the message.
* **Event timestamp** - The Unix timestamp indicating when Axonius successfully received and processed the response notification from Slack. This timestamp reflects Axonius's internal receipt time, which may differ slightly from when the user actually sent the response due to network latency.