# Source: https://docs.axonius.com/docs/create-ca-cmdb-asset.md

# CA Service Management - Create Assets

**CA Service Management - Create Assets**  (Create CA CMDB Asset) creates an asset in CA Service Management for:

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

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Use stored credentials from the CA CMDB adapter** - Select this option to use the first connected ServiceNow adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [CA Service Management](/docs/ca-service-management) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **CA CMDB domain** - The hostname or IP address of the CA Service Management server.

  * **User name** and **Password** - To connect to CA, you will need to create a user with action privileges.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Serial number** - The serial number of the asset.
* **Family type GRC number** - A unique identification number for this Family type.
* **Device name** - The name of the device.
* **IP address** - The IP address of the device.
* **Axonius to CA CAMDB field mapping** - Use the **Field Mapping Wizard** to map Axonius fields to fields in CA CMDB. This allows you to transfer data found in Axonius into CA CMDB. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  NOTE

  For details, see [Axonius to CMDB Field Mapping](/docs/axonius-to-cmdb-field-mapping).
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).