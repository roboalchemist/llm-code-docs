# Source: https://docs.axonius.com/docs/jira-ticket-event.md

# Jira Service Management Ticket Created

Axonius supports **Jira Service Management Ticket Created** as an event in a Workflow.

Users can create Jira Service Management tickets using the following Enforcement Actions:

* [Jira Service Management - Create Ticket](/docs/create-jira-service-desk-ticket) - Creates one ticket in Jira Service Management for all selected assets or assets returned from the query.

* [Jira Service Management - Create Ticket per Asset](/docs/create-jira-service-desk-incident-per-entity) - Creates a ticket in Jira Service Management for each selected asset or each asset returned from the query.

Whenever a user creates a support ticket in Jira Service Management, Jira triggers an event. All Workflows configured with this event are then triggered.

## Configuring Jira Service Management to Send Events to Axonius

Before including the **Jira Service Management Ticket Created** event in a Workflow the first time, you need to do the following:

* In the [Jira Service Management (Service Desk) Fetch Tickets adapter - Advanced Configuration](/docs/jira-fetch-tickets#advanced-settings), enable the **Enable real-time asset updates (Supported events: New Tickets)** advanced option.
* Enable events in the Atlassian adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen..

![AttlasianEnableAdapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AttlasianEnableAdapter.png)

## Adding the Jira Service Management Ticket Created Event to the Workflow

Add **Jira Service Management Ticket Created** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Jira Service Management Ticket Created event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **Jira Service Management Ticket Created** tile. The **Jira Service Management Ticket Created** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerJiraTicketCreated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerJiraTicketCreated.png)

The Workflow is triggered each time a Jira Service Management ticket is created. The next node runs on the retrieved ticket.

**To select Jira Service Management Ticket Created as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **Jira Service Management Ticket Created** tile. The **Jira Service Management Ticket Created** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventJiraTicketCreated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventJiraTicketCreated.png)

In this case, when a Jira Service Management ticket is created on the asset retrieved from the previous node (in the above example, the event user), an event occurs and the Workflow continues running.