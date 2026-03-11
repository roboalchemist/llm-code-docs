# Source: https://docs.axonius.com/docs/delete-device-in-sccm.md

# Microsoft MECM - Delete Devices

**Microsoft MECM - Delete Devices** deletes assets returned by the selected query or selected on the relevant asset page from Microsoft MECM.

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

* **Host** - The hostname or IP address of the host that has Configuration Manager cmdlets available to run via PowerShell.
  * <Callout icon="📘" theme="info">
      Note

      This action requires the WinRM service enabled in the hostname.
    </Callout>

* **Username** and **Password** - The credentials of a user that has the [required permissions](https://docs.axonius.com/delete-device-in-sccm#/required-permissions) to run this action.

* **Site Code** - The Configuration Manager site code in which the Enforcement Action will run.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Site Server** - The SCCM server hostname. When this field is provided, the Enforcement Action assumes that double-hop will occur. In this scenario, the Axonius system connects to the device configured in the Host and then to the SCCM server configured in the Site Server field. When this field is empty, the Enforcement Action assumes that a connection will be made directly to the SCCM server, and so the Host field is parsed as the SCCM server h  ostname.
  * **Example 1:** The Host field value is `proxy_server.com` and the Site Server field value is `SCCM_server.com`. In this case, The Enforcement Action will connect to `proxy_server.com` and from this device it will connect to `SCCM_server.com`.
  * **Example 1**: The Host field value is `SCCM_server.com` and the Site Server field value is empty. In this case, The Enforcement Action will connect directly to `SCCM_server.com`.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [ConfigurationManager](https://learn.microsoft.com/en-us/powershell/module/configurationmanager/?view=sccm-ps) API.

## Required Ports

Axonius must be able to communicate via the following ports:

* 5986

## Required Permissions

The stored credentials must have permission to run the following cmdlets in PowerShell:

* Remove-CMDevice
* Import-Module
* Set-Location
* New-PSDrive

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).