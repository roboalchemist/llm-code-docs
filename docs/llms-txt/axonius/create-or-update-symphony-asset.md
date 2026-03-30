# Source: https://docs.axonius.com/docs/create-or-update-symphony-asset.md

# SymphonyAI Summit - Create or Update Assets

**SymphonyAI Summit - Create or Update Assets** creates and/or updates assets in SymphonyAI Summit for:

* Assets that match the parameters of the selected saved query, and match the Enforcement Action Conditions, if defined, or assets selected on the relevant asset page.

Depending on the action selected, assets not in SymphonyAI Summit will be created and existing SymphonyAI Summit assets will be updated.

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

* **Use stored credentials from the SymphonyAI Summit adapter** - Select this option to use SymphonyAI Summit connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action. When not enabled, configure the fields described in [Connection Parameters](/docs/create-or-update-symphony-asset#connection-parameters).

## Required Fields

* **Action Choice** - Select one of the following:
  * **Create** - Create SymphonyAI Summit assets for the assets returned by the query.
  * **Update** - Update existing SymphonyAI Summit assets returned by the query.
  * **Create and Update** - Create and update SymphonyAI Summit assets for the assets returned by the query. Existing SymphonyAI Summit assets will be updated. Assets not already in SymphonyAI Summit will be created.
* **Symphony Instance** - The name of the Symphony instance.
* **Category ID** - The ID of the asset category.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname of the SymphonyAI Summit search head.

  * **API Key** - The API key for the SymphonyAI account.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

## APIs

Axonius uses this SDK:

* [SymphonyAI Summit API](https://docs.symphonysummitai.com/display/TAH/Update+CIs+in+CMDB)