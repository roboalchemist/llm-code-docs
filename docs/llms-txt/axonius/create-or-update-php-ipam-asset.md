# Source: https://docs.axonius.com/docs/create-or-update-php-ipam-asset.md

# phpIPAM - Create or Update Assets

**phpIPAM - Create or Update Assets** creates and/or updates assets in phpIPAM for each asset that matches the parameters of the selected saved query, and the other Enforcement Action settings or the assets selected on the relevant asset page.

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

* **Use stored credentials from  phpIPAM adapter** - Select this option to use the first phpIPAM connected adapter credentials.[SAS Concur](/docs/sap-concur)
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Action.

* **Action Choice** - Select the action to perform:
  * **Create** - Creates assets that don't already exist. Existing assets are ignored.
  * **Update** - Updates existing assets. Information for new assets is ignored.
  * **Create and Update** - Creates assets that don't already exist and updates existing assets.
* **Controller** - Specify the phpIPAM module used to create/update the asset.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

<Callout icon="💡" theme="warn">
  ### Connection Parameters

  If **Use stored credentials from the Salesforce Adapter** is disabled, these fields are required:

  * **phpIPAM Host Name** - The domain of the phpIPAM server.

  * **Application ID** - The phpIPAM ID used to log in and create or update assets.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

## Permissions

The credentials used to connect to phpIPAM must have permissions to create and update assets.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).