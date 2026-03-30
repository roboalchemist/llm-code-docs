# Source: https://docs.axonius.com/docs/ceridian-dayforce-new-termination.md

# Ceridian Dayforce New Termination

Axonius supports **Ceridian Dayforce New Termination** as an event in a Workflow.

Whenever the Ceridian Dayforce adapter detects a new termination (employee stops working), it sends an event to all Workflows configured with the **Ceridian Dayforce New Termination** event.

## Configuring Ceridian Dayforce to Send Events to Axonius

Before including the **Ceridian Dayforce New Termination** event in a Workflow the first time, you need to do the following:

* In the [Ceridian Dayforce adapter - Advanced Configuration](/docs/ceridian-dayforce#advanced-settings), enable the **Enable real-time asset updates (Supported events: New hires, New terminations)** advanced option.

* Enable events in the Ceridian Dayforce adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CeridianDayforceEventSettings.png)

## Adding the Ceridian Dayforce New Termination Event to the Workflow

Add **Ceridian Dayforce New Termination** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Ceridian Dayforce New Termination event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **Ceridian Dayforce New Termination** tile. The **Ceridian Dayforce New Termination** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter, <Anchor label="configure a valid adapter connection and/or enable events in the adapter" target="_blank" href="/docs/configuring-a-workflow-event#enabling-events-in-the-product-adapter">configure a valid adapter connection and/or enable events in the adapter</Anchor>.
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CeridianTerminationTriggerEvent.png)

The Workflow is triggered each time a user is added as a Ceridian Dayforce new termination. The next node runs on the retrieved user.

**To select Ceridian Dayforce New Termination as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **Ceridian Dayforce New Termination** tile. The **Ceridian Dayforce New Termination** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter, <Anchor label="configure a valid adapter connection and/or enable events in the adapter" target="_blank" href="/docs/configuring-a-workflow-event#enabling-events-in-the-product-adapter">configure a valid adapter connection and/or enable events in the adapter</Anchor>.
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CeridianTerminationNonTriggerEvent.png)

In this case, when a  user asset retrieved from the previous node terminates employment, an event occurs and the Workflow continues running.