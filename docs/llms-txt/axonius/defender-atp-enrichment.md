# Source: https://docs.axonius.com/docs/defender-atp-enrichment.md

# Microsoft Defender - Enrich Devices with MDE Client Analyzer Results

**Microsoft Defender - Enrich Devices with MDE Client Analyzer Results** enriches devices with MDE Client Analyzer data for:

* Assets returned by the selected query or assets selected on the relevant asset page.
  This action connects to the target device using WinRM/WSMAN connection, and downloads the HTM(L) file using PowerShell. Then, it parses the HTM(L) file and uses it to enrich the device with the extracted data.
  The PowerShell script used by this action is as follows:
  `Get-Contents -Name "path\to\file.zip"`

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Username** - The username to authenticate with for the WinRM connection.
* **Password** - The password to authenticate with for the WinRM connection.
* **File Path** - The path to the MDE Client Analyzer results. Enter either a .HTM(L) or .ZIP file path.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management) guide.

## Required Ports

Axonius must be able to communicate via the following ports:

* 5985 (default)
* 5986

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.
To configure permissions for WinRm connection, refer to [Installation and configuration for Windows Remote Management](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management).

## Version Matrix

This Enforcement Action was tested only with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version             | Supported | Notes |
| ------------------- | --------- | ----- |
| Windows Server 2016 | Yes       |       |
| Windows Server 2019 | Yes       |       |
| Windows Server 2022 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).