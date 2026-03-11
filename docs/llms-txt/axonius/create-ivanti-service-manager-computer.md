# Source: https://docs.axonius.com/docs/create-ivanti-service-manager-computer.md

# Ivanti - Create Assets

**Ivanti - Create Assets** creates an asset in Ivanti Service Manager for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

When this Enforcement Action creates an asset in Ivanti, it is populated with a set of [default attributes](/docs/default-field-mapping).

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

* **Use stored credentials from the Ivanti Service Manager adapter** - Select this option to use the first connected Ivanti Service Manager adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      * To use this option, you must successfully configure a [Ivanti Service Manager](/docs/ivanti-service-manager) adapter connection.
      * The API key used for the adapter connection must be user with permissions to create new asset.
    </Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Business Object** - The type of object to create. Select an item from the list or add a new one.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Ivanti Service Manager domain** - The hostname or IP address of the Ivanti Service Manager server.

  * **API Key** - REST API key created for a tenant that is used for authorizing REST API endpoints. For details on creating a REST API key from the Ivanti Service Manager configuration console, see [Ivanti Service Manager - Using the REST API Key](https://help.ivanti.com/ht/help/en_US/ISM/2019.2/admin/Content/Configure/API/Using-REST-API-Key.htm#CreatingRESTAPIKey).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Enforce software list update** - Forces the list of software to be updated.
* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Use first IP address only** - When enabled, only the device's first IP address will be added to the Ivanti Service Manager asset. Otherwise, all IP address will be added.
* **IP addresses delimiter** *(default: /)* - Specify the delimiter to separate between multiple IP addresses added to the Ivanti Service Manager asset.
* **Use first MAC address only** - When enabled, only the device's first MAC address will be added to the Ivanti Service Manager asset. Otherwise, all the device's MAC addresses will be added.
* **MAC addresses delimiter** *(default: /)* - When supplied, the specified delimiter will be used to separate between multiple MAC addresses added to the Ivanti Service Manager asset. When no delimiter is supplied, the default delimiter will be used.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).