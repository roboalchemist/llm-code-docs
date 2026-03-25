# Source: https://docs.axonius.com/docs/crowdstrike-alert.md

# CrowdStrike Alert

Axonius supports a **CrowdStrike Alert** as an event in a Workflow.

Workflows configured with a **CrowdStrike Alert** event are triggered when the Axonius Webhook URL receives an alert from CrowdStrike. Then, actions configured in the Workflow following the **CrowdStrike Alert** event, are triggered conditionally, according to the values in the relevant [fields of the event](#event-structure).

## Configuration Prerequisites

Before adding a **CrowdStrike Alert** event to a Workflow the first time (or after the URL has changed in the System Settings), you must do the following:

* In Axonius: Make sure that the URL of the Axonius CrowdStrike Webhook, and optionally, the secure key, are configured in the [Axonius System Settings](#crowdstrike-webhook-settings-in-axonius) so that Axonius can receive Webhook alerts from CrowdStrike.
* In CrowdStrike: Configure in the [CrowdStrike console](#configuring-an-axonius-custom-webhook-in-crowdstrike) the Axonius CrowdStrike Webhook URL, and optionally the HMAC Secret Key] so that CrowdStrike can send alerts to the Axonius Webhook URL.

The following sections describe how to integrate CrowdStrike with Axonius on both the Axonius and CrowdStrike sides.

### CrowdStrike Webhook Settings in Axonius

CrowdStrike supports setting up a Webhook at the Axonius destination to receive alerts from CrowdStrike.
You can view the configuration of the CrowdStrike Webhook in **System Settings> External Integrations> Workflows Events**, with **CrowdStrike** selected in the **Select Product** dropdown.

The **Workflows Events** dialog includes the following information for **CrowdStrike**:

* The URL of the Axonius Webhook that receives CrowdStrike events, with an adjacent Copy icon. This URL is predefined in the system.
* **Private Secure Key (X-API-Key)** (optional) - This field holds the secure key value entered in **HMAC Secure Key** (see [Configuring an Axonius Custom Webhook in CrowdStrike](#configuring-an-axonius-custom-webhook-in-crowdsrike) below). This secure key is used on the CrowdStrike side to verify that its events are being sent to the Axonius Webhook and on the Axonius side to verify that events arriving at the Axonius Webhook are from CrowdStrike.

### Configuring an Axonius Custom Webhook in CrowdStrike

This section explains how to configure an Axonius Custom Webhook in CrowdStrike. This includes configuring in CrowdStrike, the following:

* The Axonius **Webhook URL**.
* The **HMAC Secret Key** value (optional).

<Callout icon="📘" theme="info">
  Note

  You need to configure the Axonius Custom Webhook URL in CrowdStrike only once, unless the Axonius Webhook URL changes.
</Callout>

**To configure the Axonius Custom Webhook in CrowdStrike**

1. In the Falcon console, go to the **CrowdStrike Store**.
2. Navigate to **Webhook**.
3. Click **Configure**.
4. Click **Add configuration**.
5. In **Name**, type a meaningful name for the Webhook.
6. In **Webhook URL**, paste the [Axonius CrowdStrike Webhook URL](#crowdstrike-webhook-settings-in-axonius) - the URL that the CrowdStrike Webhook will post to.
7. In **HMAC Secret Key**, add a key of at least 32 characters for use in generating an HMAC signature in requests from CrowdStrike to your webhook.
   Enter this key in **Private Secure Key (X-API-Key)** in the [Axonius CrowdStrike Webhook Settings](#crowdstrike-webhook-settings-in-axonius) to use in your webhook to verify requests are from CrowdStrike.

<Callout icon="📘" theme="info">
  Important

  While you must provide a value here, if you don’t want to verify that a request is from CrowdStrike, you can enter any 32 or more characters for the value.
</Callout>

8. Leave the **Signature Header Name** value set to its default value of *X-CS-Primary-Signature*. This value is based on the key specified in the **HMAC Secret Key** field.
9. Click **Save configuration**. CrowdStrike is now set up to send events to the Axonius Webhook.

## CrowdStrike Event Delivery to Axonius

CrowdStrike delivers an event to the Axonius Webhook URL when an alert is triggered in CrowdStrike.

The following describes how a CrowdStrike alert is sent to Axonius:

1. When CrowdStrike generates an alert, an event is triggered.
2. CrowdStrike sends an HTTP POST request to the dedicated Axonius Webhook URL. The HTTP POST request includes the event and if configured (optional), the following three headers:
   * x-cs-primary-signature - This value is based on the key specified in the **HMAC Secret Key** field.
   * x-cs-delivery-timestamp
   * x-cs-signature-algorithm
3. If the secure key is configured in **Axonius System Settings> Workflow Events> CrowdStrike**, the Axonius Webhook computes a signature from the secure key, accesses the request headers, and compares the computed signature to the one in the request. If there is a match, the Axonius Webhook accepts and acknowledges CrowdStrike's HTTP POST request.

### Event Fields

The CrowdStrike custom Webhook delivers events to the Axonius Webhook URL.

Click **Event Fields** to view the event fields of each event payload sent to the URL.

You can follow up on a CrowdStrike event in a workflow with an enforcement action based on these event fields.

<br />