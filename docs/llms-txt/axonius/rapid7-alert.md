# Source: https://docs.axonius.com/docs/rapid7-alert.md

# Rapid7 Alert

Axonius supports a **Rapid7 Alert** as an event in a Workflow.

Workflows configured with a **Rapid7 Alert** event are triggered when the Axonius Webhook URL receives an alert from Rapid7. Then, actions configured in the Workflow following the **Rapid7 Alert** event, are triggered conditionally, according to the values in the relevant [fields of the event](#event-structure).

## Configuration Prerequisites

Before adding a **Rapid7 Alert** event to a Workflow the first time (or after the URL has changed in the System Settings), you must do the following:

* In Axonius: Make sure that the URL of the Axonius Rapid7 Webhook, and optionally, the secure key, are configured in the [Axonius System Settings](#rapid7-webhook-settings-in-axonius) so that Axonius can receive Webhook alerts from Rapid7.
* In Rapid7: Configure in the [Rapid7 console](#configuring-an-axonius-custom-webhook-in-rapid7) the Axonius Rapid7 Webhook URL, and optionally the HMAC Secret Key so that Rapid7 can send alerts to the Axonius Webhook URL.

The following sections describe how to integrate Rapid7 with Axonius on both the Axonius and Rapid7 sides.

### Rapid7 Webhook Settings in Axonius

Rapid7 supports setting up a Webhook at the Axonius destination to receive alerts from Rapid7.
You can view the configuration of the Rapid7 Webhook in **System Settings> External Integrations> Workflows Events**, with **Rapid7** selected in the **Select Product** dropdown.

The **Workflows Events** dialog includes the following information for **Rapid7**:

* The URL of the Axonius Webhook that receives Rapid7 events, with an adjacent Copy icon. This URL is predefined in the system.
* **Private Secure Key (X-API-Key)** (optional) - This field holds the secure key value entered in the Rapid7 **Password** field. This secure key is used on the Rapid7 side to verify that its events are being sent to the Axonius Webhook and on the Axonius side to verify that events arriving at the Axonius Webhook are from Rapid7.

### Configuring an Axonius Custom Webhook in Rapid7

This section explains how to configure an Axonius Custom Webhook in Rapid7. This includes configuring in Rapid7, the following:

* The Axonius **Webhook URL**.
* The **Password** value (optional but recommended for security reasons).

<Callout icon="📘" theme="info">
  Note

  You need to configure the Axonius Custom Webhook URL in Rapid7 only once, unless the Axonius Webhook URL changes.
</Callout>

**To configure the Axonius Custom Webhook in Rapid7**

1. In the **Rapid7** console, in **Settings> Notifications**, under **Notifications> Webhook Notifications** select **Create and Manage Webhook Integrations**.
2. Click **Webhook Targets> Create Webhook Target**.
3. Select the radio button for **Universal webhook**.
4. In **Name**, type a meaningful name for the Webhook.
5. In **Target URL**, paste the [Axonius Rapid7 Webhook URL](#rapid7-webhook-settings-in-axonius) - the URL that the Rapid7 Webhook will post to.
6. In **HMAC Secret Key**, add a key of at least 32 characters for use in generating an HMAC signature in requests from Rapid7 to your webhook.
   Enter this key in **Private Secure Key (X-API-Key)** in the [Axonius Rapid7 Webhook Settings](#rapid7-webhook-settings-in-axonius) to use in your webhook to verify requests are from Rapid7.

<Callout icon="📘" theme="info">
  Important

  While you must provide a value here, if you don’t want to verify that a request is from Rapid7, you can enter any 32 or more characters for the value.
</Callout>

9. Click **Create Webhook Target**. Rapid7 is now set up to send events to the Axonius Webhook.

## Rapid7 Event Delivery to Axonius

Rapid7 delivers an event to the Axonius Webhook URL when an alert is triggered in Rapid7.

The following describes how a Rapid7 alert is sent to Axonius:

1. When Rapid7 generates an alert, an event is triggered.
2. Rapid7 sends an HTTP POST request and header to the dedicated Axonius Webhook URL. The HTTP POST request includes the event (a JSON-encoded parameter payload ) and if configured (optional), the following two headers:
   * The payload contains information about the triggered alert, host, and log where the alert has been triggered, together with the triggering event and event context.
   * The header contains a **Signature**, which is the HMAC hash (based on the **Password** shared secret code) encoded in Base64.
3. If the secure key is configured in **Axonius System Settings> Workflow Events> Rapid7**, the Axonius Webhook computes a signature from the secure key, accesses the request headers, and compares the computed signature to the one in the request. If there is a match, the Axonius Webhook accepts and acknowledges Rapid7's HTTP POST request.

### Event Fields

The Rapid7 custom Webhook delivers events to the Axonius Webhook URL.

You can view the event fields of each event notification payload sent to the URL by expanding the Event Fields in the Rapid7 Alert Event pane.

You can follow up on a Rapid7 event in a Workflow with an Enforcement Action based on these Event fields.