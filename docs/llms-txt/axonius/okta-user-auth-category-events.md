# Source: https://docs.axonius.com/docs/okta-user-auth-category-events.md

# Okta User Auth Category Events

Axonius supports **Okta User Auth Category Events** in an Event node of a Workflow.

The following table lists the Okta User Authentication events, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type                      | Description                                                                                                                                                                             | Event Type Name in Okta            |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Sign in**                     | A user attempted single sign-on (SSO) to Okta. Note that the event is created even when the sign-on is unsuccessful.                                                                    | user.authentication.sso            |
| **Sign out**                    | A user performed a single logout (SLO) from Okta.                                                                                                                                       | user.authentication.slo            |
| **User MFA authentication**     | A user was authenticated through multifactor authentication (MFA).                                                                                                                      | user.authentication.auth\_via\_mfa |
| **User MFA factor activated**   | A user activated a new factor in Okta. The event contains information about the MFA factor that has been activated, as well as the target user and the user who activated the factor.   | user.mfa.factor.activate           |
| **User MFA factor deactivated** | A user deactivated a factor in Okta. The event contains information about the MFA factor that has been deactivated, as well as the target user and the user who deactivated the factor. | user.mfa.factor.deactivate         |
| **User MFA factor reset all**   | All of a user's multifactor authentication (MFA) factors were reset in Okta.                                                                                                            | user.mfa.factor.reset\_all         |
| **User MFA factor suspended**   | A user suspended an MFA factor in Okta.                                                                                                                                                 | user.mfa.factor.suspend            |
| **User MFA factor unsuspended** | A user unsuspended an MFA factor in Okta.                                                                                                                                               | user.mfa.factor.unsuspend          |

<Callout icon="📘" theme="info">
  Note

  * Multifactor authentication (MFA) means that users must verify their identity in two or more ways to gain access to their account.
  * Adding authenticators with different factor types and method characteristics strengthens users' MFA strategy.
</Callout>

* In the Okta admin management UI,[add the Okta User Auth event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a user performs a single logout (SLO) from Okta using the Okta admin UI, Axonius receives a *user.authentication.slo* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta User Auth Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *user.mfa.factor.suspend*, *user.mfa.factor.reset\_all*.

## Adding the Okta User Auth Category Events to the Workflow

You can add **Okta User Auth Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta User Auth Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta User Auth Category Events** tile.

![OktaUserAuthCatgoryEventsTrigger](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUserAuthCatgoryEventsTrigger.png)

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved user.

**To select Okta User Auth Category Events as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta User Auth Category Events** tile.

![OktaUserAuthCatgoryEvents](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaUserAuthCatgoryEvents.png)

In this case, when an event from the Okta User Auth category is created in Okta on the asset retrieved from the previous node (in the above example, the action user), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta User Auth Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta User Auth Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaUserAuthCategory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaUserAuthCategory.png)

The following describes these Event fields:

* **ID** - The unique identifier of the Okta user.
* **Type** - Type of Okta user.
* **Alternate ID** - Email address of the Okta user.
* **Display Name** - Display name of the Okta user.
* **Event Type** - Type of event that occurred. For example, *user.mfa.factor.reset\_all*.
* **Event Result** - Result of the event that was triggered.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published the event to the System Log in Okta’s internal systems.
* **Application ID** - Relevant for non-triggering event only. ID of the application.
* **Application Name** - Relevant for non-triggering event only. Name of the application.
* **Event date** - Date the event was triggered.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific Event Type.

* Filter the **Okta User Auth Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *user.authentication.sso*. This means that whenever a user attempts single sign-on (SSO) to Okta, an event is sent to Axonius, which triggers this Workflow.
  ![FilterTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilterTriggeringEvent.png)

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta User Auth Category Event** event to filter it by Event Type. The workflow will only proceed for matching events.\
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *user.authentication.auth\_via\_mfa*. This means that whenever a user is authenticated through multifactor authentication (MFA), the Workflow continues running on the True branch.
  ![FilterNonTriggeringEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FilterNonTriggeringEvent.png)