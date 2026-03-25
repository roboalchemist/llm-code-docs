# Source: https://docs.axonius.com/docs/asset-panda-create-and-update-assets.md

# Asset Panda - Create And Update Assets

**Asset Panda - Create and Update Assets** creates, updates, or creates and updates assets retrieved from the saved query supplied as a trigger (or devices that have been selected in the asset table).

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

* **Use stored credentials from Asset Panda Adapter** - Select this option to use [Asset Panda](/docs/assetpanda) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Asset Panda](/docs/assetpanda) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Asset Type** - Enter the type of asset you want to create and/or update.
* **Action Choice** - Select the Action to use: **Create**, **Create and Update**, or **Update**.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address**  - The hostname or IP address of the Asset Panda server.

  * **Password** - The password for a user account that has the permissions to perform this action.

  * **Bearer Token** - A Bearer token received from Asset Panda.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name**   - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard** to map Axonius fields to fields in Asset Panda. In this way you can transfer data found in Axonius into Asset Panda. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  NOTE

  For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Asset Panda API](https://team-asset-panda.readme.io/reference/http-status-codes).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).