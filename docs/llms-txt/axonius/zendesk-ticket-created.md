# Source: https://docs.axonius.com/docs/zendesk-ticket-created.md

# Zendesk Ticket Created

Axonius supports **Zendesk Ticket Created** as an event in a Workflow.

Users can create Zendesk tickets using the following Enforcement Actions:

* [Zendesk - Create Ticket](/docs/create-zendesk-ticket) - Creates one ticket in Zendesk for all selected assets or assets returned from the query.
* [Zendesk - Create Ticket Per Entity](/docs/zendesk-create-ticket-per-entity) - Creates a ticket in Zendesk for each selected asset or each asset returned from the query.

Whenever a user creates a support ticket in Zendesk, Zendesk creates an event. All Workflows configured with this event are then triggered.

## Configuring Zendesk to Send Events to Axonius

Before including the **Zendesk Ticket Created** event in a Workflow the first time, you need to do the following:

* In the [Zendesk adapter - Advanced Configuration](/docs/zendesk-adapter#advanced-settings), enable the **Enable real-time asset updates (Supported events: New Tickets)** option.
* Enable events in the Zendesk adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![ZendeskEvent](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ZendeskEvent.png)

## Adding the Zendesk Ticket Created Event to the Workflow

Add **Zendesk Ticket Created** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Zendesk Ticket Created event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **Zendesk Ticket Created** tile. The **Zendesk Ticket Created** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerZendeskTicketCreated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerZendeskTicketCreated.png)

The Workflow is triggered each time a Zendesk ticket is created. The next node runs on the retrieved ticket.

**To select Zendesk Ticket Created as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **Zendesk Ticket Created** tile. The **Zendesk Ticket Created** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventZendeskTicketCreated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventZendeskTicketCreated.png)

In this case, when a Zendesk ticket is created by the User retrieved from the previous node, an event occurs, and the Workflow continues running.