# Source: https://docs.axonius.com/docs/zendesk-ticket-updated.md

# Zendesk Ticket Updated

Axonius supports **Zendesk Ticket Updated** as an event in a Workflow.

Zendesk ticket update events include changes to the following:

* **Ticket properties** - For example, the subject of the ticket, ticket form, group responsible for the ticket, organization associated with the ticket, type of ticket, total time spent, time spent on the last update, status of the ticket, requester, priority, assignee, and CCs.
* **Communications** - For example, automations, routing, and email notifications.
* **User Information** - For example, submission channel, IP address, and IP location of the ticket update.

Users can update Zendesk tickets using the following Enforcement Action:

* [Update Zendesk Tickets](/docs/update-tickets-zendesk) - Updates tickets relevant for Zendesk for all selected assets or assets returned from the query.

Whenever a user updates a support ticket in Zendesk, Zendesk triggers an event. All Workflows configured with this event are then triggered.

## Configuring Zendesk to Send Events to Axonius

Before including the **Zendesk Ticket Updated** event in a Workflow the first time, , you need to do the following:

* In the [Zendesk adapter - Advanced Configuration](/docs/zendesk-adapter#advanced-settings), enable the **Fetch EC Action ticket updates** advanced option.
* Enable events in the Zendesk adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![ZendeskEvent](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ZendeskEvent.png)

## Adding the Zendesk Ticket Updated Event to the Workflow

Add **Zendesk Ticket Updated** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Zendesk Ticket Updated event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **Zendesk Ticket Updated** tile. The **Zendesk Ticket Updated** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerZendeskTicketUpdated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerZendeskTicketUpdated.png)

The Workflow is triggered each time a Zendesk ticket is updated. The next node runs on the retrieved ticket.

**To select Zendesk Ticket Updated as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **Zendesk Ticket Updated** tile. The **Zendesk Ticket Updated** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).

![EventZendeskTicketUpdated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventZendeskTicketUpdated.png)

In this case, when a Zendesk ticket is updated by the User retrieved from the previous node, an event occurs, and the Workflow continues running.