# Source: https://docs.axonius.com/docs/medical-device-discovery-workspace.md

# Medical Devices Management Workspace

The **Medical Device Management** workspace consolidates and standardizes data from various sources to create a comprehensive, unified record for all connected medical devices (IoMT) on the network. It delivers clinical engineering (HTM/Biomed) and security teams a clear inventory of all assets.

The workspace shows counts and specific measurements for the number of medical devices, critical security flaws, risk levels, device categories, manufacturers, risk breakdown for critical devices, and network placement.

By providing these metrics through passive monitoring that avoids interfering with clinical operations, the workspace enables you to focus remediation efforts on the most vulnerable and high-risk equipment, thereby maintaining patient care continuity while improving the security posture.

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

* [IoMT Devices](https://docs.axonius.com/axonius-help-docs/docs/iomt-devices)

<Callout icon="📘" theme="info">
  Note

  Each workspace in the Axonius platform has its own use-case-focused navigation menu on the left. The assets and modules available from this menu depend upon your access configuration.
</Callout>

## Workspace

The workspace provides charts with aggregated and normalized data exclusively on connected medical devices (IoMT) across the network. This includes the total number of medical devices present and highlights the quantity of devices affected by critical security vulnerabilities.

The workspace also outlines the high-priority risks impacting the medical devices and breaks down the asset population by specific device type and device manufacturer. It also features detailed metrics on the distribution of critical device risk across the network, along with a visualization of network locations (which function as device locations, such as VLAN or subnet) categorized by type.

The presented charts enable immediate awareness of medical asset distribution, exposure, and risk context, aiding clinical engineering and security teams.

<Image align="center" alt="Medical Device Management workspace" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workspaces/Medical_Device_Management_WS.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  Clicking any chart in the workspace opens a separate page that provides further in-depth details and insights related to that chart.
</Callout>

## Use Cases this Workspace Helps You Fulfill

This workspace provides data and visualizations that help you address critical security and IT management use cases related to your IoMT devices.

### Prioritizing Vulnerability Handling by Clinical Risk

In this use case, HTM/Biomed and security teams collaborate to prioritize remediation efforts where security flaws intersect with patient safety. They can identify all medical devices with high scores in the **Number of Devices with Critical Vulnerabilities** chart. Proper handling is determined by cross-referencing the medical device type and its network location (for example, Intensive Care Unit).

By focusing on high-risk clinical equipment, as defined by the **Critical Device Risk Breakdown** chart, teams ensure that critical functions are secured first, while minimizing disruptions to patient care.

### Validation of Network Segmentation for High-Risk Devices

In this use case, the HTM/Biomed team continuously monitors and validates that medical devices are not connected to network segments that violate organizational policy (for example, a medical device connected to the guest network).

The team verifies that high-risk medical devices are strictly confined to their secure segmentation zones by monitoring the **Network Location by Device Type** chart.

If a policy violation is detected (for example, a device connecting to an unsecured VLAN), the system identifies and reports the non-compliant asset, providing the context required to initiate an enforcement action for containment.

### Managing Maintenance Contracts with Medical Device Manufacturers

In this use case, the HTM/Biomed team leverages device-specific risk data to support negotiations with manufacturers or third parties for maintenance contracts.

The team utilizes the visibility provided by the **Device Manufacturers** chart and the number of exposed devices from the **Number of Devices with Critical Vulnerabilities** chart to determine the scope of required maintenance work, encompassing both operational and security perspectives.

By analyzing the frequency of critical vulnerabilities and the install base of a primary vendor, the team can request that contract terms include specific risk handling and security mitigation actions for those devices.

This process ensures resources are focused on the most critical maintenance requirements based on documented vendor exposure.