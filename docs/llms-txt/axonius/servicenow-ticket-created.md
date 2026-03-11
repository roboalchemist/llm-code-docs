# Source: https://docs.axonius.com/docs/servicenow-ticket-created.md

# ServiceNow Ticket Created

Axonius supports **ServiceNow Ticket Created** as an event in a Workflow.

Users can create ServiceNow tickets using the following Enforcement Actions:

* [ServiceNow - Create Incident](/docs/create-servicenow-incident) - Creates one ticket in ServiceNow for all selected assets or assets returned from the query.

* [ServiceNow - Create Incident per Asset](/docs/create-servicenow-incident-per-entity) - Creates a ticket in ServiceNow for each selected asset or each asset returned from the query.

Whenever a user creates a support ticket in ServiceNow, ServiceNow triggers an event. All Workflows configured with this event are then triggered.

## Configuring ServiceNow to Send Events to Axonius

Before including  the **ServiceNow Ticket Created** event in a Workflow the first time, you need to do the following:

* In the [ServiceNow adapter - Advanced Configuration](/docs/servicenow#advanced-settings), enable the **Enable real-time asset updates (Supported events: New users, New Tickets)** option.
* Enable events in the ServiceNow adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![EventServiceNowSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventServiceNowSettings.png)

## Adding the ServiceNow Ticket Created Event to the Workflow

Add **ServiceNow Ticket Created** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the ServiceNow Ticket Created event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **ServiceNow Ticket Created** tile. The **ServiceNow Ticket Created** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![ServiceNowTicketCreatedTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNowTicketCreatedTriggerEvent.png)

The Workflow is triggered each time a ServiceNow ticket is created. The next node runs on the retrieved ticket.

**To select ServiceNow Ticket Created as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **ServiceNow Ticket Created** tile. The **ServiceNow Ticket Created** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![ServiceNowTicketCreatedNonTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNowTicketCreatedNonTriggerEvent.png)

In this case, when a ServiceNow ticket is created on the asset retrieved from the previous node, an event occurs and the Workflow continues running.