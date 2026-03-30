# Source: https://docs.axonius.com/docs/tenable-security-center-new-alert.md

# Tenable Security Center New Alert

Axonius supports **Tenable Security Center New Alert** as an event in a Workflow.

Whenever a new Tenable alert occurs, Tenable Security Center triggers an event. All Workflows configured with this event are then triggered.

## Configuring Tenable Security Center to Send Events to Axonius

Before including the **Tenable Security Center New Alert** event in a Workflow the first time, you need to do the following:

* In the [Tenable Security Center adapter](/docs/tenablesc-formerly-securitycenter) Advanced Settings, enable the **Enable real-time asset updates (Supported events: New alerts)** option.
* Enable events in the Tenable Security Center adapter [from **System Settings**](/docs/configuring-workflows-events-settings#enabling-events-in-an-adapter) or from the [Workflow Event configuration](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter). The following screen shows enabling events from the **System Settings> External Integrations> Workflows Events** screen.

![TenableSecurityCenterEventSettings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TenableSecurityCenterEventSettings.png)

## Adding the Tenable Security Center New Alert Event to the Workflow

Add **Tenable Security Center New Alert** as the triggering Event of a Workflow or as an event anywhere else in the Workflow, where relevant. When this event occurs, the Workflow begins or continues running.

**To select the Tenable Security Center New Alert event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Incident Created or Updated**, click the **Tenable Security Center New Alert** tile. The **Tenable Security Center New Alert** configuration opens in the **Trigger Type** pane.

2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
   * If events are not enabled in the adapter, the following screen appears:
     ![TenableSecurityNewAlert1.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TenableSecurityNewAlert1.png)
     1. Click **View Webhook Configuration**.
     2. In the **Adapter Events Configuration** dialog, select the **Enable events in adapter checkbox**, and click **Apply**. The screen in the next step appears.
        ![TenableSecurityNewAlert2.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TenableSecurityNewAlert2.png)

3. When events are enabled in a valid adapter connection, the following screen appears:
   ![TenableSecurityNewAlert3.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TenableSecurityNewAlert3.png)

The Workflow is triggered each time a Tenable Security Center alert is created. The next node runs on the retrieved incident.

**To select Tenable Security Center New Alert as a non-triggering event**

1. In the **Event** pane, under **Incident Created or Updated**, click the **Tenable Security Center New Alert** tile. The **ServiceNow New Alert** configuration opens in the **Event** pane.
2. If there is no valid adapter connection or events are not enabled in the adapter,[configure a valid adapter connection and/or enable events in the adapter](/docs/configuring-event-webhook#enabling-events-in-the-product-adapter).
3. When events are enabled in a valid adapter connection, the following screen appears:
   ![TenableSecurityNewAlert4.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TenableSecurityNewAlert4.png)

In this case, when a Tenable Security Center alert is created by the incident retrieved from the previous node, an event occurs, and the Workflow continues running.