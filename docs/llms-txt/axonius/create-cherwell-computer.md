# Source: https://docs.axonius.com/docs/create-cherwell-computer.md

# Cherwell - Create Assets

**Cherwell - Create Assets** (Create Cherwell Asset) creates an asset in Cherwell for:

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

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Use stored credentials from the Cherwell adapter** - Select this option to use the first connected Cherwell adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      * To use this option, you must successfully configure a [Cherwell IT Service Management](/docs/cherwell) adapter connection.
      * The user name and the password used for the adapter connection must be user with permissions to create new incidents.
    </Callout>

* **Business Object ID** *(default: 9343f8800bd7ce14f0bf0a402d9d38be1a25069644)* - Specify the Cherwell Business Object ID to be associated with the created asset in Cherwell.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Cherwell domain** - The hostname or IP address of the Cherwell server.

  * **User name** and **Password** - The user name and the password of a user account that has permissions to read and to modify devices.

  * **Client ID** - Enter the client ID created in the CSM Administrator. For details, see [Cherwell - Obtaining API Client IDs](https://help.cherwell.com/bundle/cherwell_rest_api_940_help_only/page/oxy_ex-1/content/system_administration/rest_api/csm_rest_obtaining_client_ids.html#ObtainingApiClientIds#OpenSwagger#ObtainingApiClientIds#OpenSwagger).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Create devices in Axonius** - Devices are created in Axonius as well as in Cherwell.

* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Do not map default Axonius fields** - When selected, the set of default Axonius fields are mapped to the Cherwell asset. For details, see [Default Field Mapping](/docs/default-field-mapping).

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Use first IP address only** - When selected, adds the first IP address to the Cherwell asset.

* **IP addresses delimiter** *(default: /)* - Specify the delimiter to separate between multiple IP addresses added to the Cherwell asset.

* **Use first MAC address only** - When selected, adds the first MAC address to the Cherwell asset. Otherwise, all the device's MAC addresses will be added to the Cherwell asset.

* **MAC addresses delimiter** *(default: /)* - Specify the delimiter to separate between multiple MAC addresses added to the Cherwell asset.

* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded.

* **CIDR include list** - Specify a comma-separated list of CIDRs to be included.

* **Number of parallel requests** *(default 10)* - Specify the number of machines that can be created in parallel.

* **Sleep 1 second every token request** - Select this option to wait before sending authentication tokens.

* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).