# Source: https://docs.axonius.com/docs/enrich-device-data-with-dns-records.md

# WMI - Enrich Devices with DNS Records

**WMI - Enrich Devices with DNS Records** enriches DNS records for:

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

* **DNS Server** - Enter the DNS server you want to get records from.

* **User Name** and **Password** - The credentials for a user account that has the permissions to run a WMI scan and access the DNS server.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Query A, CNAME, PTR and check consistency** - When enabled, the action will query the A, CNAME, PTR records for the query devices and check if the A-PTR values are consistent.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Microsoft DNS WMI Provider API](https://learn.microsoft.com/en-us/windows/win32/dns/dns-wmi-classes).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* The permission to run Powershell commands, for example, `Get-WmiObject`.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).