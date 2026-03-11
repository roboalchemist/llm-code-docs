# Source: https://docs.axonius.com/docs/servicenow-user-created.md

# ServiceNow User Created

Axonius supports **ServiceNow User Created** as an event in a Workflow.

Users can create ServiceNow users using the following Enforcement Action:

* [ServiceNow - Create User](/docs/create-servicenow-user) - Creates a ServiceNow user account for all selected users or users returned from the query.

Each time a new user is added to ServiceNow, ServiceNow triggers an event. All Workflows configured with this event are then triggered.

## Configuring ServiceNow to Send Events to Axonius

Before including the **ServiceNow User Created** event in a Workflow the first time, you need to do the following:

* In the [ServiceNow adapter](/docs/servicenow), enable the **Enable real-time asset updates (Supported events: New users, New Tickets)** option.
* Enable events in the ServiceNow adapter [from **System Settings**](/docs/configuring-event-webhook) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.
  ![EventServiceNowSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventServiceNowSettings.png)

## Adding the ServiceNow User Created Event to the Workflow

Add **ServiceNow User Created** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the ServiceNow User Created event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **ServiceNow User Created** tile. The **ServiceNow User Created** configuration opens in the **Trigger Type** pane.

2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
   * If events are not enabled in the adapter, the following screen appears:
     ![ServiceNowUserCreatedTriggerEventA.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNowUserCreatedTriggerEventA.png)

     a. Click **View Webhook Configuration**.
     ![ServiceNowAdapterEventsConfig.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNowAdapterEventsConfig.png)

     b. Select the **Enable events in adapter checkbox** and click **Apply**. The screen in the next step appears.

3. When events are enabled in a valid adapter connection, the following screen appears:
   ![ServiceNowUserCreatedTriggerEventB.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNowUserCreatedTriggerEventB.png)

The Workflow is triggered each time a ServiceNow user is created. The next node runs on the retrieved user.

**To select ServiceNow User Created as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **ServiceNow User Created** tile. The **ServiceNow User Created** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![ServiceUserCreatedNonTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceUserCreatedNonTriggerEvent.png)

In this case, when a ServiceNow user is created on the asset retrieved from the previous node (in the above example, the user), an event occurs, and the Workflow continues running.