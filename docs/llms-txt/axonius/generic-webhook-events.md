# Source: https://docs.axonius.com/docs/generic-webhook-events.md

# Generic Webhook Events

## Overview

Generic Webhook Events provide a flexible and dynamic way to connect any external service that can send data via a webhook directly to an Axonius Workflow. This connection enables you to trigger custom automations based on events from unique, custom, or unintegrated tools and systems.
While Workflows can use Axonius-provided predefined events, generic webhooks provide a dynamic solution for integrating with custom APIs, third-party tools, or internal systems not already configured in your environment.

### Key Capabilities

Generic Webhooks enable you to:

* Receive data from any external system via a webhook.

* Automatically parse incoming payloads, such as JSON, to facilitate seamless integration.

* Dynamically extract key fields from the payload for use in subsequent Workflow actions.

## Data Structure Support

Generic Webhook Events handle complex data structures, ensuring all necessary information from an external event is available for your Workflow.

* **Data flexibility** - Supports Events as full objects or flat key/value pairs.
* **Nesting** - Easily handles nested objects and arrays (e.g., mapping to a field like event.user.manager.email).
* **Multiple levels** - Supports various levels of nesting.
* **Data Visibility** - The Workflow Data repository stores and allows you to browse/preview nested values within objects and arrays.

## Use Cases

* **HR/Identity Management** - Receive a 'new hire' or 'termination' event that includes nested fields (e.g., user → manager → email). Workflow Action: Map nested fields directly to user and manager fields for provisioning or deprovisioning.
* **Security Alerts (SIEM)** - SIEM sends an alert with nested arrays of IPs, devices, and users. Workflow Action: Pick the correct values (e.g., first IP, all users, or specific device) to initiate a security response.
* **SaaS Management** - Webhooks from services such as Okta or Slack include nested groups. Workflow Action: Check conditions on sub-objects directly without needing a pre-processing step.

## How Generic Webhook Events Work

A Generic Webhook Event acts as a bridge between an external service and your Workflow. The external service sends a request to a dedicated Axonius webhook URL, and if the request is successful, it triggers your Workflow to process the event data.

<Callout icon="📘" theme="info">
  Note

  The Activity Log records all incoming requests, which you can use to troubleshoot any issues with your webhook.
</Callout>

1. **The External Service Sends an Alert:** When an event occurs, the external service builds a JSON payload with the event data and includes a custom header with a secure key (X-API-Key). It sends an HTTP POST request with this information to the unique Axonius Webhook URL (provided for the Generic Webhook Event).

2. **Axonius Verifies Authentication:** The Axonius webhook verifies that the secure **X-API-Key** in the request's custom header matches the one configured in Axonius (in the Generic Webhook Event settings).

3. **Axonius Sends a Response:**
   * **Success** - If the secure key matches, Axonius accepts the POST request and sends back a success code:
     * **200 OK** - A general Success response.
     * **204 No Content** - A Success response with no additional information.
   * **Failure** - If the external service receives a timeout or error from the Axonius webhook, it may retry the request once before receiving a final **HTTP 400 Bad Request** error.

4. **Workflow is Triggered:** Once Axonius successfully receives the webhook request, any Workflows configured with that specific Generic Webhook event are triggered.

## Adding a Generic Webhook Event to a Workflow

You can add an existing Generic Webhook Event to your Workflow, or create a new one and then add it.

**To add an existing Generic Webhook Event to a Workflow:**

1. From the **Trigger Type** (for triggering event) or **Event** (for non-triggering event) panes in the Workflow, select an Event under the **Generic Webhook Event** category.

**To create and add a new Generic Webhook Event to a Workflow**

1. [Create the new Generic Webhook Event](/docs/creating-a-generic-webhook-event).
2. Copy the [**URL** and **Private Secure Key** of the new Generic Webhook event](/docs/generic-webhook-events#generic-webhook-general-settings-in-axonius) into the [Webhook settings of the relevant external service](/docs/generic-webhook-events#configuring-the-external-service).
3. From the **Trigger Type** (for triggering event) or **Event** (for non-triggering event) panes in the Workflow, under the **Generic Webhook Event** category, select the newly created Event.

### Generic Webhook General Settings in Axonius

These settings define the endpoint on the Axonius platform that receives data from your external service.

You can view the configuration of a Generic Webhook Event:

* In **System Settings> External Integrations> Workflows Events**, with **Generic Webhook** selected in the **Select Product** dropdown.
* In the **Trigger** or **Event** pane of the Workflow, click **View Configuration** for the selected Generic Event.

The **Generic Webhook Event** general settings include:

* The URL of the Axonius Webhook that receives Generic Webhook alerts, with an adjacent Copy icon.
* **Private Secure Key (X-API-Key)** (optional) - This field holds the secure key used on the Generic Webhook side to confirm that its alerts are being sent to the Axonius webhook and on the Axonius side to verify that alerts arriving at the Axonius webhook are from the Generic Webhook.

The system generates this URL and private secure key when you create the Generic Webhook Event.

You can update the Private Secure Key. After you update the key, save the configuration.
You cannot update the URL.

### Configuring the External Service

This step links the external system to the Axonius Webhook URL and is only necessary for a newly created event or whenever the URL or secure key changes.

**To configure the Generic Webhook in the external service:**

1. Log in to the console of the external service and navigate to its webhook settings.

2. In Axonius, open the event's configuration in either of the following ways:

   * Select the Product from **System Settings> External Integrations> Workflows Events`>`Generic Webhook Events**.
   * From the **Trigger Type** (for triggering event) or **Event** (for non-triggering event) panes in the Workflow, select the event under the Generic Webhook Event category and click **View Configuration**.

3. Copy the webhook URL (click the Copy icon) and  **Private Secure Key (X-API-Key)** from the Configuration screen into the corresponding fields in the external service's webhook settings.

4. Save the configuration in the external service.

Once configured, the Generic Webhook external service sends alerts to the Axonius webhook URL, and Axonius is ready to receive and process them.

## Viewing the Event Fields

You can view the event fields that the Generic Webhook Event sends to the Axonius Webhook URL. Knowing this structure helps build robust Workflow logic, which includes filtering, sending notifications, and updating other systems.

**To view the Event fields:**

1. In your Workflow, in the **Trigger Type** or **Event** configuration panes, select a Generic Webhook Event.
2. Click **Event Fields**. A list of the field names and data types (for example: `id: string`, `timestamp: date`, `alert_name: string`) opens.