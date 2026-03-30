# Source: https://docs.axonius.com/docs/wmi-create-or-delete-dns-records.md

# WMI - Create or Delete DNS Records

**WMI - Create or Delete DNS Records** creates or deletes DNS records (A, CNAME, or PTR) in a Microsoft DNS Server for:

* Assets returned by the selected query or assets selected on the relevant asset page.

This enforcement action allows you to manage DNS records in a Microsoft DNS Server by creating or deleting A, CNAME, or PTR records. The action uses the DnsServer PowerShell module to interact with the DNS server through WinRM (Windows Remote Management) over a secure HTTPS connection.

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **DNS Server** - The DNS Server hostname or IP address where records will be created or deleted.

* **Username** - The username for authenticating to the DNS server.

* **Password** - The password for the specified username.

* **Record Type** - Select the type of DNS record to create or delete: A, CNAME, or PTR.

* **Forward Zone** - The forward zone in which to create or delete the record.

* **Action** - Select whether to Create or Delete the DNS record.

* **Owner Name** - The key value in the record. For example, in an A record `example.com → 1.1.1.1`, `example.com` is the Owner Name.

* **Resource Data** - The data value in the record. For example, in an A record `example.com → 1.1.1.1`, `1.1.1.1` is the Resource Data.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [DnsServer PowerShell module](https://learn.microsoft.com/en-us/powershell/module/dnsserver/) to interact with Microsoft DNS Server.

The following PowerShell commands are used:

* `Add-DnsServerResourceRecordA`
* `Add-DnsServerResourceRecordCName`
* `Get-DnsServer`
* `Get-DnsServerResourceRecord`
* `Remove-DnsServerResourceRecord`

## Required Ports

Axonius must be able to communicate via the following ports:

* Port 5986 (WinRM service must be enabled on the DNS Server for secure HTTPS communication)

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Permission to run the `Add-DnsServerResourceRecordA`, `Add-DnsServerResourceRecordCName`, `Get-DnsServer`, `Get-DnsServerResourceRecord`, and `Remove-DnsServerResourceRecord` PowerShell commands.
* User must be a member of the **DNSAdmins** group.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).