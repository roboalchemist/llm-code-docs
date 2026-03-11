# Source: https://docs.axonius.com/docs/add-ips-to-tenablesc-asset.md

# Tenable.sc (SecurityCenter) - Add or Remove IP Addresses to/from Assets

**Tenable.sc (SecurityCenter) - Add or Remove IP Addresses to/from Assets** adds an IP address to an existing Tenable.sc asset; or removes an IP address from an existing Tenable.sc asset; or creates a new Tenable.sc asset for:

* Assets returned by the selected query or assets selected on the relevant asset page.

Tenable.sc assets are lists of devices (e.g., laptops, servers, tablets, phones, etc.) within a Tenable.sc organization. Assets can be shared with one or more users based on local security policy requirements and may be accessed by multiple IP addresses. For more details about Tenable.sc assets, see [Tenable.sc online documentation](https://docs.tenable.com/vulnerability-management/Content/Explore/assets-intro.htm).

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

* **Use stored credentials from the Tenable.sc Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the Select Adapter Connection drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Tenable.sc](/docs/tenablesc-formerly-securitycenter) adapter connection.
  </Callout>

* **Asset name** - Specify the Tenable.sc asset name to be updated/created.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Tenable.sc domain** -  The IP address or hostname of your Tenable.sc management server.

  * **User Name** and **Password** - The user name and password for an account in Tenable.sc that has the “Security Manager” role, with access to all the required repositories.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Do not user other connections as fallback** - Prevents the use of other adapter connections and restricts the connection to the one selected in **Use stored credentials from the Tenable.sc adapter**.
* **Create new asset** - Select to create a new asset in Tenable.sc.
  * If enabled, Axonius will create a new asset in Tenable.sc.
  * If disabled, Axonius will update the specified asset name in Tenable.sc.
* **Use private IP addresses** - Select to add private IP addresses to Tenable.sc.
* **Use public IP addresses** - Select to add public IP addresses to Tenable.sc.
* **Exclude IPv6 addresses** - Select to add IPv6 addresses to the Tenable.sc asset.
  * If enabled, Axonius will add only IPv4 addresses to Tenable.sc.
  * If disabled, Axonius will add both IPv4 and IPv6 addresses to Tenable.sc.
* **Override current IP address list** - Select to override the current Tenable.sc asset IP list.
  * If enabled, Axonius will override the current Tenable.sc asset IP list.
  * If disabled, Axonius will add IP addresses to the existing Tenable.sc asset IP list.
* **Remove current IP address list** - Select to remove the current Tenable.sc asset IP list from the asset.
* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded.
  * If supplied, Axonius will not add to Tenable.sc IP addresses in the IP range of the specified CIDRs.
  * If not supplied Axonius will add to Tenable.sc IP addresses in any IP range.
* **Source Adapter** - Specify an adapter name as it appears in Axonius to send specific adapter IP data.
* **Use only AWS primary private IP** - Select to only use the AWS primary private IP address.
* **Create a new scan with the asset** - Select to create a new scan with the asset (the scan name will be the same as the asset name).
* **Policy ID for the new scan** - Adds a policy to the scan that is created.
* **Succeed action even if no IPs were found** - Select to prevent the action from failing when there is no data to update.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).