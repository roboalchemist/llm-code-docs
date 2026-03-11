# Source: https://docs.axonius.com/docs/remove-subdomain-from-dns-made-easy.md

# DNS Made Easy - Remove Subdomain

**DNS Made Easy - Remove Subdomain** removes subdomain entry from DNS Made Easy for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the DNS Made Easy adapter** *(required, default: False)* - Select this option to use the first connected DNS Made Easy adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure a [DNS Made Easy](/docs/dns-made-easy) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Host Name or IP Address** *(required, default: api.dnsmadeeasy.com)* - The hostname or IP address of the DNS Made Easy server.

<Callout icon="📘" theme="info">
  NOTE

  If **Use stored credentials from the DNS Made Easy adapter** is disabled, this field is required.
</Callout>

* **API Key** and **Secret Key** *(optional, default: empty)* - An API Key and Secret Key pair associated with a user account that has permissions to perform this action.

<Callout icon="📘" theme="info">
  NOTE

  If **Use stored credentials from the DNS Made Easy adapter** is disabled, this fields are required.
</Callout>

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
* **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

## APIs

Axonius uses the [DNS Made Easy API](https://api-docs.dnsmadeeasy.com/?version=latest).

## Required Permissions

The value supplied in [API Key and Secret Key](#connection-settings) must have update and delete access to subdomain records.

To generate an API Key and Secret Key pair, see [DNS Made Easy adapter - Required Permissions](/docs/dns-made-easy#required-permissions).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).