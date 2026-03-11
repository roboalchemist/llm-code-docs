# Source: https://docs.axonius.com/docs/configuring-workflows-events-settings.md

# Viewing and Configuring Workflow Events Settings

## Overview

Axonius workflows can be triggered or continued by events from external third-party systems. This includes both events predefined in Axonius and generic webhook events that you create for your organization.
Before you can use these events in your workflows, Axonius must be configured to receive webhook events from the vendors of the webhook events.

The **Settings> External Integrations> Workflows Events** page provides the necessary configuration for Axonius to receive Webhook Events from each third-party product. The exact method for configuring webhooks varies by product.

<Callout icon="📘" theme="info">
  Note

  You can also configure webhook settings directly from the workflow **Trigger Type** (for triggering events) or **Event** (for non-triggering events) panes. Learn [how to configure webhooks from the workflow event](/docs/configuring-a-workflow-event).
</Callout>

## Configuring the Product Webhook Settings

The configuration method depends on the third-party product you select:

* [**Webhook URL and Signing Secret**](#using-the-webhook-url-and-signing-secret) - Provide Axonius's webhook URL, which is dedicated to that product, and a signing secret for security verification. Not all products require a signing secret.

* [**Adapter Event Enablement**](#enabling-events-in-the-product-adapter) - Enable event collection directly within their Axonius adapter.

**To configure a product's Webhook settings**

1. From any page, in the top right corner, click the **Settings** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.

2. In the System Settings navigation pane, expand **External Integrations** and select **Workflows Events**.

3. On the **Workflows Events** page, select the product (vendor) you want to configure from the **Select Product** dropdown, under  **Predefined Events** or **Generic Webhook Vendor**.

   <Image alt="ProductDropdown" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProductDropdown.png" />

4. Follow the instructions for the required configuration method.

### Using the Webhook URL and Signing Secret

Some third-party products require you to configure the Axonius dedicated Webhook URL and signing secret (if specified) to receive events.

**To view or configure a product's Webhook settings**

1. **Copy URL:** The displayed Axonius URL is read-only and is the destination for incoming webhook events. Click the Copy icon to copy this URL and paste it into the vendor's configuration.
   * Exception: The Microsoft Teams webhook URL does not need to be manually pasted into its configuration. When a user clicks a response button in a message sent with the [**Microsoft Teams - Send Message**](/docs/send-microsoft-teams-message) interactive enforcement action, this URL is automatically sent to the enforcement action. The Response event is then sent to this URL. Learn more about the [Teams Message Response configuration](/docs/teams-message-response).

2. **Manage Signing Secret:** Enter or update the **Signing Secret** or **Private Secure Key** (if it appears for the selected product). When you enter the value, the **Save** button becomes enabled. Click **Save** to save it. Axonius exchanges this secret with the third-party vendor to verify the authenticity of webhook events. This secret is vital for security; make sure to save this value for future reference.

For example, the Slack Webhook settings display both the Webhook URL and the **Signing Secret** (refer to the screenshot below for an example; the URL is hidden).

<Image alt="SettingsWorkflowEventsURL.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SettingsWorkflowEventsURL.png" />

### Enabling Events in the Product Adapter

Some products require you to enable event collection directly within their Axonius adapter (disabled by default) before sending webhook events to Axonius.

**To enable events in a product's adapter**

1. In the **Workflows Events** screen, select the **Enable events in adapter** checkbox.
2. Click **Save**.

For example, ServiceNow events use these settings.

<Image alt="WorkflowsAdapterEventsSettings" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WorkflowsAdapterEventsSettings.png" />

## Managing Generic Webhook Events

From the **Workflows Events** page, you can manage your generic webhook events:

* **Create** - [Create a new Generic Webhook Event](/docs/creating-a-generic-webhook-event) for your organization.
* **Edit** - [Modify the settings of an existing Generic Webhook Event](/docs/managing-generic-webhook-events#modifying-the-generic-webhook-event-settings).
* **Delete** - [Remove a Generic Webhook Event](/docs/managing-generic-webhook-events#deleting-a-generic-webhook-event) that is no longer in use.