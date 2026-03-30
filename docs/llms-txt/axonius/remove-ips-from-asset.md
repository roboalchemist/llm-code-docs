# Source: https://docs.axonius.com/docs/remove-ips-from-asset.md

# Rapid7 - Remove IP Addresses from Asset

**Rapid7 - Remove IP Addresses from Asset** removes IP addresses from an existing Rapid7 InsightVM asset for:

* Assets returned by the selected query or assets selected on the relevant asset page.

A Rapid7 InsightVM site is a collection of assets that are targeted for a scan.

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

* **Use stored credentials from the Rapid7 adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Rapid7 InsightVM](/docs/rapid7-insightvm) adapter connection.
  </Callout>

* **Source Adapter** - Specify an adapter name as it appears in Axonius (as in the Axonius URL) in order to send specific adapter IP data.

* **Exclude IPv6 addresses** - This option must be selected. It will add IPv6 addresses to the Rapid7 InsightVM site.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host name** - The hostname of the Rapid7 InsightVM server.

  * **Port** - Use port 3780.

  * **User name** and **Password** - The credentials for a user account that has the permissions to update a site.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Use public IP addresses** - Select to add public IP addresses to Rapid7 InsightVM.
* **Use private IP addresses** - Select to add private IP addresses to a Rapid7 InsightVM site.
* **CIDRs exclude list** - Specify a comma-separated list of CIDRs to be excluded.
  * If supplied, Axonius will not add to the Rapid7 InsightVM site IP addresses in the IP range of the specified CIDRs.
* **Override site IPs** - Select to overwrite the IP addresses of the Rapid7 InsightVM site.
* **Add Hostnames names to scan** - Select whether to send the hostname name as well as the IP address to the Rapid7 InsightVM site.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [InsightVM API (v3)](https://help.rapid7.com/insightvm/en-us/api/index.html#operation/createAsset) API.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).