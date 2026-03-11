# Source: https://docs.axonius.com/docs/deploy-package-in-sccm.md

# Microsoft MECM - Deploy Package to Devices

**Microsoft MECM - Deploy Package to Devices** deploys packages for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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
* **Host** -  A host that has Configuration Manager Cmdlets available to run via PowerShell.
* **Username** - The username used to run the PowerShell commands.
* **Password** - The username's password.
* **Site** - The Configuration Manager Site in which the Enforcement Action will run.
* **Package ID** - The ID of the deployed package.
* **Program Name** - The name of the deployed program, which is a part of the package.
* **Collection Name** -  The name of the Axonius collection where all devices receiving the deployment will be stored. You first need to create such collection in Configuration Manager and make it exclusive for each Enforcement Action. For example, if you create two **Deploy Package to Devices** Enforcement Actions, each one of them requires a different collection name. To learn more, see [ Creating Collections](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/collections/create-collections).
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses [Microsoft's Configuration Manager API](https://learn.microsoft.com/en-us/powershell/module/configurationmanager/?view=sccm-ps).

## Required Ports

Axonius must be able to communicate via the following ports:

* 5986

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Permission to run the following Cmdlets in PowerShell:
  * New-CMPackageDeployment
  * Add-CMDeviceCollectionDirectMembershipRule
  * Get-CMDevice
  * Get-CMDeviceCollection
  * Remove-CMDeviceCollectionDirectMembershipRule
  * Import-Module
  * Set-Location

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).