# Source: https://docs.axonius.com/docs/servicenow-ticket-updated.md

# ServiceNow Ticket Updated

Axonius supports **ServiceNow Ticket Updated** as an event in a Workflow.

Users can update ServiceNow tickets using the following Enforcement Action:

* [Update ServiceNow Tickets](/docs/update-tickets-servicenow) - Updates tickets (all related tickets, last created ticket, or specific tickets) of all selected assets or assets returned from the query.

ServiceNow ticket updates include changes to the following:

* **Ticket Status** - Changed ticket status. Available options: new, open, pending, hold, solved, closed.
* **Ticket Assignee** - Ticket assigned to another agent.
* **Ticket Comments** - For example, submission channel, IP address, and IP location of the ticket update.

Whenever a user updates a support ticket in ServiceNow, ServiceNow triggers an event. All Workflows configured with this event are then triggered.

## Configuring ServiceNow to Send Events to Axonius

Before including the **ServiceNow Ticket Updated** event in a Workflow the first time, you need to do the following:

* In the [ServiceNow adapter - Advanced Configuration](/docs/servicenow#advanced-settings), enable the **Fetch EC Action ticket updates** option.

* Enable events in the ServiceNow adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![EventServiceNowSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventServiceNowSettings.png)

## Adding the ServiceNow Ticket Updated Event to the Workflow

Add **ServiceNow Ticket Updated** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the ServiceNow Ticket Updated event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **ServiceNow Ticket Updated** tile. The **ServiceNow Ticket Updated** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![EventTriggerServiceNowTicketUpdated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerServiceNowTicketUpdated.png)

The Workflow is triggered each time a ServiceNow ticket is updated. The next node runs on the retrieved ticket.

**To select ServiceNow Ticket Updated as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **ServiceNow Ticket Updated** tile. The **ServiceNow Ticket Updated** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![EventServiceNowTicketUpdated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventServiceNowTicketUpdated.png)

In this case, when a ServiceNow ticket is updated on the asset retrieved from the previous node, an event occurs and the Workflow continues running.