# Source: https://docs.axonius.com/docs/create-snipeit-asset.md

# SNIPE-IT - Create Asset

**SNIPE-IT - Create Asset** creates or updates assets in SNIPE-IT for:

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

* **Use stored credentials from the SNIPE-IT adapter** - Select this option to use (the first) SNIPE-IT connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Set.

* **Status ID** - The ID of the related status label.
* **Model ID** - The ID of the related asset model.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  If **Use stored credentials from the SNIPE-IT adapter**  is not enabled, these fields are required.

  * **SNIPE-IT Domain** - The domain of the SNIPE-IT server.

  * **API Key** - In order to use the API, you’ll need to generate an API key that will be associated with your user. Generating API Tokens

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
</Callout>

* **Action Choice** - Select the action to perform:
  * **Create** - Only create new assets and ignore existing ones.
  * **Create and Update** - Create new assets and update existing ones.
  * **Update** - Only update existing assets and ignore new ones.
* **Exclude connections** - Assets from the selected connections will not be included in the query results. You can select more than one.
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Asset Tag** - The asset tag of the asset being created or updated. If auto-incrementing is enabled in SNIPE-IT settings, this is not required and will be automatically generated.
* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [SNIPE-IT](https://snipe-it.readme.io/reference/hardware-create) API.

## Required Permissions

Personal Access Tokens reflect the permissions of the user the token is associated with. For example, if a user is only allowed to view assets but not update them, any API requests made using that user’s Personal Access Token will return an Unauthorized error if they attempt to perform an action their regular logged-in user isn’t permitted to do, such as updating an asset.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).