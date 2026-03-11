# Source: https://docs.axonius.com/docs/iot-discovery-workspace.md

# IoT/OT Discovery Workspace

The **IoT/OT Discovery** workspace provides a unified asset record for all connected devices by aggregating and normalizing data from disparate security, IT, and specialized clinical/industrial systems. It delivers an accurate inventory of IoT and OT devices on your network.

The workspace displays device counts and specific metrics for critical vulnerabilities, risk prioritization, device type classification, manufacturer distribution, critical risk breakdown, and network location. This information supports efficient risk assessment and policy enforcement across the networked physical environment.

<Callout icon="📘" theme="info">
  Note

  See [Workspaces](https://docs.axonius.com/axonius-help-docs/docs/workspaces) to learn how to generally access, navigate, and use workspaces.
</Callout>

## Products Required for this Workspace

To access and use this workspace, you must have access to **[Axonius for Healthcare](https://docs.axonius.com/axonius-help-docs/docs/axonius-for-healthcare)** .

## Adapters Required for this Workspace

To populate this workspace with data, the [Axonius Network Inspector](https://docs.axonius.com/axonius-help-docs/docs/axonius-network-inspector) adapter is required. The adapter is provided by Axonius and does not require any connection action.

## Workspace Assets and Modules

You can access the following assets directly from this workspace:

* [IoT Devices](https://docs.axonius.com/axonius-help-docs/docs/iot-devices)

<Callout icon="📘" theme="info">
  Note

  Each workspace in the Axonius platform has its own use-case-focused navigation menu on the left. The assets and modules available from this menu depend upon your access configuration.
</Callout>

## Workspace

The workspace provides charts with aggregated and normalized data about the current state of connected devices across IoT and OT environments. This includes the total quantity of IoT devices present and highlights the number of devices affected by critical security vulnerabilities.

The workspace also outlines the high-priority risks impacting the environment and breaks down the asset population by specific device type and manufacturer. The homepage features detailed metrics on the distribution of critical device risk across the network, along with a visualization of device locations on the network categorized by type.

The presented charts enable immediate awareness of asset distribution, exposure, and risk context.

<Image align="center" alt="IoT/OT Discovery workspace" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workspaces/IoT-OT_Discovery_WS_fixed.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  Clicking any chart in the workspace opens a separate page that provides further in-depth details and insights related to that chart.
</Callout>

## Use Cases this Workspace Helps You Fulfill

This workspace provides data and visualizations that help you address critical security and IT management use cases related to your IoT/OT devices.

### Prioritized Vulnerability Remediation for Critical OT Assets

In this use case, the primary objective is to direct remediation efforts toward assets that pose a high risk to operations. The security team first utilizes the **IoT Device Types** and **Manufacturers by Device Type** charts to gain visibility into the organization's OT install base from different vendors.

The security team can then run queries to identify all OT devices exhibiting critical security vulnerabilities. This list is cross-referenced with the **Top Risks** chart information and prioritized using the **Critical Device Risk Breakdown** chart score to establish a remediation program, focusing on device types and vendors with the highest systemic risk (for example: control systems over cameras).

The security team can then create and send a high-priority work order ticket, complete with full asset and vulnerability context, to the operational staff responsible for immediate patching or policy enforcement.

### Continuous OT Segmentation Policy Validation

In this use case, the security team identifies critical infrastructure and continuously verifies that it remains isolated from other systems.

The security team establishes a policy rule based on the **Network Location by Device Type** chart, prohibiting OT assets from communicating with non-OT network segments (for example, the corporate IT subnet). This is done to ensure that the OT devices are connected to their designated network sites and to confirm that there was no mistake connecting those devices to an unauthorized network.

If a connection is detected that violates this segmentation rule, the system identifies and reports the non-compliant asset, providing the context required to initiate an enforcement action for network containment.

### Automated Compliance Reporting and Asset Export

In this use case, the Governance, Risk, and Compliance (GRC) team automates the collection and delivery of audit evidence and inventory data. A scheduled report can be configured in the Axonius platform to run on a periodic basis and generate a PDF file that documents asset inventory validation.

This report includes the total count of IoT/OT assets and a breakdown from the **Manufacturers by Device Type** chart, enabling the compliance officer to verify that no unauthorized vendors or device types are present in the organization. It also validates policy adherence through segmentation checks against the **Network Location by Device Type** chart.

The team can export the full query result set of all assets as a CSV file for the Configuration Management Database (CMDB) administrator to use in a reconciliation process.