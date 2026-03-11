# Source: https://docs.axonius.com/docs/dynatrace-alert.md

# Dynatrace Alert

Axonius supports a **Dynatrace Alert** as an event in a workflow.

Use a Dynatrace Alert to trigger a workflow in Axonius. When Axonius receives a problem notification from Dynatrace, the notification payload data is parsed and used in subsequent workflow nodes.

## Configuration Prerequisites

Before adding a **Dynatrace Alert** event to a workflow for the first time (or after the URL has changed in the System Settings), you must do the following:

* **In Axonius:** Configure an Dynatrace webhook in [Axonius System Settings](#crowdstrike-webhook-settings-in-axonius) so that Dynatrace can send notifications to Axonius via this webhook.
* **In Dynatrace:** Configure Dynatrace to send notifications to the Axonius Dynatrace webhook.

### Configuring the Dynatrace Adapter Webhook in Axonius

Before using a Dynatrace webhook for the first time, you must configure the Dynatrace adapter in Axonius to allow webhooks and create a webhook URL and key.

**To configure the Dynatrace webhook in Axonius:**

1. In Axonius, navigate to the Dynatrace adapter: **System Settings> External Integrations> Workflows Events**.
2. From the **Select Product** dropdown, select **Dynatrace**.
3. From the **Workflows Events** page, click the Copy icon to copy the URL of the webhook This URL is predefined in the system. You will paste this URL into Dynatrace so it knows where to send notifications.

### Configuring Dynatrace to Send Notifications to the Axonius Webhook URL

This section explains how to configure Dynatrace to send notifications to the Axonius webhook URL.

<Callout icon="📘" theme="info">
  Note

  You need to configure the Axonius Custom Webhook URL in Dynatrace only once, unless the Axonius Webhook URL changes.
</Callout>

**To configure notifications in Dynatrace:**

<Callout icon="📘" theme="info">
  Note

  There are optional parameters in Dynatrace that are not described here.
</Callout>

1. In Dynatrace, go to **Settings Classic** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Custom integration**.
4. In **Display name**, enter a name for this integration that will be displayed in Dynatrace on Settings> Classic > Integration > Problem notifications.
5. In **Webhook URL**, paste the [Axonius Dynatrace webhook URL](<#configuring-the -dynatrace-adapter-webhook-in-axonius>) configured above.
6. In Custom payload, enter a custom payload definition.
7. Select **Send test notification** to verify that your webhook integration is functioning correctly.
8. Click **Save**.
9. Use this webhook in workflows.

## Dynatrace Event Delivery to Axonius

When Dynatrace delivers an event to the Axonius webhook URL, Dynatrace sends an HTTP POST request to the dedicated Axonius webhook URL. The HTTP POST request includes the notification payload.

### Event Fields

Click **Event Fields** to view the event fields of each event payload sent to the URL.

You can follow up on a Dynatrace event in a workflow with an enforcement action based on these event fields.

<br />

<br />

<br />