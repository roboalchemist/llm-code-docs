# Source: https://docs.axonius.com/docs/okta-device-category-events.md

# Okta Device Category Events

Axonius supports **Okta Device Category Events** in an Event node of a Workflow.

The following table lists the Okta Device Category Events, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type             | Description                                                                                                                                                            | Event Type Name in Okta     |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| **Activate**           | Device was activated in Okta.                                                                                                                                          | device.lifecycle.activate   |
| **Deactivate**         | Device was deactivated in Okta.                                                                                                                                        | device.lifecycle.deactivate |
| **Deleted**            | Device was deleted from Okta. The device no longer appears in the Admin console.                                                                                       | device.lifecycle.delete     |
| **Suspend**            | Device was suspended in Okta. When triggered, access to the device is temporarily paused. Only active devices can be suspended.                                        | device.lifecycle.suspend    |
| **Unsuspend**          | Device was unsuspended in Okta. When triggered, all Okta factors associated with the device are unsuspended, and users can access protected resources from the device. | device.lifecycle.unsuspend  |
| **Enrolled**           | A new device was registered successfully in Okta.                                                                                                                      | device.enrollment.create    |
| **Add user to device** | A device was added to a user in Okta. The event is triggered when a user adds a new account in Okta.                                                                   | device.user.add             |
| **Remove from user**   | A device was removed for a user in Okta. The device remains in the Universal Directory after the user is removed.                                                      | device.user.remove          |

* In the Okta admin management UI,[add the Okta Device event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a customer removes a user from a device using the Okta admin UI, Axonius receives a *device.user.remove* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta Device Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *device.lifecycle.activate*, *device.lifecycle.deactivate*.

## Adding the Okta Device Category Events to the Workflow

You can add **Okta Device Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta Device Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta Device Category Events** tile.

![OktaDeviceCatgoryEventsTrigger.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaDeviceCatgoryEventsTrigger.png)

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved device.

**To select Okta Device Category Events as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta Device Category Events** tile.
   ![OktaDeviceCatgoryEvents.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaDeviceCatgoryEvents.png)

In this case, when an event from the Okta Device category is created in Okta on the asset retrieved from the previous node (in the above example, the action device), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta Device Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta Device Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaDeviceCategory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaDeviceCategory.png)

The following describes these Event fields:

* **ID** - ID of the device.
* **Type** - Type of device.
* **Alternate ID** - Alternate ID of the device.
* **Display Name** - Display name of the device.
* **User ID** - ID of the Okta user with added device. Relevant only for device.user.add and device.user.remove event types.
* **User Display** - Display name of the Okta user with added device. Relevant only for device.user.add and device.user.remove event types.
* **Event Type** - Type of event that was triggered. For example, *device.lifecyce.activate*.
* **Event Result** - Result of the event that was triggered.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published the event to the System Log in Okta’s internal systems.
* **Event date** - Date the event was triggered.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific event type.

* Filter the **Okta Device Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *device.lifecycle.deactivate*. This means that whenever a device is deactivated in Okta, the Workflow begins running.
  ![FilterTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilterTriggeringEvent.png)

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta Device Category** event to filter it by Event Type. The Workflow will only proceed for matching events.
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *device.lifecycle.activate*. This means that whenever a device is activated in Okta, the Workflow continues running on the True branch.
  ![FilterNonTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilterNonTriggeringEvent.png)