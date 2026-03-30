# Source: https://docs.axonius.com/docs/freshservice.md

# Freshservice

Freshservice is a cloud-based IT help desk and service management solution that enables organizations to simplify their IT operations.

<br />

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications
* Tickets

## Parameters

1. **Freshservice Domain** *(required)* - The hostname of the Freshservice server. The hostname field format is '\[instance].freshservice.com'.

2. **API Key** *(required)* - Specify the API Key provided by Freshservice.
   To locate your API Key, see [Locate API Key](/docs/freshservice#locate-api-key).

3. **Throttle API Requests** - Select this option to only use 90% of the API total rate limit bandwidth. For example: If a customer has 3000 total API calls allowed per hour, Axonius will only produce 2700 calls and leave the remaining 10% available.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Freshservcenew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Freshservcenew.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Freshservice asset  type Include list** *(optional)* - Specify a comma-separated list of Freshservice asset types.
   * If supplied, all connections for this adapter will only fetch devices whose asset type is any of the comma-separated list of Freshservice CI types that have been defined in this field.
   * If not supplied, all connections for this adapter will fetch devices with any Freshservice asset type.
2. **Fetch installed software** - Select to fetch installed software.
3. **Fetch disabled users** - Select to fetch disabled users. This setting is relevant only if one of the **Fetch \_\_\_ as Users** settings is selected.
4. **Fetch devices** *(optional, default: true)* - Select to fetch devices.
5. **Fetch device relationships**  - Select this option to fetch device relationships from Freshservice (when cleared this data is not fetched).
6. **Fetch Agent as Users** - Select to fetch agents as users.
7. **Fetch Requesters as Users** - Select to fetch requestors as users.
8. **Fetch Assets as Users** - Select to fetch assets as users.
9. **Use short format to describe OS Builds** - Select this option to use short format to describe OS Builds.
10. **Fetch and resolve Product Fields** - Select this option to fetch Freshservice product fields.
11. **Devices Schema** and **Users Schema** *(Custom schema entry (JSON)* - Use these settings to add a JSON file to fetch information from one object to another. Refer to [Using Custom Schema Entries to add a JSON file to Fetch Information from One Object to Another](/docs/freshservice#using-custom-schema-entries-to-add-a-json-file-to-fetch-information-from-one-object-to-another) for details of how to configure these fields.
12. **Advanced to Basic Devices Schema** and **Advanced to Basic Users Schema** *(Custom schema entry (JSON)* - You can configure fields that generally appear in 'Advanced' to appear in 'Basic' view. Refer to [Showing Advanced Fields in Basic View](/docs/freshservice#showing-advanced-fields-in-basic-view).
13. **Enable real-time asset updates (Supported events: New Tickets)** *(default: disabled)*- Select this option to update assets in real-time with New Ticket events.
14. **Fetch EC Action ticket updates** *(optional, default: true)* - Select whether to fetch EC action ticket updates.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Using Custom Schema Entries to Add a JSON File to Fetch Information from One Object to Another

You can use Custom devices schema, Custom users schema to add a JSON file to fetch information from one object to another. For instance from a source. For instance to enrich a laptop with information from another object. You can add more than one JSON file.

The schema below fetches extra information for the entity in the “Assets” table from the “Users” table and it looks up using the value in the “UserID” field. It then inserts the information in the “Advanced View” (JSON view in the Asset Profile page for the specific adapter connection) under the “ax\_user” field. The JSON file must be of the format:

```JSON
{
        "type": "link",
        "link_type": "reference",
        "source_table": "Assets",
        "source_field": "UserID",
        "destination_table": "Users",
        "link_to_field": "ax_user"
}
```

**link\_type** - The only supported type is reference.
source\_table - The type of the source object type in Freshservice. This is the table that will be enriched from the data in the destination\_table.
**source\_field** - The attribute of the object type from which the values should be brought. Enrich the contents of the **source\_table** which has the same name as the value of the **source\_field** in the **destination\_table**, with the contents of the **destination\_table field**.
**destination\_table** - The destination object type in Freshservice from which the data will be imported.
**linked\_record\_identifier** - the name of the attribute that identifies the object.
All of the above are mandatory.
It is not necessary to list all of the source tables, instead of listing all source\_tables, it is possible to write “$ROOT” in the “source\_table” field.

```JSON
[
  {
    "id": "35452789AI",
    "type": "link",
    "link_type": "reference",
    "source_table": "$ROOT",
    "destination_table": "sys_user",
    "source_field": "u_user"
  }
]
```

For instance if the source table contains the field "owner" then the system fetches the object of the sort "user" for all of the tables. This will populate associated users for all source objects that have the field "owner".

### Showing Advanced Fields in Basic View

You can configure fields that generally appear in 'Advanced' to appear in 'Basic' view. Configure for devices and users separately as required. Use the plus sign to add an entry to each field.

<Image alt="Freshservice Advanced to Basic" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Freshservice%20Advanced%20to%20Basic.png" />

Enter fields in the following JSON format:

```JSON
[
{
    "label":"My First Field", 
    "raw_field": "field_a",
    "field_type": "str"
},
{
    "label":"My Second Field",
    "raw_field": "field_b",
    "field_type": "int"
}
]
```

* **label** - the name for the field you want to appear in the basic view
* **raw\_field** - the path of the field as it appears in JSON format on the Adapter Connections page of the Asset Profile (or Advanced view table). For the inner path use the slash sign (/).
* **field\_type** -the field type as  it appears in JSON format. The following field types are supported. int, string, datetime, float, bool. You can write them in the following ways:

  'int', 'string', 'str', 'date', 'datetime', 'float', 'bool', 'boolean'.

## APIs

Axonius uses the [Freshservice API](https://api.freshservice.com/#intro).

## Locate API Key

**To locate your API Key**

1. Log in to your **Support Portal**.
2. Click on your profile picture on the top right corner of your portal.
3. Go to the **Profile Settings** page. Your API Key is displayed below the **Change Password** section on the right side.

<br />

## Related Enforcement Actions

* [Freshservice - Create Ticket](/docs/create-freshservice-ticket)
* [Freshservice - Create Ticket per Asset](/docs/create-fresh-service-ticket-per-entity)
* [Freshservice - Create Assets](/docs/create-freshservice-asset)
* [Freshservice - Update Assets](/docs/update-freshservice-asset)
* [Update Fresh Service Ticket](/docs/update-fresh-service-ticket)
* [Freshservice - Add or Remove User from Group](/docs/assign-freshservice-group)
* [Freshservice - Update Application](/docs/update-fresh-service-application)
* [Freshservice - Create Service Request per Asset](https://docs.axonius.com/axonius-help-docs/docs/create-fresh-service-service-request)