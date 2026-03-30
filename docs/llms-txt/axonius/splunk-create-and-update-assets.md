# Source: https://docs.axonius.com/docs/splunk-create-and-update-assets.md

# Splunk - Create and Update Assets

**Splunk - Create and Update Assets** creates and/or updates assets in Splunk for:

* Assets returned by the selected query or assets selected on the relevant asset page.

Depending on the action selected, assets not in Splunk will be created and existing Splunk assets will be updated.

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

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Splunk adapter** - Select this option to choose which [Splunk](/docs/splunk) connected adapter credentials to use.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Splunk](/docs/splunk) adapter connection.
  </Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name** - The hostname of the Splunk search head.

  * **Port** - Specify the port of the Splunk system. It is recommended to use TCP port 8089. For more details, see [Splunk Docs - Securing Splunk Enterprise](https://docs.splunk.com/Documentation/Splunk/8.0.3/Security/SecureSplunkonyournetwork).

  * **Protocol** *(rdefault: HTTPS)* - Select between HTTP and HTTPS protocols when using that specific adapter connection.

  * **User Name** and **Password** - The user name and password for an account that has read access to the API.

  <Callout icon="📘" theme="info">
    Note

    You must use one of the following:

    * **API Token** or both **User Name** and **Password** together.
  </Callout>

  * **API Token** - API token can be used instead of user name and password.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

* **Action Choice** - Select one of the following:
  * **Create** - Create Splunk assets for the assets returned by the query.
  * **Update** - Update existing Splunk assets returned by the query.
  * **Create and Update** - Create and update Splunk assets for the assets returned by the query. Existing Splunk assets will be updated. Assets not already in Splunk will be created.

* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

<Callout icon="📘" theme="info">
  Note

  If the Vendor field (table column) does not currently exist within the collection, Axonius will add the field value(s) specified as a new column(s) in the KV Store Collection. If the field already exists, Axonius will update or add the mapped value.
</Callout>

* **KV Store Collection Name** - The name of the KV store collection in which to create and update the assets.

  <Callout icon="📘" theme="info">
    Notes

    * If a KV Store Collection name is not provided, the default name will be listed as “axonius”.
    * The KV Store stores your data as key-value pairs in collections. Collections are the containers for your data, similar to a database table. Collections exist within the context of a given app.
    * Fields correspond to key names, similar to the columns in a database table. Fields contain the values of your data in JSON format.
  </Callout>

* **Mapped Axonius field to Splunk ID (Required field for Update Assets)** - Select fields fetched from the Splunk adapter to map their values to Splunk IDs. Note that when you select **Update** for **Action Choice**, this field is mandatory.

## APIs

Axonius uses the [Splunk API](https://dev.splunk.com/enterprise/docs/devtools/python/sdk-python).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Permission to create and update assets.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).