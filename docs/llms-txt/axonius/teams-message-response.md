# Source: https://docs.axonius.com/docs/teams-message-response.md

# Teams Message Response

Axonius supports **Teams Message Response** as an event in a Workflow.

Whenever a user responds to a Teams message, a Webhook event is automatically sent to the Axonius URL dedicated for Teams. Then, any Workflows configured with the **Teams Message Response** event are triggered (if a triggering event) or continue (if a non-triggering event).

You can configure a Workflow with a **Teams Message Response** event, provided that you have configured any of the following Enforcement Actions as interactive with a list of predefined Responses:

* [**Microsoft Teams - Send Message**](/docs/send-microsoft-teams-message)
* [**Microsoft Teams - Send Direct Message to Assets**](/docs/teams-send-dm-to-assets)
* [**Microsoft Teams - Send Direct Message to a User**](/docs/teams-send-dm-to-user)
* [**Microsoft Teams - Send Direct Message to a Channel**](/docs/teams-send-dm-to-channel)

## Setting Up Axonius to Receive Webhook Events from Teams

Axonius supports setting up a Webhook URL at the Axonius destination to receive webhook events from Teams.

The Teams event settings, specifically the Webhook URL, are configured in **System Settings> External Integrations> Workflow Events**, with **Microsoft Teams** selected in the **Select Product** dropdown.

The **Workflows Events** dialog includes the following information for **Microsoft Teams**:

* The URL of the Axonius Webhook that receives Microsoft Teams webhook events, with an adjacent Copy icon. This URL is predefined in the system.

## Integrating Teams Message Response with Axonius

When a response is sent to a message sent using an interactive Microsoft Teams - send message enforcement action, a Teams Message Response event is automatically sent to the URL configured in Axonius System Settings. Therefore, there is no need to configure the Axonius webhook URL for **Microsoft Teams** into the Microsoft Teams application.

## Adding the Teams Message Response Event to the Workflow

You can add **Teams Message Response** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

When this event is not the triggering event, this event must be preceded in the workflow by an interactive Microsoft Teams Send Message enforcement action, which is configured with a list of predefined responses (in the **Create list of predefined responses** field).

When a user clicks a Response button in an interactive Microsoft Teams message sent with a Microsoft Teams - send Message enforcement action, the Axonius incoming webhook URL configured for Microsoft Teams in the System Settings is automatically sent to the **Microsoft Teams - Send Message** enforcement action, which in turn sends a Response event to that URL.

**To select the Teams Message Response event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Message Response**, click the **Teams Message Response** tile.

<Image alt="TeamsMessageResponseWebhookConfDetails.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TeamsMessageResponseWebhookConfDetails.png" />

2. In the dropdown, select the type of asset to be retrieved. The next workflow nodes will run on the selected asset type.
3. Click **View configuration** and in the **Webhook Configuration Details** screen that opens, check that a URL is configured for Teams.

The Workflow is triggered each time a user sends a response to a Teams message. The next node runs on the retrieved asset.

<Image alt="WFTriggerTeamsResponse.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WFTriggerTeamsResponse.png" />

**To select Teams Message Response as a non-triggering event**

1. In the **Event** pane, under **Message Response**, click the **Teams Message Response** tile.

<Image alt="TeamsMessageResponseNonTrigger.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TeamsMessageResponseNonTrigger.png" />

<Callout icon="📘" theme="info">
  Note

  This event must be preceded by an interactive Send Teams message event.
</Callout>

In this case, when a response is received to a Send Teams message in a previous node of the workflow, an event occurs and the Workflow continues running.

<Image alt="WFTeamsNonTriggerResponseEvent.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WFTeamsNonTriggerResponseEvent.png" />

## Viewing the Event Fields

After you select the event, you can view the fields of the Events that the Teams webhook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on the **Teams Message Response** event in a Workflow, for example, in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Teams Message Response** event (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

<Image alt="TeamsEventFields.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TeamsEventFields.png" />

The following describes these Event fields:

* **Response** - The response returned by the user.
* **Event date** - Date the event occurred.
* **Event timestamp** - Timestamp when the response was delivered to Axonius.

## Teams Event Delivery to Axonius

When a Teams Message Response event occurs, the following describes how Microsoft Teams sends the event to Axonius:

1. The Microsoft Teams webhook is automatically triggered and then sends an HTTPS POST request to the dedicated Axonius Webhook URL.
   4.The Axonius webhook accepts and acknowledges Okta's POST request with either a 200 (Success) or 204 (Success no content) return code.
   * If there is a timeout or an error response from Axonius during the attempts, one request retry is sent. If a successful response isn't received after that, an HTTP 400 error is returned with more information about the failure.