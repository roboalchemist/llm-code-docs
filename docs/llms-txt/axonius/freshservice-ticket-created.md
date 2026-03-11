# Source: https://docs.axonius.com/docs/freshservice-ticket-created.md

# Freshservice Ticket Created

Axonius supports **Freshservice Ticket Created** as an event in a Workflow.

Users can create Freshservice tickets using the following Enforcement Actions:

* [Freshservice - Create Ticket](/docs/create-freshservice-ticket) - Creates one ticket for all selected assets or assets returned from the query.

* [Freshservice - Create Ticket per Asset](/docs/create-fresh-service-ticket-per-entity) - Creates a ticket for each selected asset or each asset returned from the query.

Whenever a user creates a support ticket in Freshservice, Freshservice triggers an event. All Workflows configured with this event are then triggered.

## Configuring Freshservice to Send Events to Axonius

Before including the **Freshservice Ticket Created** event in a Workflow the first time, you need to do the following:

* In the [Freshservice adapter - Advanced Configuration](/docs/freshservice#advanced-settings), enable the **Enable real-time asset updates (Supported events: New Tickets)** advanced option.
* Enable events in the Freshservice adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![FreshserviceEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FreshserviceEvent.png)

## Adding the Freshservice Ticket Created Event to the Workflow

Add **Freshservice Ticket Created** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Freshservice Ticket Created event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **Freshservice Ticket Created** tile. The **Freshservice Ticket Created** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerFreshserviceTicketCreated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerFreshserviceTicketCreated.png)

The Workflow is triggered each time a Freshservice ticket is created. The next node runs on the retrieved ticket.

**To select Freshservice Ticket Created as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **Freshservice Ticket Created** tile. The **Freshservice Ticket Created** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventFreshserviceTicketCreated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventFreshserviceTicketCreated.png)

In this case, when a Freshservice ticket is created on the asset retrieved from the previous node (in the above example, the device), an event occurs and the Workflow continues running.