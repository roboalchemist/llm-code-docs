# Source: https://docs.axonius.com/docs/enrich-device-data-with-lenovo.md

# Lenovo - Enrich Asset Data

**Lenovo - Enrich Asset Data** enriches devices with Lenovo warranty information at the device level for:

* Assets returned by the selected query or assets selected on the relevant asset page.

You can then query for devices soon to be out of warranty. This Enforcement Action pulls Lenovo data from the Lenovo support database to match device serial numbers (SN) as unique device IDs.

<Callout icon="💡" theme="warn">
  Note

  Although you might see an adapter on your system, all configuration necessary is performed using this Enforcement Action.
</Callout>

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

* **Host Name or IP Address** *(default: `https://SupportAPI.lenovo.com`)* - The host name or IP address of the Lenovo support database.

* **Client ID** - Enter your client ID token.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
* **Use Serial Number as Name** - Select this option to use the device’s serial number as the name  instead the given ‘name’ field from the API.
* **Avoid parsing Asset Name** - When selected, the *Asset Name* and *Host Name* fields in Lenovo will be blank.

## APIs

Axonius use the [eSupport WebAPI](https://supportapi.lenovo.com/Documentation/Index.html) API.

## Required Permissions

The values supplied in **Host Name or IP Address** must have the following permissions.

* WebAPI.Content
* WebAPI.Warranty (required to view warranty information)

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).