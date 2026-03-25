# Source: https://docs.axonius.com/docs/netbox-create-or-update-assets.md

# Netbox - Create or Update Assets

**Netbox - Create or Update Assets** creates a Netbox Asset, or updates a Netbox Asset for:

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

* **Use stored credentials from the Netbox Adapter** - Select this option to use [Netbox](/docs/netbox) connected adapter credentials. By default, the first connection is selected.

  * When you select this option, the Select Adapter Connection drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Netbox](/docs/netbox) adapter connection.
  </Callout>

* **Create Object Type** - Select the type of asset to create or update.

* **Action Choice** - Select the action to perform:
  * **Create** - Only create new assets and ignore existing ones.
  * **Create and Update** - Create new assets and update existing ones.
  * **Update** - Only update existing assets and ignore new ones.

* **Content type** - Add a Content Type field in the format ..

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **NetBox Domain** - The hostname of the NetBox server.

  * **Authentication token** - Enter the NIST controls used by the company.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Exclude connections** -Enter connections to exclude from asset queries.
</Callout>

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard** to map Axonius fields to fields in Netbox. In this way you can transfer data found in Axonius into Netbox. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

  <Callout icon="📘" theme="info">
    Note

    For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).
  </Callout>

## APIs

Axonius uses the [NetBox REST API](https://demo.netbox.dev/static/docs/integrations/rest-api/).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).