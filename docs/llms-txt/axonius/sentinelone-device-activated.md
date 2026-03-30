# Source: https://docs.axonius.com/docs/sentinelone-device-activated.md

# SentinelOne Device Activated

Axonius supports **SentinelOne Device Activated** as an event in a Workflow.

Whenever a SentinelOne device is activated, SentinelOne triggers an event. All Workflows configured with this event are then triggered.

## Configuring SentinelOne to Send Events to Axonius

Before including  the **SentinelOne Device Activated** event in a Workflow the first time, you need to do the following:

* In the [SentinelOne adapter](/docs/sentinelone), enable the **Enable real-time asset updates (Supported events: Recently activated devices)** option.
* Enable events in the SentinelOne adapter from [System Settings - Workflows Events](/docs/configuring-workflows-events-settings#enabling-events-in-the-product-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.
  ![EventSentinelOneSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EventSentinelOneSettings.png)

## Adding the SentinelOne Device Activated Event to the Workflow

Add **SentinelOne Device Activated** as the triggering event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the SentinelOne Device Activated event as the Workflow trigger**

1. In the **Trigger Type** pane, under **User Onboarded or Offboarded**, click the **SentinelOne Device Activated** tile. The **SentinelOne Device Activated** configuration opens in the **Trigger Type** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears.
   ![SerntinelOneDeviceActivatedTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SerntinelOneDeviceActivatedTriggerEvent.png)

The Workflow is triggered each time a SentinelOne device is activated. The next node runs on the retrieved device.

**To select SentinelOne Device Activated as a non-triggering event**

1. In the **Event** pane, under **User Onboarded or Offboarded**, click the **SentinelOne Device Activated** tile. The **SentinelOne Device Activated** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![SerntinelOneDeviceActivatedNonTriggerEvent.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SerntinelOneDeviceActivatedNonTriggerEvent.png)

In this case, when a SentinelOne device is activated on the asset (device) retrieved from the previous node, an event occurs and the Workflow continues running.