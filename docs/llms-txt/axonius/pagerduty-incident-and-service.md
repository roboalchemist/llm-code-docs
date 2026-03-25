# Source: https://docs.axonius.com/docs/pagerduty-incident-and-service.md

# PagerDuty Incident and Service

Axonius supports **PagerDuty Incident and Service** as an event in a Workflow.

When significant events happen in the PagerDuty account, for example, an incident triggers, escalates, or resolves, an event occurs.

Workflows configured with a **PagerDuty Incident and Service** event are triggered when the Axonius Webhook URL receives an event from PagerDuty. Then, actions configured in the Workflow following the **PagerDuty Incident and Service** event, are triggered conditionally, according to the values in the relevant [fields of the event](#event-structure).

## Configuration Prerequisites

Before adding a PagerDuty event to a Workflow the first time (or after the URL has changed in **System Settings**), do the following:

* In Axonius:[Make sure that the URL of the Axonius PagerDuty Webhook, and optionally, the secure key, are configured in the Axonius System Settings](#pagerduty-webhook-settings-in-axonius) so that Axonius can receive Webhook events from PagerDuty.
* In PagerDuty:[Configure the Axonius PagerDuty Webhook URL and optionally the Custom Header](#configuring-an-axonius-custom-webhook-in-pagerduty) so that the PagerDuty app can send Webhook events to the Axonius Webhook URL.

The following sections describe how to integrate PagerDuty with Axonius on both the Axonius and PagerDuty sides.

### PagerDuty Webhook Settings in Axonius

PagerDuty supports setting up a Webhook at the Axonius destination to receive alerts from PagerDuty.
You can view the configuration of the PagerDuty Webhook in **System Settings> External Integrations> Workflows Events**, with **PagerDuty** selected in the **Select Product** dropdown.

The **Workflows Events** dialog includes the following information for **PagerDuty**:

* The URL of the Axonius Webhook that receives PagerDuty alerts, with an adjacent Copy icon. This URL is predefined in the system.
* **Private Secure Key** (optional) - This field holds the secure key **Value** entered in **Custom Header** in the PagerDuty Webhook subscription configuration (see [Configuring an Axonius Custom Webhook in PagerDuty](#configuring-an-axonius-custom-webhook-in-pagerduty) for **x-custom-header**. This secure key is used on the PagerDuty side to verify that its alerts are being sent to the Axonius webhook and on the Axonius side to verify that alerts arriving at the Axonius Webhook came from PagerDuty (and not a third-party or malicious system).

### Configuring an Axonius Custom Webhook in PagerDuty

This section explains how to configure an Axonius Custom Webhook in PagerDuty. This includes doing in the PagerDuty console the following:

* Entering the Axonius webhook URL.
* Generating the **Private Secure Key** (optional).

<Callout icon="📘" theme="info">
  Note

  You are required to configure the Axonius Custom Webhook URL in PagerDuty only once, unless the Axonius webhook URL changes.
</Callout>

**To configure the Axonius Custom Webhook in PagerDuty**

1. Navigate to **Integrations>  Generic Webhooks (v3)**.

2. Click **New Webhook** and then perform the following:

   1. In **Webhook URL**, paste the [Axonius PagerDuty Webhook URL](#pagerduty-webhook-settings-in-axonius) into this field.
   2. Enter a **Description** (optional).
   3. From the **Event Subscription** dropdown, select the event types that you would like to subscribe to.
   4. Create a **Custom Header** by entering **x-custom-header** in the **Name** and a **Value** for it (optional).
   5. Click **Add Webhook**. A confirmation dialog appears notifying you that the Webhook has been created, and it will supply a secret if you would like to verify Webhook payloads.

3. When you are finished, click **Finish Setup**. PagerDuty is now set up to send alerts to the Axonius webhook.

4. [Update the alert\_context function](#configurable-alert-information-fields).

For full instructions and PagerDuty configuration screens, including optional settings, see [Custom Webhook Destination](https://docs.pagerduty.com/alerts/destinations/custom_webhook).
Learn more on [the alert\_context section](https://docs.pagerduty.com/detections/rules/python#alert_context).

## PagerDuty Event Delivery to Axonius

PagerDuty delivers an event to the Axonius Webhook URL when an alert is triggered in PagerDuty.

The following describes how PagerDuty sends an event to Axonius:

1. When an event happens in PagerDuty, PagerDuty sends an HTTP POST request to the dedicated Axonius Webhook URL.
2. The POST request includes the event (see the [event structure](#event-structure) below) and if configured (optional), **Custom Header** configured with **Private Secure Key** as **x-custom-header** and its **Value**.
3. If the secure key is configured, the Axonius Webhook verifies that the **Value** in **Custom Header** matches the value of **x-custom-header** configured in **Axonius System Settings> Workflow Events> PagerDuty**,  and if yes, accepts and acknowledges PagerDuty's POST request with an HTTP status code in the 2XX range.
   * If during the attempts, there are network failures or entry of non 2XX codes, PagerDuty retries the request up to ten times before permanent failure.

### Event Structure

The PagerDuty custom Webhook delivers events to the Axonius Webhook URL.
Here is an example of the event’s payload sent to the URL:

```
{
  "event": {
    "id": "01CH754SM17TWPE2V2H4VPBRO7",
    "event_type": "pagey.ping",
    "resource_type": "pagey",
    "occurred_at": "2021-12-08T22:58:53.510Z",
    "agent": null,
    "client": null,
    "data": {
      "message": "Hello from your friend Pagey!",
      "type": "ping"
    }
  }
}
```

Each event includes the following information fields of type String:

* **ID** - Identifier of the event
* **Event Type** - Type of the event
* **Resource Type** - Resource type
* **Occurred At** - Date that the event occurred.

You can follow up on a PagerDuty event in a Workflow with an Enforcement Action based on these Event fields.