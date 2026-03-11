# Source: https://docs.axonius.com/docs/servicenow-adv-settings-custom-asset-schema.md

# ServiceNow Advanced Settings - Custom Asset Schema

You can use the Custom Devices schema and the Custom Users schema to add a JSON file that fetches information from one object to another, such as from a source or to enrich a device with information from a different object. You can add more than one JSON file.

## Using Custom Schema Entries to Fetch Information from One Object to Another

### Example 1

```json
{
        "type": "link",
        "link_type": "reverse_reference",
        "source_table": "u_computer_users",
        "source_field": "software",
        "destination_table": "u_sn_cmdb_ci_class_configuration_item_has_users",
        "linked_record_identifier": "u_user",
        "link_to_field": "ax_local_accounts"
}
```

* **link\_type** - The supported types are:
  * `reference` - For one-to-one relationships
  * `reverse_reference` - For many-to-one relationships
* **source\_table** - The type of the source object type in ServiceNow. This is the table that will be enriched from the data in the destination\_table.
* **source\_field** - The attribute of the object type from which the values should be brought. Enrich the contents of the **source\_table** which has the same name as the value of the **source\_field** in the **destination\_table**, with the contents of the **destination\_table field**.
* **destination\_table** - The destination object type in ServiceNow from which the data will be imported.
* **linked\_record\_identifier** - The name of the attribute that identifies the object.
* **link\_to\_field** - A name for the key in raw view which will contain the newly fetched data.

All of the above are mandatory.

### Example 2

**An example for `reverse_reference’` that utilizes different keys:**

```
 {
 "type": "link",
 "link_type": "reverse_reference",
 "source_table": "$ROOT",
 "based_on_field": "u_supporting_table_ref",
 "destination_table": "u_supporting_table",
 "link_to_field": "u_item_number",
 "linked_record_identifier": "sys_id"
}
```

* **based\_on\_field** - An attribute in the `source_table` with a value that matches the `linked_record_identifer` in the `destination_table`.
* **linked\_record\_identifier** - An attribute with a value that matches the root table `sys_id` or the attribute specified in `based_on_field`.
* **link\_to\_field** - A name for the key in raw view which will contain the newly fetched data.

<Callout icon="📘" theme="info">
  **Note**

  Fields are not compared by the display name of an attribute, but the actual value.
</Callout>

### Example 3

**Creating a complex object from nested data in the raw view:**

```
[
  {
    "label": "Owners",
    "relative_path": "fields/owners",
    "parsed_field": "owners",
    "field_type": "objects",
    "inner_fields": {
      "display_name": {
        "label": "Name",
        "raw_field": "displayName",
        "field_type": "str"
      },
      "active": {
        "label": "Is Active",
        "raw_field": "active",
        "default_value": false,
        "field_type": "bool"
      }
    }
  }
] 
```

* **label** - The display name of the new field.
* **relative\_path** - The path to the parent attribute.
* **field\_type** - Use “objects” to create a complex field.
* **inner\_fields** - A description of attributes to append to the desired complex field in the table view.
* **raw\_field** - The raw name of the field (key name).
* **default\_value** - Default value for the attribute if null.
* **field\_type**
  * The accepted values are:
    bool, boolean, str, string, date, datetime, float

<Callout icon="📘" theme="info">
  **Note**

  Pre-existing complex fields cannot not be overwritten or have data appended to them.
</Callout>

### Example 4

**Linking many-to-one based on a field that contains another many-to-one link:**

To implement this, add `/` inside `based_on_field`:

```
[
  {
    "type": "link",
    "source_table": "$ROOT",
    "based_on_field": "z_snow_nics/sys_id",
    "destination_table": "cmdb_ci_ip_address",
    "linked_record_identifier": "nic",
    "link_to_field": "x_cmdb_ci_ip_address",
    "link_type": "reverse_reference"
  }
]
```

### Example 5

**Using $ROOT as a source:**

It is not necessary to list all of the source tables; instead of listing all source\_tables, you can write “$ROOT” in the “source\_table” field. For example, if the source table contains the field "owner", then the system fetches the object of the sort "user" for all of the tables. This will populate associated users for all source objects that have the field "owner".

```json
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

### Example 6

**Reference field with multiple values:**

When the original reference field contains multiple values, use `csv_reference` for the **link\_type** field. In this case, the output will be an array of objects instead of a single object.

* The expected input (raw field) needs to be a string of comma-separated ServiceNow identifiers (sys\_id). For example:

  `"u_related_servers": "71c031213784200044e0bfc8bcbe5de1,46c12959a9fe1981009955ab1fa64226,6b43105c37301000deeabfc8bcbe5db2,2dfd7c8437201000deeabfc8bcbe5d56"`

The JSON should be in this format:

```json
[
  {
    "id": "17112500002",
    "type": "link",
    "link_type": "csv_reference",
    "source_table": "$ROOT",
    "source_field": "u_relate_servers",
    "destination_table": "cmdb_ci",
		"linked_record_identifier": "sys_id"
  }
]
```

The output is an array of objects: `"u_related_servers": [{...},{...},{...}]`