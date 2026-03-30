# Source: https://docs.axonius.com/docs/okta-group-category-events.md

# Okta Group Category Events

Axonius supports **Okta Group Category Events** in an Event node of a Workflow.

You can perform actions using the Okta admin UI or by running the following Enforcement Actions for assets retrieved from the saved query supplied as a trigger or assets selected in the asset table:

* [Okta - Update Group](/docs/update-okta-group) - Updates a group in Okta.
* [Okta - Create Group](/docs/create-okta-group) - Creates a group in Okta.
* [Okta - Delete Group](/docs/delete-okta-group) - Deletes a group in Okta.
* [Okta - Add or Remove Users to/from Group](/docs/add-remove-user-in-group-okta) - Adds users to a group or removes users from a group.

The following table lists the supported Okta Group events, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type                 | Description                                                                                                                                                                                                                                                                                                                                                                                           | Event Type Name in Okta       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **Privilege Granted**      | Group's admin privilege was granted. This can be used to audit the provisioning of admin privileges for groups. When fired, this event contains information about the type of admin privileges the group currently has, and what entity sources the group. The group granted privileges can be an Okta sourced group, an AD-sourced group, or an LDAP-sourced group.                                  | group.privilege.grant         |
| **Privilege Revoked**      | Group's admin privilege was revoked. This can be used to audit the deprovisioning of admin privileges from groups. When fired, this event indicates the group has no more admin privileges.                                                                                                                                                                                                           | group.privilege.revoke        |
| **Profile Updated**        | Okta group profile was updated. Events of this type can be used by an IT administrator who wants to trigger an Okta Workflow to provision groups into downstream systems. The utility of the Event type is for Provisioning use cases to downstream systems. A classic example of this is a customer who uses Okta for Office 365 LCM, and wants to push a distribution list from Okta to Office 365. | group.profile.update          |
| **Import Group Created**   | Create group was triggered by import process.                                                                                                                                                                                                                                                                                                                                                         | system.import.group.create    |
| **Import Group Deleted**   | Remove group was triggered by import process.                                                                                                                                                                                                                                                                                                                                                         | system.import.group.delete    |
| **Add user to group**      | A user was added to group membership.                                                                                                                                                                                                                                                                                                                                                                 | group.user\_membership.add    |
| **Remove user from group** | A user was removed from group membership.                                                                                                                                                                                                                                                                                                                                                             | group.user\_membership.remove |

* In the Okta admin management UI,[add the Okta Group event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a user is added to a Group, Axonius receives a *group.user\_membership.add* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta Group Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *group.user\_membership.add*, *system.import.group.create*.

## Adding the Okta Group Category Events to the Workflow

You can add **Okta Group Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta Group Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **Group Onboarded or Offboarded**, click the **Okta Group Category Events** tile.
   ![OktaGroupCategoryTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaGroupCategoryTriggeringEvent.png)

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved Group.

**To select Okta Group Category Events as a non-triggering event**

1. In the **Event** pane, under **Group Onboarded or Offboarded**, click the **Okta Group Category Events** tile.
   ![OktaGroupCategoryEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaGroupCategoryEvent.png)

In this case, when an event from the Okta Group category is created in Okta on the asset retrieved from the previous node (in the above example, the event user), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta Group Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta Group Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.
  ![EventFieldsOktaUserAuthCategory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaUserAuthCategory.png)

The following describes these Event fields:

* **ID** - The unique identifier of the Okta Group.
* **Type** - Type of Okta Group.
* **Alternate ID** - Alternate ID of the Okta Group.
* **Display Name** - Display name of the Okta Group.
* **Event Type** - Type of event that occurred. For example, *group.user\_membership.remove*.
* **Event Result** - Result of the event that was triggered.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published the event to the System Log in Okta’s internal systems.
* **User ID** - ID of user added/removed to/from the group.
* **User Name** - Username of the user added/removed to/from the group.
* **Event date** - Date the event was triggered.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific Event Type.

* Filter the **Okta Group Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *group.user\_membership*. This means that whenever a user is added to or removed from Okta group membership, an event is sent to Axonius, which triggers this Workflow.
  ![OktaGroupCategoryTriggerFilter.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaGroupCategoryTriggerFilter.png)

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta Group Category Event** event to filter it by Event Type. The workflow will only proceed for matching events.\
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *group.user\_membership.add*. This means that whenever a a user is added to Okta group membership, the Workflow continues running on the True branch.
  ![OktaGroupCategoryEventCondition.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaGroupCategoryEventCondition.png)