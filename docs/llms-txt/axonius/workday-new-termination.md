# Source: https://docs.axonius.com/docs/workday-new-termination.md

# Workday New Termination

Axonius supports **Workday New Termination** as an event in a Workflow.

Users can suspend a Workday user account using the following Enforcement Action:

* [Workday - Suspend User](/docs/suspend-workday-user) - Suspends a Workday user account for all selected user assets or user assets returned from the query.

Whenever an employee stops working, Workday triggers an event. All Workflows configured with this event are then triggered.

## Configuring Workday to Send Events to Axonius

Before including the **Workday New Termination** event in a Workflow the first time, you need to do the following:

* In the [Workday adapter - Advanced Configuration](/docs/workday#advanced-settings), enable the **Enable real-time asset updates (Supported events: New hires, New terminations)** advanced option.
* Enable events in the Workday adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![WorkdayEventSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WorkdayEventSettings.png)

## Adding the Workday New Termination Event to the Workflow

Add **Workday New Termination** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Workday New Termination event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Workday New Termination** tile. The **Workday New Termination** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventTriggerWorkdayNewTermination.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventTriggerWorkdayNewTermination.png)

The Workflow is triggered each time a user is added as a Workday new hire. The next node runs on the retrieved user.

**To select Workday New Termination as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Workday New Termination** tile. The **Workday New Termination** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:

![EventWorkdayNewTermination.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventWorkdayNewTermination.png)

In this case, when a  user asset retrieved from the previous node terminates employment, an event occurs and the Workflow continues running.