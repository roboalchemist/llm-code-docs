# Source: https://docs.axonius.com/docs/update-servicenow-computer.md

# ServiceNow - Update Assets

**ServiceNow - Update Assets** updates device details in ServiceNow for:

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

* **Use stored credentials from the [ServiceNow](/docs/servicenow) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note:

    To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
  </Callout>

## Additional Fields

These fields are optional.

<br />

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **ServiceNow Domain** - The full URL for your ServiceNow instance.

  * **User Name** and **Password** - To connect to ServiceNow, you need to create a user with action privileges to create and manage assets.

  * **OAuth Client ID** and **OAuth Client Secret** - The credentials for OAuth-based access to ServiceNow. Refer to [OAuth 2.0 with Inbound REST](https://community.servicenow.com/community?id=community_blog\&sys_id=56086e4fdb9014146064eeb5ca961957) for full details on how to obtain the OAuth Token.

  * **OAuth Refresh Token** - When using the OAuth method of authentication, enter the value of the Refresh Token issued by a ServiceNow instance. This token is used to obtain new access tokens without requiring the user to reauthenticate.

  * **OAuth Custom Endpoint Path** - Specify a custom endpoint path to be used instead of the default `oauth_token.do`.

  * **Enable sending OAuth requests as JSON** -  Enable sending the request in JSON format instead of the standard `www-form-urlencoded` format.

  * **Apigee URL** - The URL of the domain that the GET request is sent to for acquiring the Apigee token.

  * **Resource Apigee** - The specific resources that the Apigee token is configured to access.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

**Additional fields** - Specify additional fields to be added as part of the ServiceNow asset as key/value pairs in JSON format. For example:

* ```json
  {"field1": "value1", "field2": "value2"}
  ```

  You can also use functions within the field value either by themselves or embedded within larger text strings. In this example, the `{{CURRENT_DATE}}` function is embedded into the field value for the field **Date of Update**:

  <Image alt="AdditionalFieldsFunctionsCurrentDate.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdditionalFieldsFunctionsCurrentDate.png" />

  * Use the `{{CURRENT_DATE}}` function to add the current date:

    * Using `{{CURRENT_DATE}}` with no format codes is the same as using the format codes: `%B %d, %Y`. This produces a date string like this: August 09, 2022.
    * Use format codes to specify a date format. For example, in the string *AX VM Update - `{{CURRENT_DATE:%m/%d/%Y}}`*, the *`%m/%d/%Y`* format codes will be replaced with 08/09/2022. The full string will be *AX VM Update - 08/09/2022*. The available format codes are described here: [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

* **Split by field values** - Splits the field values by the selected adapter and field.

* **Do not map default Axonius fields** - Select whether to map the set of default Axonius fields to the ServiceNow asset. For details, see [Default Field Mapping](/docs/default-field-mapping).

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* If **Fetch dynamic dropdown values** is enabled for the adapter connection, **Placeholder text fields** will be a list populated with the available values from ServiceNow.

* **Convert Preferred Total RAM (GB) to MB** - select to display the total RAM in Megabytes instead of in Gigabytes.

* **Use first IP address only** - Select whether the first IP address to be added to the ServiceNow asset.

  * If enabled, only the device's first IP address will be added to the ServiceNow asset.
  * If disabled, all the device's IP addresses will be added to the ServiceNow asset.

* **IP addresses delimiter** *(default: /)* - Specify the delimiter to separate between multiple IP addresses added to the ServiceNow asset.

  * If supplied, the specified delimiter will be used to separate between multiple IP addresses added to the ServiceNow asset.
  * If not supplied, the default delimiter will be used to separate between multiple IP addresses added to the ServiceNow asset.

* **Use first MAC address only** - Select whether the first MAC address to be added to the ServiceNow asset.

  * If enabled, only the device's first MAC address will be added to the ServiceNow asset.
  * If disabled, all the device's MAC addresses will be added to the ServiceNow asset.

* **MAC addresses delimiter** *(default: /)* - Specify the delimiter to separate between multiple MAC addresses added to the ServiceNow asset.

  * If supplied, the specified delimiter will be used to separate between multiple MAC addresses added to the ServiceNow asset.
  * If not supplied, the default delimiter will be used to separate between multiple MAC addresses added to the ServiceNow asset.

* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded.

  * If supplied, Axonius will not add to ServiceNow IP addresses in the IP range of the specified CIDRs.
  * If not supplied Axonius will add to ServiceNow IP addresses in any IP range.

* **CIDR include list** - Specify a comma-separated list of CIDRs to be included.

  * If supplied, Axonius will only use ServiceNow IP addresses in the IP range of the specified CIDRs.
  * If not supplied Axonius will add to ServiceNow IP addresses in any IP range.

* **Number of parallel requests** *(default: 10)* - The number of requests allowed at the same time.

* **Additional fields to use by querying ServiceNow** - This option allows you to specify an “external enrichment query“ (by specifying a ServiceNow table, and a mapping between Axonius fields to ServiceNow fields). You then specify mapping between the source table (the query results table) to the destination table (the table where the EC will create the asset in ServiceNow).

  * This ServiceNow query is performed for every device the EC is run for.

  * The result of the ServiceNow query is appended to the created asset (based on the mapping between the source table to the destination table).

  * Enter the required information in the following fields:

    * **Table Name** - the source table for query data.

    * **Axonius to source table query mapping** - Define the mapping between Axonius fields and the ServiceNow source table.

    * **Filter Operator** - Select the filter operator in ServiceNow which will be used when querying the table:

      * **Is one of** - Checks whether the value in Axonius is contained within a list of values in the ServiceNow field.
      * **Contains** - Checks whether the value in Axonius is contained in the ServiceNow field value.
      * **Is** - Checks for complete equality between the Axonius field and the ServiceNow field.

    * **Axonius fields** - Select the Axonius fields you want to use to enrich the ServiceNow table. The fields used to query the table (e.g., using the device IP address of the  Axonius field to search the table to find an entry with that IP address).

  * **Create Record with matching values if no existing values found** -   When an entity does not exist in the ServiceNow table, it will be created.

    * When not selected, and an Axonius field is missing from the mapping (i.e.,a device doesn’t have this field), the query for that device is skipped. Only the first result from each query for each device is used (i.e., for a device, every query from ServiceNow will only have a single result).

  * **Source table fields to Destination table fields mapping** - Mapping from the ServiceNow source table to the destination table fields. Define the fields in a JSON formatted file, as follows:

    ```json
    {“source_table_field“: “dest_table_field“, “source_table_field_2“: “dest_table_field_2“}
    ```

    Reference fields from the source table will be mapped to the destination table using their “display\_value“.

* **Exclude connections** - From the list, select the connections to ignore. You can select more than one.

* **Update only the following tables (Comma Separated)** - When the Enforcement Set runs on a device with two ServiceNow records, enter a comma separated list of ServiceNow tables. Only records from the tables listed in this fields are updated. You can enter a wildcard (\*) in this field, in which case all records are updated.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).

<br />