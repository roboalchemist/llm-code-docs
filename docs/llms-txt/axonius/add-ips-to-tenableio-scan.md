# Source: https://docs.axonius.com/docs/add-ips-to-tenableio-scan.md

# Tenable Vulnerability Management - Add IP Addresses to Scan

**Tenable Vulnerability Management - Add IP Addresses to Scan** adds the IP addresses to an existing Tenable Vulnerability Management scan for:

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

## APIs

To successfully run this Enforcement Set, the following API endpoints and permissions are required:

**API Endpoints**

* GET /scanners
* GET /scans
* GET /scans/\{scan\_id}
* PUT /scans/\{scan\_id}

**Permissions:**

* Scan Manager \[40] user role
* Can Edit \[64] scan permissions

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Tenable Vulnerability Management Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the Select Adapter Connection drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Tenable Vulnerability Management](/docs/tenableio) adapter connection.
  </Callout>

* **Scan name** - Specify the Tenable Vulnerability Management scan name to be updated.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Tenable Vulnerability Management domain** -  The IP address or hostname of your Tenable Vulnerability Management management server.

  * **Access API key** and **Secret API key** - These values must be created in the Tenable Vulnerability Management console. To generate an API key in the Tenable Vulnerability Management console, see [Tenable Vulnerability Management - Generate an API Key](https://developer.tenable.com/docs/api-access).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **IPs to add (overrides other IP selection options)** - Provide IP addresses to add to the scan. They will be added regardless of other IP selection settings.
* **Do not use network interfaces IPs** - This option should be used only when **Use public IP addresses** is selected. The Enforcement Action will only add the IP addresses from Public IPs and not from network interfaces. When using only the option **Use public IP addresses**, a combination of public IPs from network interfaces and the public IP field are added to the scan.
* **Use public IP addresses** - Select to add public IP addresses. This option is useful when needing to scan IP addresses from cloud providers, like AWS.
* **Use private IP addresses** - Select to only add private IP addresses.
* **Use hostnames** - Hostnames from query results will be sent to scan in Tenable Vulnerability Management.
* **Exclude IPv6 addresses** - When enabled, Axonius will add only IPv4 addresses to Tenable Vulnerability Management and not IPv6 addresses. Otherwise, both IPv4 and IPv6 addresses will be added.
* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded.
* **Succeed action even if no IPs were found** - Select to prevent the action from failing when there is no data to update.
* **Override current IP address list** - When enabled, Axonius will override completely the IP addresses that already exist in the scan, effectively replacing outdated or irrelevant entries; when disabled, Axonius will add the IP addresses to the ones that are already in the scan.
* **Remove current IP address list** - When enabled, Axonius will remove the IP addresses from the scan.
  * When enabling both **Override current IP address list** and **Remove current IP address list** - the latter takes precedence.
* **Scan schedule** - When enabled, select a **Frequency** and then configure the schedule options.
* **Auto route scan targets to scanner groups based on their configured scan routes** - When selected, adds `'target_network_uuid': '00000000-0000-0000-0000-000000000000'` and `'scanner_id': 'AUTO-ROUTED' `to the request so that both fields are included.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).