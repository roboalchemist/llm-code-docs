# Source: https://docs.axonius.com/docs/panther-siem-alert.md

# Panther SIEM Alert

You can configure a Workflow with a Panther SIEM Alert event.

## Configuration Prerequisites

Before adding a Panther event to a Workflow the first time (or after the URL has changed in the System Settings), you must do the following:

* In Axonius:[Make sure that the URL of the Axonius Panther Webhook, and optionally, the secure key, are configured in the Axonius System Settings](#panther-webhook-settings-in-axonius) so that Axonius can receive webhook events from Panther.
* In Panther:[Configure the Axonius Panther Webhook URL, and optionally the Custom HTTP header, in Panther](#configuring-an-axonius-custom-webhook-in-panther) so that the Panther app can send webhook events to the Axonius webhook URL.

The following sections describe how to integrate Panther with Axonius on both the Axonius and Panther sides.

## Panther Webhook Settings in Axonius

Panther supports setting up a Webhook at the Axonius destination to receive alerts from Panther.
You can view the configuration of the Panther Webhook in **System Settings> External Integrations> Workflows Events**, with **Panther** selected in the **Select Product** dropdown.

The **Workflows Events** dialog includes the following information for **Panther**:

* The URL of the Axonius Webhook that receives Panther alerts, with an adjacent Copy icon. This URL is predefined in the system.
* **Private Secure Key (X-API-Key)** (optional) - This field holds the secure key value from **Header Value** that is generated in Panther when  the **Add custom HTTP Headers?** option (see [Configuring an Axonius Custom Webhook in Panther](#configuring-an-axonius-custom-webhook-in-panther) below) is enabled. This secure key is used on the Panther side to verify that its alerts are being sent to the Axonius webhook and on the Axonius side to verify that alerts arriving at the Axonius webhook are from Panther.

## Configuring an Axonius Custom Webhook in Panther

This section explains how to configure an Axonius Custom Webhook in Panther. This includes doing in the Panther console the following:

* Entering the Axonius webhook URL.
* Generating the **Private Secure Key (X-API-Key)** (optional).

<Callout icon="📘" theme="info">
  Note

  You need to configure the Axonius Custom Webhook URL in Panther only once, unless the Axonius webhook URL changes.
</Callout>

**To configure the Axonius Custom Webhook in Panther**

1. Log in to the Panther Console.
2. On the left sidebar, click **Configure `>` Alert Destinations**.
3. Click **+Add your first Destination**.
4. Click **Custom Webhook**. A form opens with required and optional fields to fill in to configure the Webhook destination (Axonius Webhook URL).
5. In **Display Name**, add a meaningful name to identify your destination.
6. In **Custom Webhook URL**, paste the [Axonius Panther Webhook URL](#panther-webhook-settings-in-axonius) into this field.
7. Toggle on **Add custom HTTP Headers?**. The **Header Name** and **Header Value** fields open.
8. In **Header Name**, type **X-API-Key**. This is the name of the custom HTTP header that needs to be included with the POST request that sends the alerts. A value is generated for the header, and appears in the **Header Value** field.
9. Copy the **Header Value** value (from the Panther form; previous step) into **Private Secure Key (X-API-Key)** in the Axonius Panther Webhook configuration screen (see above).
10. Click **Add Destination**. The Axonius webhook URL is added as a destination of Panther alerts.
11. On the final page, optionally click **Send Test Alert** to test the integration using a test payload.
12. When you are finished, click **Finish Setup**. Panther is now set up to send alerts to the Axonius webhook.
13. [Update the alert\_context function](#configurable-alert-information-fields).

For full instructions and Panther configuration screens, including optional settings, see [Custom Webhook Destination](https://docs.panther.com/alerts/destinations/custom_webhook).
Learn more on [the alert\_context section](https://docs.panther.com/detections/rules/python#alert_context).

## Panther Event Delivery to Axonius

Panther delivers an event to the Axonius Webhook URL when an alert is triggered in Panther.

The following describes how Panther sends an event to Axonius:

1. When Panther SIEM generates an alert, it sends an HTTP POST request to the dedicated Axonius webhook URL.
2. The POST request includes the alert and if configured (optional), a custom HTTP header named X-API-Key.
3. If the secure key is configured, the Axonius webhook verifies that the value of secure key X-API-Key in the header matches the one configured in **Axonius System Settings> Workflow Events> Panther**,  and if yes, accepts and acknowledges Panther's POST request with an HTTP status code in the 2XX range.
   * If during the attempts, there are network failures or entry of non 2XX codes, Panther retries the request up to ten times before permanent failure.

The alert includes static fields, as well as additional fields, provided they have been added to the alert configuration.

Workflows configured with a **Panther SIEM Alert** event are triggered when the Axonius Webhook URL receives an alert from Panther. Then, actions configured in the Workflow following the **Panther SIEM Alert** event, are triggered conditionally, according to the values in the relevant [fields of the event](#event-structure).

### Event Fields

The Custom Webhook delivers alerts, which are composed of the following:

* [Static information fields](#static-alert-information-fields).
* [Configurable information fields](#configurable-alert-information-fields).

#### Static Alert Information Fields

The following are the static information fields of type String that are included in each alert sent to the Axonius Webhook URL:

* **ID** - Identifier of the alert's detection
* **Date Created** - Alert creation time as  a valid ISO-8601 DateTime string in the format YYYY-MM-DDThh:mm:ss.sssZ (sssZ is a nanosecond field; optional)
* **Severity** - Level of urgency of the alert
* **Type** - Type of the alert
* **Link** - Link to the alert in the Panther Console
* **Title** - Generated title of the alert
* **Name** - Name of the alert's detection
* **AlertId** - Identifier of the alert in Panther Backend
* **Description** - Description explaining why the rule exists
* **Runbook** - A list of instructions to follow once the alert is generated
* **Version** - Version identifier for the alert's detection

You can use these Event Fields to follow up on a Panther Siem Alert event in a Workflow with an Enforcement Action.

#### Configurable Alert Information Fields

It is possible to customize the structure of the alert with fields (in addition to the static fields) according to your organization's needs. The **alertContext** section contains event details to pass to the alert destination (Axonius webhook) as additional context, such as usernames and IP addresses. These user-configurable alert fields can be crucial in a workflow to follow up on an alert with an enforcement action.

<Callout icon="📘" theme="info">
  Note

  * It is recommended to configure the alert\_context function to return mail, username, hostname, ip, and cloud\_id, so that the keys can be extracted.
  * It is also possible to configure a list of tags (**tags**) associated with the alert.
</Callout>

The following is a sample of the content of an alert for when an administrator has logged into Okta from a new IP address:

```
{
  "id": "Custom.Okta.AdminLogin",
  "createdAt": "2023-10-09T18:21:53Z",
  "severity": "HIGH",
  "type": "RULE",
  "link": "https://axonius.runpanther.net/alerts-and-errors/15d8bd0671c9d9591a3f2f08afe5d2c0?source=webhook",
  "title": "[Okta] test@example.com logged in as an Administrator into Okta from a new IP",
  "name": "An Administrator Logged Into Okta from a new IP",
  "alertId": "15d8bd0671c9d9591a3f2f08afe5d2c0",
  "alertContext":
  {
    "login_time": "2023-10-09 18:16:01.478000000",
    "actor_email": "test@example.com",
    "ip": "1.2.3.4"
  },
  "description": "An Administrator Logged Into Okta from a new IP.",
  "runbook": "Verify the login activity for this user (from a new IP) is legitimate by reaching out to the user.",
  "tags":
  [
    "Custom",
    "Okta",
    "Resource Development:Compromise Accounts"
  ],
  "version": "6eAuG0RaMQPDgtEoyIrXm36kcxbwCNr."
}
```