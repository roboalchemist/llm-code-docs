# Source: https://docs.axonius.com/docs/okta-policy-category-events.md

# Okta Policy Category Events

Axonius supports **Okta Policy Category Events** in an Event node of a Workflow.

You can perform actions using the Okta admin UI or by running the following Enforcement Actions from the Okta Policy category, for users retrieved from the saved query supplied as a trigger or users selected in the asset table:

[Okta - Activate rule](/docs/okta-activate-rule) - Activates a rule in Okta.

[Okta - Deactivate Rule](https://docs.axonius.com/axonius-help-docs/docs/okta-deactivate-rule-1) - Deactivates a rule in Okta.

The following table lists the Okta Policy Category Events, their descriptions, as well as their event names in Okta. Learn more about these [event types](https://developer.okta.com/docs/reference/api/event-types/).

| Event Type          | Description                          | Event Type Name in Okta     |
| ------------------- | ------------------------------------ | --------------------------- |
| **Activate**        | Policy was activated in Okta.        | policy.lifecycle.activate   |
| **Deactivate**      | Policy was deactivated in Okta.      | policy.lifecycle.deactivate |
| **Update**          | Policy was updated in Okta.          | policy.lifecycle.update     |
| **Add Rule**        | Policy rule was added in Okta.       | policy.rule.add             |
| **Rule deactivate** | Policy rule was deactivated in Okta. | policy.rule.deactivate      |
| **Rule deleted**    | Policy rule was deleted from Okta.   | policy.rule.delete          |
| **Rule updated**    | Policy rule was updated in Okta.     | policy.rule.update          |

* In the Okta admin management UI,[add the Okta Policy event types you want to monitor and use in the Workflow](#integrating-okta-with-axonius).
* Whenever one of the registered events occurs in the Okta admin UI, a Webhook event is sent to the Axonius URL for Okta events. For example, if a customer updates a policy using the Okta admin UI, Axonius receives a *policy.lifecycle.update* event and any Workflows configured with this event are triggered.

## Integrating Okta with Axonius

Before Okta can begin sending **Okta Policy Category Events**, you must [configure the following in the Okta admin management UI](integrating-okta-with-axonius):

* Axonius webhook URL that is to receive Okta events.

* Private Secure Key.

* The event types from the above table in Okta, which you want to monitor and include in Workflows. For example, *policy.lifecycle.activate*, *policy.lifecycle.deactivate*.

## Adding the Okta Policy Category Events to the Workflow

You can add **Okta Policy Category Events** in the triggering Event node of a Workflow or in an Event node anywhere else in the Workflow, where relevant. When an event from this category occurs, the Workflow begins or continues running.

**To select Okta Policy Category Events as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Okta Policy Category Events** tile.

<Image alt="OktaPolicyCatgoryEventsTrigger.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaPolicyCatgoryEventsTrigger.png" />

The Workflow is triggered each time an event from this category occurs in Okta. The next node runs on the retrieved policy.

**To select Okta Policy Category Events as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Okta Policy Category Events** tile.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaPolicyCatgoryEvents.png)

In this case, when an event from the Okta Policy category is created in Okta on the asset retrieved from the previous node (in the above example, the action policy), an event occurs and the Workflow continues running.

## Viewing the Event Structure

After you select the event, you can view the structure of the Events that Okta hook delivers to the Axonius Webhook URL. You can then use these Event fields to follow up on **Okta Policy Category Events** in a Workflow, for example in triggering Event filters or in Event Conditions.

**To view the Event fields**

* In the **Trigger Type** or **Event** configuration panes for the **Okta Policy Category Events** (see above screens), click **Event Fields**. A list opens of all Event field names and their field types.

<Image alt="EventFieldsOktaPolicyCategory.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFieldsOktaPolicyCategory.png" />

The following describes these Event fields:

* **Event Type** - Type of event that occurred. For example, *policy.lifecyce.activate*.
* **Policy Entity ID** - Unique identifier of the Okta policy.
* **Policy Entity Alternate ID** - Alternate ID of the Okta policy.
* **Policy Entity Display Name** - Display name of the Okta policy.
* **Policy Rule ID** - Unique identifier of the policy rule.
* **Policy Rule Alternate ID** - Alternate ID of the policy rule.
* **Policy Rule Display Name** - Display name of the policy rule.
* **Event date** - Date the event occurred.
* **Event timestamp** - Timestamp when the notification was delivered to Axonius.

## Filtering By Event Type

This section describes how to set up your Workflow to be triggered or continued only for a specific event type.

* Filter the **Okta Policy Category Events** triggering event so that only a specific Event Type triggers the Workflow. Learn how to [filter a triggering event](/docs/selecting-the-workflow-trigger#filtering-the-triggering-event).
  The following example shows a Workflow that is triggered only for **Event Type** = *policy.rule.update*. This means that whenever a policy rule is updated in Okta, the Workflow begins running.

<Image alt="OktaPolicyCategoryFilterTriggeringEvent.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaPolicyCategoryFilterTriggeringEvent.png" />

* [Add an Event Condition](/docs/configuring-an-event-condition#adding-conditions-based-on-event-criteria) under any **Okta Policy Category** event to filter it by Event Type. The Workflow will only proceed for matching events.
  The following example shows a Workflow that continues on the True branch only for **Event Type** = *policy.rule.deactivate*. This means that whenever a policy rule is deactivated in Okta, the Workflow continues running on the True branch.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OktaPolicyCategoryEventCondition.png)