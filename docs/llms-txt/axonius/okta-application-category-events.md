# Source: https://docs.axonius.com/docs/okta-application-category-events.md

# Okta Application Category Events

Axonius supports **Okta Application Category Events** in an Event node of a Workflow.

The following table lists the Okta Application Category Events, i.e., Okta events related to Applications, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type                    | Description                                                                                                                                                                                | Event Type Name in Okta                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| **Consent Granted**           | User granted consent to app in Okta. This event can be used to identify the org AS consent grant. When fired, the event contains information about the successful consent grant by org AS. | app.oauth2.consent.grant                      |
| **Activate**                  | Application was activated in Okta.                                                                                                                                                         | application.lifecycle.activate                |
| **Create**                    | Application was created in Okta.                                                                                                                                                           | application.lifecycle.create                  |
| **Deactivate**                | Application was deactivated in Okta.                                                                                                                                                       | application.lifecycle.deactivate              |
| **Deleted**                   | Application was deleted from Okta.                                                                                                                                                         | application.lifecycle.delete                  |
| **Updated**                   | Application was updated in Okta.                                                                                                                                                           | application.lifecycle.update                  |
| **Sync user**                 | User was synced in an external application in Okta.                                                                                                                                        | application.provision.user.sync               |
| **Assigned user to app**      | User was added to an application membership  in Okta.                                                                                                                                      | application.user\_membership.add              |
| **User app password changed** | User's application password changed in Okta.                                                                                                                                               | application.user\_membership.change\_password |
| **Unassigned user from app**  | User was revoked from an application in Okta (unassigned but not yet deprovisioned).                                                                                                       | application.user\_membership.revoke           |

* In the Okta admin management UI,[add the Okta Application event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a user subscribes to an application using the Okta admin UI, Axonius receives an *application.user\_membership.add* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta Application Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *application.lifecycle.activate*, *application.lifecycle.deactivate*.

## Adding the Okta Application Category Events to the Workflow

You can add **Okta Application Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta Application Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta Application Category Events** tile.

![OktaAppCatgoryEventsTrigger.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaAppCatgoryEventsTrigger.png)

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved application.

**To select Okta Application Category Events as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta Application Category Events** tile.

![OktaAppCatgoryEvents.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaAppCatgoryEvents.png)

In this case, when an event from the Okta Application category is created in Okta on the asset retrieved from the previous node (in the above example, the event application setting), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta Application Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta Application Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaAppCategory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaAppCategory.png)

The following describes these Event fields:

* **ID** - ID of the Okta application.
* **Type** - Type of Okta application.
* **Alternate ID** - Alternate ID of the Okta application.
* **Display Name** - Display name of the Okta application.
* **Event Type** - Type of event that occurred. For example, *application.lifecyce.activate*.
* **Event Result** - Result of the event that was triggered.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published the event to the System Log in Okta’s internal systems.
* **User ID**, **User Display Name** - ID and display name of the Okta user. Relevant for *application.provision.user.sync*, *application.user\_membership.add*, *application.user\_membership.revoke*, and *application.usermembership.changepassword*.
* **Event date** - Date the event occurred.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific event type.

* Filter the **Okta Application Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *application.user\_membership.add*. This means that whenever a user subscribes to an application in Okta, the Workflow begins running.

![OktaAppCategoryFilterTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaAppCategoryFilterTriggeringEvent.png)

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta Application Category** event to filter it by Event Type. The Workflow will only proceed for matching events.
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *application.lifecycle.activate*. This means that whenever an application is activated in Okta, the Workflow continues running on the True branch.

![OktaAppCategoryEventCondition.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaAppCategoryEventCondition.png)