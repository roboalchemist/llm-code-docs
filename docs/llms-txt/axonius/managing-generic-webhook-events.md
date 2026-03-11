# Source: https://docs.axonius.com/docs/managing-generic-webhook-events.md

# Managing Generic Webhook Events

## Viewing the Event Configuration

You can view the configuration of a Generic Webhook Event at any time from:

* The event in your Workflow - Click **View Configuration** to open the **Webhook Configuration Details** dialog.
* The **Workflow Events** page - Navigate to **System Settings> External Integrations> Workflows Events** and select the **Generic Webhook Events** product.

The configuration includes the webhook URL and the private secure key.

## Modifying the Event Configuration

* You can modify the Generic Webhook Event's **Private Secure Key** from the **Workflow Events** system settings or the **Webhook Configuration Details** dialog.

* You can modify fields in any of the steps of the Generic Webhook Event Settings (General, Schema, or Asset Mapping) from the **Edit Generic Webhook Event** wizard, accessible from the **Workflow Events** system settings or the **Webhook Configuration Details** dialog.

* After you change the Private Secure Key value, update it in the external service as well.

* You cannot change the URL.

### Modifying the Private Secure Key

**To modify the Private Secure Key from System Settings:**

1. In the **Workflows Events** page, modify the **Private Secure Key**, and click **Save**.

**To modify the Private Secure Key from the Workflow:**

1. In the **Trigger Type** or **Event** pane in the Workflow, under **Generic Webhook Events**, select an event, and click **View Configuration**.
2. In the **Webhook Configuration Details** dialog that opens, modify the **Private Secure Key**, and then click **Enable Webhook**.

### Modifying the Generic Webhook Event Settings

**To modify the Generic Webhook Event settings from System Settings**

1. In the **Workflows Events** page of the selected event, click **Edit**.
2. In the **Edit Generic Webhook Event** wizard that opens, modify the fields as necessary, the same way you [create these fields](creating-a-generic-webhook-event), and then click **Save Generic Event**.

**To modify the Generic Webhook Event settings from the Workflow:**

1. In the **Trigger Type** or **Event** pane in the Workflow, click **View Configuration**.
2. In the **Webhook Configuration Details** dialog that opens, click **Edit**.
3. In the **Edit Generic Webhook Event** wizard that opens, modify the fields as necessary, the same way you [create these fields](creating-a-generic-webhook-event), and then click **Save Generic Event**.

## Deleting a Generic Webhook Event

You can delete a Generic Webhook Event, provided it is not used in any Workflow.

**To delete a Generic Webhook Event:**

1. In **System Settings> External Integrations> Workflows Events**, under
   **Generic Webhook Events**, select the event you want to delete.

2. Click **Delete Event**.

3. In the confirmation box that opens, click **Delete Webhook**. Once removed, you cannot restore the Webhook.