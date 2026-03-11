# Source: https://docs.axonius.com/docs/update-freshservice-asset.md

# Freshservice - Update Assets

**Freshservice - Update Assets**  updates a Freshservice asset for:

* Assets returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  All Freshservice field names are case sensitive. To check a field name, fetch the asset with a *curl* command and check the RAW data in Axonius. See [Service Desk API for Developers | Freshservice](https://api.freshservice.com/#view_an_asset).
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

* **Use stored credentials from the Freshservice adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    * To use this option, you must successfully configure a [Freshservice](/docs/freshservice) adapter connection.
    * The API key used for the adapter connection must be for a user with permissions to update an asset.
  </Callout>

* **Map Axonius fields to Freshservice fields** - This field is only for mapping **mandatory** fields, such as the **name** field.

  <Callout icon="📘" theme="info">
    Note

    To map custom fields, use the **Map Axonius fields to Freshservice *type* fields** field under [**Additional Fields**](/docs/create-freshservice-asset#additional-fields).
  </Callout>

  Use the **Field Mapping Wizard** to map Axonius fields to fields in Freshservice. This allows you to transfer data found in Axonius into Freshservice. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

  <Callout icon="📘" theme="info">
    Note

    For details, see [Axonius to CMDB Field Mapping](/docs/axonius-to-cmdb-field-mapping).
  </Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Freshservice domain** - The hostname or IP address of the Freshservice server.

  * **API Key** – Specify the API Key provided by Freshservice.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Throttle API Requests** -  Select this option to only use 90% of the API total rate limit bandwidth. For example: If a customer has 3000 total API calls allowed per hour, axonius will only produce 2700 calls, and leave the remaining 10% available.
* **Fresh Service Workspace ID** - Enter the Freshservice workspace ID in which to place the assets.
* **Do not map default Axonius fields** - Select whether to map the set of default Axonius fields to the Freshservice asset. For details, see [Default Field Mapping](/docs/default-field-mapping).
* **Map Axonius fields to Freshservice type fields** - Use the **Field Mapping Wizard** to map Axonius fields to type fields in Freshservice. This field is used to map custom fields defined in Freshservice and MUST be typed exactly as they appear in Freshservice.
* **Adjust Date fields to ISO-8601 format** - Select to have dates adjusted to the ISO-8601 format.
* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Additional fields to use by querying the API** - Use these additional fields populated by querying the API.
* **Query from API endpoint**
  * **API Endpoint** - Enter the API endpoint to query.
  * **URL Parameters** - Enter any URL parameters.
* **Payload mapping** -
  * **Payload Key for create/update requests** - Enter the payload key.
  * **Key from the response** - Enter the key from the response.
* **Axonius to URL Parameters mapping** - See [Default Field Mapping](https://docs.axonius.com/axonius-help-docs/docs/default-field-mapping).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).