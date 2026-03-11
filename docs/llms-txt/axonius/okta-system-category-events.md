# Source: https://docs.axonius.com/docs/okta-system-category-events.md

# Okta System Category Events

Axonius supports **Okta System Category Events** in an Event node of a Workflow.

The following table lists the Okta System Category Events, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type                    | Description                                                     | Event Type Name in Okta                       |
| ----------------------------- | --------------------------------------------------------------- | --------------------------------------------- |
| **Verification SMS sent**     | A phone verification SMS message was sent.                      | system.sms.send\_phone\_verification\_message |
| **Verification call sent**    | A phone verification call was sent.                             | system.voice.send\_phone\_verification\_call  |
| **API token created**         | API token was created.                                          | system.api\_token.create                      |
| **API token revoked**         | API token was revoked.                                          | system.api\_token.revoke                      |
| **Rate limit warning**        | An endpoint is nearing its rate limit.                          | system.org.rate\_limit.warning                |
| **Rate limit violation**      | An endpoint exceeded its rate limit.                            | system.org.rate\_limit.violation              |
| **Import started**            | Import started.                                                 | system.import.start                           |
| **Import complete**           | Import process completed.                                       | system.import.complete                        |
| **Import roadblocks**         | An import roadblock was triggered due to an exceeded threshold. | system.import.roadblock                       |
| **Authenticator activated**   | An admin activated an authenticator for the org.                | security.authenticator.lifecycle.activate     |
| **Authenticator deactivated** | An admin deactivated an authenticator for the org.              | security.authenticator.lifecycle.deactivate   |
| **Submitted**                 | An access request was created.                                  | access.request.create                         |
| **Resolved**                  | An access request was resolved.                                 | access.request.resolve                        |

* In the Okta admin management UI,[add the Okta System event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a customer starts an import using the Okta admin UI, Axonius receives a *system.import.start* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta System Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *system.api\_token.create*, *system.api\_token.revoke*.

## Adding the Okta System Category Events to the Workflow

You can add **Okta System Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta System Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta System Category Events** tile.

![OktaSystemCatgoryEventsTrigger.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaSystemCatgoryEventsTrigger.png)

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved system.

**To select Okta System Category Events as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta System Category Events** tile.

![OktaSystemCatgoryEvents.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaSystemCatgoryEvents.png)

In this case, when an event from the Okta System category is created in Okta on the asset retrieved from the previous node (in the above example, the action system), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta System Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta System Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

![EventFieldsOktaAppCategory.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaAppCategory.png)

The following describes these Event fields:

* **ID** - ID of the Okta system.
* **Type** - Type of Okta system.
* **Alternate ID** - Alternate ID of the Okta system.
* **Display Name** - Display name of the Okta system.
* **Event Type** - Type of event that occurred. For example, *system.import.start*.
* **Event Result** - Result of the event that was triggered.
* **Event Published At** - Indicates the precise time (standard timestamp in ISO 8601 format) that Okta recorded and published the event to the System Log in Okta’s internal systems.
* **Event date** - Date the event occurred.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific event type.

* Filter the **Okta System Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *system.import.start*. This means that whenever an import starts in Okta, the Workflow begins running.

![OktaSystemCategoryTriggerFilter.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaSystemCategoryTriggerFilter.png)

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta System Category** event to filter it by Event Type. The Workflow will only proceed for matching events.
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *security.authenticator.lifecycle.activate*. This means that when an admin activates an authenticator in Okta, the Workflow continues running on the True branch.
  ![OktaSystemCategoryEventCondition](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaSystemCategoryEventCondition.png)