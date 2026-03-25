# Source: https://docs.axonius.com/docs/create-servicenow-computer.md

# ServiceNow - Create Assets

**ServiceNow - Create Assets** creates an asset in ServiceNow for:

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

* **Use stored credentials from ServiceNow adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
  </Callout>

* **Retry count** *(default: 1)* - If the action fails, Axonius will retry to run it the specified number of times for each asset.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

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

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## Main Asset Configuration

<br />

This section describes how to configure the main asset record created in ServiceNow.

* **CMDB CI table name** *(default: cmdb\_ci\_computer)* - Specify the target table in your ServiceNow CMDB where the new Configuration Item (CI) will be created, if other than the default table. For example, if you are creating a record for a network switch, you would enter *cmdbcinetgear\_switch* here to ensure it's placed in the correct table. This is essential for proper classification and management of different asset types within your CMDB.

* **Create devices in Axonius** - Select this option if you want the enforcement action also to create a corresponding device record in the Axonius platform using the data it is sending to ServiceNow. This option is crucial for keeping your Axonius asset inventory synchronized. It ensures that any new or updated asset information that originated from ServiceNow  and is being processed by the enforcement action is also reflected back in the Axonius platform.

<Callout icon="📘" theme="info">
  Note

  If a customer created an asset in a table that was not fetched by the adapter, the asset will not be updated.
</Callout>

* **Additional fields (JSON format)** - This field allows you to add extra, static key-value pairs to the asset payload that will be sent to ServiceNow. The data must be in valid JSON format. For example:

```json
{"field1": "value1", "field2": "value2"}
```

If the JSON is formatted incorrectly or a specified field name is invalid, the request may fail.

* **Example 1:** To add a static value for the operational\_status and department fields, you would enter:

```json
{"operational_status": "in_use", "department": "IT"}
```

* **Example 2:** If you enter a field called 'additional\_items', ServiceNow handles that data differently.  Instead of a simple key-value pair, it processes the contents as a separate object, which is used for advanced data such as the asset's discovery source. To specify Axonius as the source of the asset's data, you would use this format:

```json
{"additional_items": { "sys_object_source_info": { "source_name": "Axonius", "source_native_key": "123" } } }
```

This ensures that the *sysobjectsource\_info* field is sent correctly to the Identification and Reconciliation Engine (IRE), which properly records the asset's origin, and not as a mapped field.

* **Split by field values** - Select the adapter and the list field from that adapter to split into individual entities. The system will iterate through the specified list and generate a new entity for each entry, allowing you to send a distinct record for every item.<br />
  **Example:** If a single device record in your source data contains a list of three separate IP addresses, enabling this option will create three individual device entities in Axonius, one for each IP address.

* **Do not map default Axonius fields** - Do not map default Axonius fields - By default, Axonius automatically maps a set of standard fields to corresponding fields in ServiceNow assets (e.g., hostname, serial\_number, mac\_addresses). Enable this option to disable that default behavior. This is useful when you want to have full control over the field mapping yourself, or if your ServiceNow instance uses custom field names that conflict with the default mapping. For details, see [Default Field Mapping](/docs/default-field-mapping).

* **Map Axonius fields to ServiceNow fields** - Use the Field Mapping Wizard to define how data found in Axonius is transferred to ServiceNow. This process creates a direct link between a specific Axonius field (e.g., *hostname*) and a corresponding ServiceNow field (e.g., *name*), ensuring the correct data is populated in your assets. When the **Fetch dynamic dropdown values** option is enabled in the ServiceNow adapter connection, the wizard automatically displays a live, selectable list of available ServiceNow fields, which simplifies the process and prevents manual entry errors. For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).

* **Add last seen aggregated field details name if it was input in the previous mapping** - Configure this option to enrich an aggregated field in Axonius with additional details from a ServiceNow field. When you add a new entry, it creates a link so that the last seen data for a specific field is pulled from ServiceNow and displayed in the Axonius user interface. This is useful for ensuring that key, single-value fields from ServiceNow are reflected in Axonius aggregated fields, providing more detailed and accurate "last seen" information without needing to create a separate field mapping.

  * Click + to add values
  * In the **ServiceNow Key** field, enter the name of the field in ServiceNow that you want to reference (e.g., serial\_number, device\_status).
  * In the **ServiceNow Value** field, enter the name of the corresponding Axonius field.

* **Send True/False as boolean values** - Enable this option to ensure that True/False values from Axonius are sent to ServiceNow as a standard Boolean data type (true or false).

<Callout icon="📘" theme="info">
  Note

  If this option is not enabled, Axonius might send these values as simple text strings ("True" or "False"), which ServiceNow may not interpret correctly, potentially causing the request to fail or the data to be stored incorrectly.
</Callout>

* **Convert Preferred Total RAM (GB) to MB** - Select to convert the total RAM value from Gigabytes (GB) to Megabytes (MB) before it is sent to ServiceNow. This is useful when the corresponding field in your ServiceNow CMDB is configured to store data in MB, ensuring that the imported value is correctly formatted.

* **Use first IP address only** - Select this option to add only the first IP address from the Axonius device record to the ServiceNow asset. This is useful for environments where a device has multiple IP addresses (e.g., virtual interfaces, multiple NICs), but your ServiceNow CMDB is configured to store only a single, primary IP address for each asset. When not selected, the system adds all IP addresses to the ServiceNow asset, separated by the specified IP addresses delimiter.

* **IP addresses delimiter** *(default: /)* - Specify the custom character to use in between multiple IP addresses when they are added to a ServiceNow asset. If you don't specify a character, the default delimiter is used.

* **Use first MAC address only** *(default: enabled)* - Enable this option to ensure that only the first MAC address from the Axonius record is added to the ServiceNow asset. When disabled, all MAC addresses are added to the ServiceNow asset, separated by the specified MAC addresses delimiter.

* **MAC addresses delimiter** *(default: /)* - Specify the custom character to use in between multiple MAC addresses when they are added to a ServiceNow asset. If you don't specify a character, the default delimiter is used.

* **Use full URL for device creation** -  Select this option to use the entire URL entered in the 'ServiceNow Domain' field when creating a new device. (When this is not selected, only the domain part of the URL is used to create the device, and the rest of the URL is calculated by the Action depending on the table name.) This can be used, for example, to insert devices using a custom API in ServiceNow.

* **Create ServiceNow asset even if device's asset entities include ServiceNow** - Select this option to allow the enforcement action to create or update an asset in ServiceNow even if the device record in Axonius was originally discovered by a ServiceNow adapter. By default, the system prevents this to avoid creating duplicate records.

* **CIDR exclude list** - Specify a comma-separated list of CIDRs to be excluded from the data sent to ServiceNow. Any IP address that falls within the specified IP ranges will be ignored and will not be added to the asset record. If not specified, Axonius adds to ServiceNow all IP addresses.

* **CIDR include list** - Specify a comma-separated list of CIDRs to send to ServiceNow only those IP addresses within the specified ranges. If not specified, Axonius adds to ServiceNow all IP addresses.

* **When using IRE, specify main asset referenced field names that must be translated to sys\_id** - This only applies when using the Identification and Reconciliation Engine (IRE). This field is for specifying which asset fields contain a reference to another record in ServiceNow. By default, Axonius sends the display value of a field (e.g., a user's name or a department's name). However, ServiceNow's IRE requires the unique system ID (**sys\_id**) of the related record to correctly link assets. Enter the names of the fields that need to be translated to a **sys\_id** for IRE to properly process and connect the asset records. Press **Enter** to add each field name as a new entry.

* **Additional fields to use by querying ServiceNow** - This option allows you to enrich new assets with additional data by performing a query on an external ServiceNow table. For every asset created, the system uses a key field from Axonius to find a matching record in ServiceNow. The results of that query are then used to update the newly created asset.

  * This option allows you to specify an 'external enrichment query' (by specifying a ServiceNow table, and a mapping between **Axonius fields** to **ServiceNow fields**). You then specify a mapping between the source table (the query results table) and the destination table (the table where the EC will create the asset in ServiceNow).

  * This ServiceNow query is performed for every asset for which the EC is run.

  * The result of the ServiceNow query is appended to the created asset (based on the mapping between the source table and the destination table).

  * To add an enrichment query, click **+ Add Enrichment Query**, and define the following:

    * **Table Name** - The ServiceNow source table to query for additional data (e.g., cmdb\_ci\_server).

    * **Axonius to source table query mapping** - Define the mapping between **Axonius fields** and the ServiceNow source table.

    * **Axonius fields** - Select the Axonius fields you want to use to enrich the ServiceNow table. The system will use the values of these fields to search the specified ServiceNow table for a corresponding entry. For example, you might use a device's IP address from the Axonius field to query the ServiceNow table to find a corresponding entry with that IP address.
      For details on the Axonius field configuration, see the relevant instructions  in [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).

    * **Filter Operator** - Select the type of match to use when querying the ServiceNow table:
      * **Is one of** - Checks if the Axonius field value is contained within a list of values in the ServiceNow field.
      * **Contains** - Checks if the Axonius field value is a substring of the ServiceNow field value.
      * **Is** - Checks for a complete and exact match between the Axonius and ServiceNow fields.

    * **Create Record with matching values if no existing values found** - When enabled, a new record will be created in the specified ServiceNow table if no matching asset is found.
      * When disabled, the query is skipped for an asset if a required Axonius field is missing from the mapping. The system uses only the first result from each query, even if multiple matches are found.

    * **Source table fields to Destination table fields mapping** - This field defines how to transfer data from the enrichment query's results to the newly created asset. Define this mapping in JSON format, where the *key* is the field from the source table and the *value* is the corresponding field in the destination table. Reference fields from the source table are mapped to the destination table using their “display\_value“ to ensure data is transferred correctly.

    ```json
    {“source_table_field“: “dest_table_field“, “source_table_field_2“: “dest_table_field_2“}
    ```

* **Create ServiceNow asset for each installed software** - Select this option to automatically create a new ServiceNow asset for each software application installed on the device.
  * By default, the enforcement action will only create a single asset for the main device (e.g., a computer).
  * When enabled, it will also create or update a new related asset for each software application (e.g., one for Adobe Photoshop, one for Microsoft Office, etc.), linking them to the main device asset.

* **Assure uniqueness of created software assets** - When both this option and **Create ServiceNow asset for each installed software** are selected, a new software asset will not be created in ServiceNow if the asset exists in ServiceNow and was previously fetched from any adapter connection. This prevents the duplication of software assets.

* **Asset payload static data** - When using IRE, use this field to add static, predefined key-value pairs directly to the asset payload`s root level that will be sent to the ServiceNow Identification and Reconciliation Engine (IRE). This option is primarily used for providing IRE-specific metadata, such as the discovery source, that doesn`t fit into the standard field mapping.
  * **Example:** To define Axonius as the discovery source for all created assets, enter the following JSON:

```json
{"sys_object_source_info":{"source_name":"Axonius"}} 
```

The result will be:

```json
{
  "items": [
    {
      "className": "cmdb_ci_computer",
      "lookup": [],
      "values": {here are the asset fields},
      "sys_object_source_info": {
        "source_name": "Axonius"
      }
    }
  ],
  "relations": [here are the relations]
}
```

* **Skip asset creation if the asset already exists in ServiceNow** - When selected, if the asset already exists in ServiceNow, it will not be created again.

## Related Asset and IRE Configuration

Use these settings to create and manage assets that are related to the main asset that is created. For instance, you can create a new software asset and link it to its host computer.
The Identification and Reconciliation Engine (IRE) fields in this section are optional.

* **Use Identify Reconcile Discovery Source to create asset and related assets** - Creates the asset using the [Identification and Reconciliation (IdentifyReconcile) API](https://developer.servicenow.com/dev.do#!/reference/api/paris/rest/c_IdentifyReconcileAPI). The supplied value is used as the source for the newly created asset. This uses the Identify Reconcile API to create the related asset instead of the regular create asset table API. This is the recommended method as it minimizes the creation of duplicate Configuration Items (CIs) and reconciles CI attributes by only accepting information from authorized sources when updating the Configuration Management Database (CMDB). It is recommended to use ‘Axonius’ as the source value.
  * If not supplied, the asset is created in ServiceNow via the [Table API](https://developer.servicenow.com/dev.do#!/reference/api/orlando/rest/c_TableAPI), and the CMDB will be updated directly.

* **Create virtual related assets if VM data exists** - Enable this option to create a separate related asset for each virtual machine. Add additional configuration for the virtual machine asset in the **Related Assets Configurations** section (below). The **Related asset table name** field must be empty.

* **Create cloud related assets if Cloud data exists** - Enable this option to create a separate related asset for each cloud instance3. Add additional configuration for the cloud asset in the **Related Assets Configurations** section (below). The **Related asset table name** field must be empty.

### Related Assets Configuration

Create related assets in addition to the main asset. Click **+ Add related asset configuration** for each related asset you want to configure.
**Related Asset**

* **Related asset table name** - When creating a non-virtual or non-cloud asset, enter the exact name of the ServiceNow table where the new related asset record will be created. For example, 'cmdb\_ci\_web\_server', cmdb\_ci\_network device. When creating a VM or cloud-related asset, leave this field empty. The related asset's table is automatically determined by the payload's data and the specific cloud-based mapping you've configured.

* **Asset Internal ID (IRE)** - Used to configure relations or references between related assets.
  May be omitted if not needed. If used, it must be unique.

* **Related asset creation method** - Select between IRE, Table, insertMultiple, and Main Asset Lookup List.
  * When you select insertMultiple, the **Related asset table name** must extend `sys_import_set_row`.
  * When you select Main Asset Lookup List and an IRE endpoint exists, the related asset will be added to the main asset's `lookup` field rather than as a separate asset in items.

* **Split related assets by complex field** - Enable this option to create a separate related asset for each item in a specified list field within a single payload. For example, a software license for each item in an installed\_software list. Each of these new assets will be created based on the field mapping that you configured. For example, a payload for a single server contains a network\_interfaces list field with details of three separate network interfaces. By enabling this option and specifying network\_interfaces as the field, the system will create three separate network interface assets, each using the data from its corresponding item in the list field.
  * **Filter related assets by field** - When **Split related assets by complex field** is enabled, you can filter the field according to the following:
    * **Axonius field** - Select an adapter and the field to filter by.
    * **Filter type** - Select the type of filter.
    * **Filter value** - Enter the value to filter for.
    * Click **+** to configure multiple filters.
    * Only the related assets that match the filter criteria are created. When multiple filters are configured, the are combined as with an AND; only assets that match all the filters are created.

* **Related asset fields with static data** - This field lets you set specific, non-changing values for any fields on a new or updated related asset. Any field you set here will be overridden if it is also included in the ServiceNow related asset fields mapping section. The mapping section takes precedence, using data directly from the incoming payload instead of the static value. This is useful to automatically populate fields that don't change from record to record, such as a default location, status, or source.

* **ServiceNow related asset fields mapping** - Use the **Field Mapping Wizard** to map **Axonius fields** to fields on the related asset in ServiceNow. In this way you can transfer data found in Axonius into ServiceNow. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note

  * For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).
  * When **Fetch dynamic dropdown values** is enabled for the ServiceNow adapter connection, and the ServiceNow adapter fetch ends successfully, the placeholder text fields within the Field Mapping Wizard will automatically be populated with the actual IRE field names available from ServiceNow.
</Callout>

* **Skip creating related asset if first "ServiceNow related asset fields mapping" mapped field value is empty** - Enable this option to prevent the creation of a new related asset record if the first field you have mapped in the ServiceNow related asset fields mapping section contains no value. This is a safeguard against creating incomplete or "junk" records in your CMDB (Configuration Management Database).

* **Specify related asset referenced field names that must be translated to sys\_id** - Enter the field names of the related asset, whose display values you want to translate to sys\_id.  For example, reference fields in the ServiceNow related asset fields mapping or in the Related asset fields with static data.

* **Main Asset fields to append when creating related asset** - Appends the fields from the main asset to the related asset values.

* **Update exists related assets (Table API only)** - Enable this option for Axonius to look up existing asset in the specified ServiceNow table, by querying the fields listed in **Asset unique key identifiers** (the following field). If one asset is found, it is updated (the same as IRE). If more than one asset is found, no action is performed. This prevents creating duplicate assets and instead updates existing ones.

* **Asset unique key identifiers** - This field specifies the criteria used by Axonius to perform the lookup described in the **Update exists related assets (Table API only)** field (above). It requires you to enter a list of ServiceNow field names (e.g., name, serial\_number, mac\_address) that, when combined, are used to form a unique identifier for the asset. You can add multiple fields, and they all work together to define the unique identity of an asset within the payload. Press **Enter** to add each field as a new entry.
  Axonius uses the values from the incoming asset data for these specified fields to query the target ServiceNow table to determine whether the incoming asset record already exists. If a match is found, the existing asset record is updated. If no match is found, a new asset record is created. It is important to choose a combination of fields that is unique for each asset.
  Example 1: Entering 'name' means Axonius will search for an existing asset where the value in the ServiceNow 'name' field matches the name value in the incoming asset data.
  Example 2: If you enter serial\_number and mac\_address, ServiceNow first checks for an existing asset with that specific combination of serial number and MAC address.

* **IRE relations or Reference configuration** - IRE relations allow you to create connections between two assets: a main asset and a related asset. You can use existing relationships from the ServiceNow relation table or define your own custom relations. Click **+ Add Relationship** to define a new relation and establish a clear directional connection.
  * **Relation Direction** - Specifies which asset is the source of the relationship. Select the direction of the relationship between main and related assets. The possible values are:
    * **Main Asset::Related Asset** - The main asset is the source of the relationship. For example, a server (Main Asset) hosts a website (Related Asset).
    * **Related Asset::Main Asset** - The related asset is the source of the relationship. For example, an application (Related Asset) runs on a server (Main Asset).
  * **Internal ID (IDE)** - Used to identify the "Other Related Asset" when using relevant relation direction types. Can only be used with IRE. Leave empty to point to the Main Asset. When **Split related assets by complex field** is used and both directions are generated, both adapter fields must be the same length.
  * **Relation type or Reference field name**
    * **Relation type** - Describes the specific nature of the relationship using a verb pair, between assets that ServiceNow discovers or identifies specifically for the IRE process(such as servers, applications, and databases). The first verb defines the relationship from the main asset's perspective, and the second verb defines it from the related asset's perspective.
      * **Runs on::Runs** - Describes a process or application that executes on another asset. For example, a database "'runs on' a virtual machine for direction **Related Asset::Main Asset** (the database is the related asset).

      * **Hosted on::Hosts** - Describes a hosting relationship where one asset provides a platform for another. For example, a web server 'hosts' a website for direction **Main Asset::Related Asset** (the web server is the main asset).
    * **Reference field name** - The field name you are referring to on the referred main or related asset. The options are `cmdb_ci` or `asset`.

## Additional Fields

These fields are optional.

* **Number of parallel requests** *(default:10)* - This setting controls the maximum number of requests that can be sent to ServiceNow simultaneously. The system only uses this limit when the total number of tasks is greater than the limit. If there are fewer tasks than the specified limit, the system sends all tasks at once.
* **Perform bulk insert (insertMultiple)** - Select this option to insert multiple assets created by the action into ServiceNow in a single bulk operation.

<Callout icon="📘" theme="info">
  Note

  * This option cannot be used with the 'Use full URL for device creation' or 'Use IdentifyReconcile API endpoint to create computer' options.
  * When using this option, the table name configured in 'CMDB CI table name' must extend the sys\_import\_set\_row table in ServiceNow.
</Callout>

* **Exclude connections** - Enable this option to prevent the action from querying assets from a list of selected connections. This is useful for filtering out data from specific sources when creating assets.

## Required Permissions

The ServiceNow user configured for this action must have the necessary roles to interact with the CMDB.

* For the **IdentifyReconcile API** - The ServiceNow user supplied in [User name](#parameters) must have either the 'itil' or 'asset' role to use this API. This API leverages ServiceNow's Identification and Reconciliation Engine (IRE) to manage CIs.
* For the **Table API** -  If you are not using the IdentifyReconcile API, the user must have the necessary permissions to write directly to the target table. This generally requires the 'itil' or 'admin' role.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).