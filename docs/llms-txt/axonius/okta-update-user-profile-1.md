# Source: https://docs.axonius.com/docs/okta-update-user-profile-1.md

# Okta Update User Profile

Axonius supports **Okta Update User Profile** as an event in a Workflow.

* In the Okta admin management UI,[add the event type name: *user.account.update\_profile*](#integrating-okta-with-axonius).
* Whenever a user profile updated event occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta. Then, any Workflows configured with the **Okta Update User Profile** event are triggered (if a triggering event) or continue (if a non-triggering event).

You can update Okta user profiles using the following Enforcement Action:

* [Okta - Update user](/docs/update-okta-user) - Updates the profile for each Okta user returned by the selected query or selected on the Users page.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta Update User Profile** events to Axonius, you must [configure the following in Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.
* Private Secure Key.
* The *user.account.update\_profile* event type.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta Update User Profile** events in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta Update User Profile** event (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaNewUser.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaNewUser.png)

The following describes these Event fields:

* **ID** - ID of the Okta user who was created.

* **Type** - Type of Okta user created.

* **Alternate ID** - Email address of the Okta user.

* **Display Name** - Display name of the Okta user.

* **Event date** - Date the event occurred.

* **Event timestamp** - Timestamp when the notification was delivered to Axonius

## Adding the Okta Update User Profile Event to the Workflow

You can add **Okta Update User Profile** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Okta Update User Profile event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta Update User Profile** tile.

![OktaUpdateUserProfileTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUpdateUserProfileTriggerEvent.png)

The Workflow is triggered each time a user profile is updated in Okta. The next node runs on the retrieved user.

**To select Okta Update User Profile as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta Update User Profile** tile.

![OktaUpdateUserProfileEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUpdateUserProfileEvent.png)

In this case, when a user profile is updated in Okta on the asset retrieved from the previous node (in the above example, the event user), an event occurs and the Workflow continues running.