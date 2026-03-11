# Source: https://docs.axonius.com/docs/atlassian-jira-service-desk.md

# Jira Service Management

Jira Service Management (Service Desk) enables to receive, track, manage, and resolve requests from customers.
Use to fetch assets from the Jira Insight platform. This is intended to be used with Jira Service Management.

In order to correlate data correctly in Axonius, define the following fields in your system as follows:

| Field Name  | Accepted  Field Name(s) in Jira            |
| :---------- | :----------------------------------------- |
| MAC Address | MAC, Mac Address, MAC Address, mac address |
| IP Address  | IPs, Ip Address, IP Address, ip address    |

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Business Applications, Tickets, Application Services, Networks, Certificates, Software

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Jira Service Management (Jira Service Desk) server.
2. **Jira Service Management API version** - The version type. The default value is 1.0
3. **User Name** and **API Token** *(required)* - The credentials for a user account that has the permissions to fetch assets. Note: The API Token is not the same as the Admin Key. For information on how to create an API Token, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).
4. **Verify SSL**  - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
8. **Use Cloud API** - Use this option to add support for cloud-based installations of Jira Service Management (Service Desk) with Jira Insight.
9. **Workspace IDs** *(optional)* - Enter an optional list of Workspace IDs to use. If no Workspace IDs are entered, the adapter queries the configured hosts for all Workspace IDs.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="JiraServiceManagementCloudConfigN" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JiraServiceManagementCloudConfigN.png" />

*Jira Service Management Settings for Cloud*

<Image alt="JiraServiceManagementOnPremN" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/JiraServiceManagementOnPremN.png" />

*Jira Service Management Settings for On Prem*

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **IQL query (Override Filter Device object types)** - Enter a custom IQL query so that all objects will be treated as devices. Note that using this setting will override the configuration value set in **Filter Device object types**.
2. **Filter Device object types** - Enter a comma-separated list of objects that the client wants to fetch, for example 'Servers, laptops, desktops'. Then only these object types are fetched.

<Callout icon="📘" theme="info">
  Note

  If you do not define the object types using this setting, then ALL assets, regardless of type, are mapped as devices.
</Callout>

3. **IQL query for Users (Override Filter Users object types)** - Enter a custom IQL query so that all objects will be treated as users. Note that using this setting will override the configuration value set in **Filter Users object types**.

4. **Filter Users object types** - Enter a comma-separated list of objects to parse as users, for example: ‘Employees’.

5. **IQL query to asset mapping** - From the **Axonius Asset Type** dropdown, select an asset type. In the **IQL query for Jira** field, map a relevant IQL query to fetch the selected asset from Jira. Click `+` to add more assets to fetch.

6. **Use asset name for hostname** - Select this option to use the asset name for the hostname if the hostname doesn't exist.

7. **Use Device 'Updated' as 'Last Seen'** - Select this option to use the "Updated" field as "Last Seen".

8. **Additional MAC Address Field Names** - Enter a list of Jira field names that the adapter should recognize as MAC address fields. To add each field name, type the value and then press **Enter** to create a new entry.

9. **Additional IP Address Field Names** - Enter a list of Jira field names that the adapter should recognize as IP address fields. To add each field name, type the value and then press **Enter** to create a new entry.

10. **Custom schema entry (JSON)** *(Custom devices schema, Custom users schema)* - Use these settings to add a JSON file to fetch information from one object to another. Refer to [Using Custom Schema Entries to add a JSON file to Fetch Information from One Object to Another](/docs/atlassian-jira-service-desk#using-custom-schema-entries-to-add-a-json-file-to-fetch-information-from-one-object-to-another) for details of how to configure these fields.

11. [**Custom Parsing**](/docs/adapter-custom-parsing)

12. **Fetch EC Action ticket updates** - Select this option to configure the adapter to fetch updates on Jira Service Management tickets created using the [Jira Service Management - Create Issue](/docs/create-jira-service-desk-ticket) or [Jira Service Management - Create Issue per Asset](/docs/create-jira-service-desk-incident-per-entity) enforcement actions. The updated ticket information is stored in Axonius and can be displayed in the Tickets table of each relevant asset (user, device).

13. **Exclude devices with the following statuses** - Enter a comma-separated list of statuses. Devices with one of these statuses will not be ingested into the system.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

**Object Names**
Object names in Axonius are set according to the following parameters:

* The naming attribute in Jira. This is the attribute of the Jira object set as a label attribute (could be an attribute called 'green').

or

* The 'Name' attribute in the Jira object

or

* The 'objectKey' of the Jira object

in this order.

### Using Custom Schema Entries to Add a JSON File to Fetch Information from One Object to Another

You can use Custom devices schema and Custom users schema to add a JSON file to fetch information from one object to another. For instance from a source. For instance to enrich a laptop with information from another object. You can add more than one JSON file.
The JSON file must be of the format:

```json
{
        “type”: “link”,
        “link_type”: “reference”,
        “source_table”: “Manufacturer”,
        “source_field”: “Software”,
        “destination_table”: “Software”,
        “linked_record_identifier”: “objectKey”,
        “destination_table_fields”: [“Type”, “Vendor”],
        “destination_table_query”: “objectTypeId=5"
}

```

* **link\_type**  - The only supported type is reference.
* **source\_table** - The type of the source object type in Jira. This is the table that will be enriched from the data in the destination\_table.
* **source\_field** - The attribute of the object type from which the values should be brought.   Enrich the contents of the **source\_table**, which has the same name as the value of the  **source\_field** in the **destination\_table**, with the contents of the   **destination\_table** field.
* **destination\_table** - The destination object type in Jira from which the data will be imported.
* **linked\_record\_identifier** - the cname of the attribute that identifies the object.

All of the above are mandatory.

* **destination table fields** *(optional)* - List of fields to bring from the source - if no fields are listed, then all fields are brought.
* **destination\_table\_query**  *(optional)* - IQL Jira query to run when searching for the destination object.

It is not necessary to list all of the source tables, instead of listing all source\_tables, it is possible to write “$ROOT” in the  “source\_table”  field.

```json
“type”: “link”,
    “link_type”: “reference”,
    “source_table”: “$ROOT”,
    “source_field”: “Owner”,
    “destination_table”: “User”

```

For instance if the source table contains the field "owner" then the system fetches the object of the sort "user" for all of the  tables. This will populate associated users for all source objects that have the field "owner".

## APIs

Axonius uses the [Get AQL Objects API](https://developer.atlassian.com/cloud/assets/rest/api-group-aql/#api-aql-objects-get).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                         | Supported  | Notes |
| ----------------------------------------------- | ---------- | ----- |
| JIRA Service Desk 3.6.2                         | Yes        |       |
| docs.atlassian.com/jira-servicedesk/REST/3.6.2/ | Deprecated |       |

## Related Enforcement Actions

* [Jira Service Management - Create Ticket](/docs/create-jira-service-desk-ticket)
* [Jira Service Management - Create Ticket per Asset](/docs/create-jira-service-desk-incident-per-entity)
* [Jira Service Management - Update Tickets](/docs/update-tickets-jira)
* [Jira Service Management - Create Insight Asset per Asset](/docs/create-jira-insight-asset-per-entity)
* [Jira Service Management - Update Insight Asset ](/docs/update-jira-insight-asset)
* [Jira Service Management - Remove Insight Asset](/docs/delete-jira-insight-asset)

## Supported From Version

Supported from Axonius version 4.5