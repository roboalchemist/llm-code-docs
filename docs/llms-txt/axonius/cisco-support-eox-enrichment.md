# Source: https://docs.axonius.com/docs/cisco-support-eox-enrichment.md

# Cisco Support - Enrich Cisco Devices OS with EOL/EOS

**Cisco Support - Enrich Cisco Devices OS with EOL/EOS** enriches assets with End of Life/End of Service data from Cisco Support for:

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

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

* **Host Name or IP Address** - The hostname or IP address of the Cisco Support server.

* **Client ID** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

* **Client Secret** *(required)* - A Client Secret Key associated with a user account that has the Required Permissions to perform this action.

## Additional Settings

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

## APIs

Axonius uses the [Cisco Support API](https://developer.cisco.com/docs/support-apis/eox/#introduction).

## Required Ports

Axonius must be able to communicate via the following ports:

* 443

## Required Permissions

The user must retrieve the [**Client ID** and **Client Secret**](#parameters) from the [Cisco Support](https://developer.cisco.com/docs/support-apis/authentication/).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).