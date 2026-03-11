# Source: https://docs.axonius.com/docs/okta-new-user.md

# Okta New User

Axonius supports **Okta New User** as an event in a Workflow.

* In the Okta admin management UI,[add the event type name: *user.lifecycle.create*](#integrating-okta-with-axonius).
* Whenever a new user event occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta. Then, any Workflows configured with the **Okta New User** event are triggered (if a triggering event) or continue (if a non-triggering event).

You can create new Okta users using the following Enforcement Action:

* [Okta - Create User](/docs/create-user-okta) - Creates one user in Okta for each user returned by the selected query or users selected on the Users page.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta New User** events to Axonius, you must [configure the following in Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The *user.lifecycle.create* event type.

## Adding the Okta New User Event to the Workflow

You can add **Okta New User** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Okta New User event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta New User** tile.

![OktaNewUserTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaNewUserTriggerEvent.png)

The Workflow is triggered each time a new user is created in Okta. The next node runs on the retrieved user.

**To select Okta New User as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta New User** tile.

![OktaNewUserEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaNewUserEvent.png)

In this case, when a new user is created in Okta on the asset retrieved from the previous node (in the above example, the event user), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta New User** events in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta New User** event (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaNewUser.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaNewUser.png)

The following describes these Event fields:

* **ID** - ID of the Okta user who was created.
* **Type** - Type of Okta user created.
* **Alternate ID** - Email address of the Okta user.
* **Display Name** - Display name of the Okta user.
* **Event date** - Date the event occurred.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published the event to the System Log in Okta’s internal systems.