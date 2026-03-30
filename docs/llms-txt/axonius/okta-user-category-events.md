# Source: https://docs.axonius.com/docs/okta-user-category-events.md

# Okta User Category Events

Axonius supports **Okta User Category Events** in an Event node of a Workflow.

You can perform actions using the Okta admin UI or by running the following Enforcement Actions from the Okta user category, for users retrieved from the saved query supplied as a trigger or users selected in the asset table:

* [Okta - Create user](/docs/create-user-okta) - Creates a user in Okta.
* [Okta - Enable Users](/docs/enable-users-in-okta) - Enables each user by reactivating or unsuspending the users retrieved from the saved query supplied as a trigger or users selected in the asset table.
* [Okta Reset User Password](/docs/reset-user-password-okta) - Forces users to reset their password on the next login.
* [Okta - Disable Users](/docs/disable-users-in-okta) - Can suspend, deactivate, or delete each user returned by the selected query or assets selected on the relevant asset page.
* [Okta - Update User](/docs/update-okta-user).
* [Okta - Revoke User Sessions](/docs/okta-revoke-user-sessions) - Revokes all user sessions for each Okta user returned by the selected query or assets selected on the relevant asset page.

The following table lists the supported Okta User events, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Event Type Name in Okta         |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **Reactivate**            | An Okta user was reactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | user.lifecycle.reactivate       |
| **Deactivate**            | An Okta user was deactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | user.lifecycle.deactivate       |
| **Delete**                | An Okta user delete was initiated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | user.lifecycle.delete.initiated |
| **Delete**                | An Okta user delete was completed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | user.lifecycle.delete.completed |
| **New User**              | An Okta user was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | user.lifecycle.create           |
| **Suspend**               | An Okta user was suspended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | user.lifecycle.suspend          |
| **Unsuspend**             | An Okta user was unsuspended.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | user.lifecycle.unsuspend        |
| **Profile Updated**       | An Okta user profile was updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | user.account.update\_profile    |
| **Account Lock**          | An Okta user account was auto-locked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | user.account.lock               |
| **Account Unlock**        | An Okta user account was auto-unlocked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | user.account.unlock             |
| **User Privilege Grant**  | A User's admin privileges changed. This can be used to audit the provisioning of admin privileges for users. When fired, this event contains information about the type of admin privileges the user currently has. The list of current privileges contain both individually assigned roles as well as the ones granted to the user through their group membership.                                                                                                                                                                                                                                                                                                                                                                                                              | user.account.privilege.grant    |
| **User Privilege Revoke** | All of user's admin privilege revoked. This can be used to audit the deprovisioning of admin privileges from users. When fired, this event indicates the user has no more admin privileges. All of user's privileges were revoked including individually assigned roles as well as the ones granted to the user through their group membership.                                                                                                                                                                                                                                                                                                                                                                                                                                  | user.account.privilege.revoke   |
| **Password Reset**        | This event in Okta's System Log indicates that a user's Okta password has been reset. This event is triggered in two main scenarios: **Administrator-initiated Reset** - An Okta administrator manually resets a user`s password. **Self-Service Password Reset (SSPR)** - A user successfully completes the identity verification steps of the SSPR process (e.g., via email or SMS), which typically begins by clicking `Forgot password' and ends with them selecting a new password.                                                                                                                                                                                                                                                                                         | user.account.reset\_password    |
| **Password Update**       | A user's Okta password was updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | user.account.update\_password   |
| **Password Import**       | A user has successfully logged into Okta and an attempt to import their Password has been made. This can be used to understand if a user password import attempt was successful or if it failed. If the attempt failed, the password import will be tried again on a subsequent successful login. When fired, this event contains information about the import type, and whether or not the password import was successful. If the import is successful, it is safe to "clean up" that user from an external system. If the import failed, Okta will continue retrying the import during every successful authentication attempt until the password is successfully imported. Check the failure reason for details about whether any action is needed for the import to succeed. | user.import.password            |

* In the Okta admin management UI,[add the Okta User event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a user updates their Okta password using the Okta admin UI, Axonius receives a *user.account.update\_password* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta User Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *user.mfa.factor.suspend*, *user.mfa.factor.reset\_all*.

## Adding the Okta User Category Events to the Workflow

You can add **Okta User Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta User Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta User Category Events** tile.
   ![OktaUserCategoryTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUserCategoryTriggeringEvent.png)

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved user.

**To select Okta User Category Events as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta User Category Events** tile.

![OktaUserCategoryEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUserCategoryEvent.png)

In this case, when an event from the Okta User category is created in Okta on the asset retrieved from the previous node (in the above example, the event user), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta User Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta User Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaUserAuthCategory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaUserAuthCategory.png)

The following describes these Event fields:

* **ID** - The unique identifier of the Okta user.
* **Type** - Type of Okta user.
* **Alternate ID** - Email address of the Okta user.
* **Display Name** - Display name of the Okta user.
* **Event Type** - Type of event that occurred. For example, *user.account.unlock*.
* **Event Result** - Result of the event that was triggered.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published this event to the System Log in its internal systems.

<Callout icon="📘" theme="info">
  Note

  The **Event Published At** field is vital for tracking self-service password reset activities (see the **Password Reset** event description above). When a user requests a link to reset their password via email or SMS, a *system.email.password\_reset.sent\_message* or *system.sms.send\_password\_reset\_message* event occurs. Once the user provides the necessary information and successfully resets their password, the *user.account.reset\_password* event is recorded in Okta's System Log, and its **Event Published At** field provides the timestamp for this action.
</Callout>

* **Event date** - Date the event was triggered.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific Event Type.

* Filter the **Okta User Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *user.account.reset\_password*. This means that whenever a user's Okta password is reset, an event is sent to Axonius, which triggers this Workflow.

![OktaUserCategoryTriggerFilter.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUserCategoryTriggerFilter.png)

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta User Category Event** event to filter it by Event Type. The workflow will only proceed for matching events.\
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *user.account.privilege.grant*. This means that whenever a user's admin privileges change, the Workflow continues running on the True branch.

![OktaUserCategoryEventCondition.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUserCategoryEventCondition.png)