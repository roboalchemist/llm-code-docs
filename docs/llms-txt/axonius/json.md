# Source: https://docs.axonius.com/docs/json.md

# JSON

The JSON adapter is able to import .json files with information about devices, users, or installed software.

## Asset Types Fetched

* Devices
  , Aggregated Security Findings, Users
  , Software
  , SaaS Applications

The adapter parameters are as same as the [CSV adapter parameters](/docs/csv). Although the JSON adapter parameter list does not include the **File contains installed software information** field, the adapter is capable of importing [installed software data](/docs/csv#which-fields-can-be-populated-for-each-file-import-type), but since it has a dynamic structure (unlike CSV), it is not required to declare that.

The functionality of this adapter is as same as the [CSV adapter](/docs/csv).

In addition, the following connection parameters are available specifically for the JSON adapter:

* **File format is JSONL** - Select this option to upload a file in JSONL format (JSON Lines). When you select this option, if you are uploading more than one files from an S3 directory, all files must have the same format (either JSON or JSONL).
* **JSON Path to fetched entities (Empty for top level)** - Select this option to fetch assets that are not on the top level from the JSON file. Add the JSON path to the list of assets, for example: `point1/point2/elements`

<Image border={false} src="https://files.readme.io/fd6fd536735b2aef5ed4ac32d6cdd4235f1b2ba1c003d0817e922746ddaa960e-image.png" />

<br />

## Example JSON File

Given the following JSON file with a single device:

```
[
    {
        "id": "device_example_id",
        "name": "asset_name_example",
        "hostname": "hostname_example",
        "list_example_field": [
            {
                "field1": "value1",
                "field2": "value2"
            }
        ],
        "installed_software": [
            {"swname": "softwar_example_123", "swversion": "v1.2.3.4.5.6.7.8.9.10"}
        ],
        "custom field example": "custom json example value",
        "custom numeric example field": 123
    }
]
```

The following JSON asset entity will be created:

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(898).png" />

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(897).png" />

<Callout icon="📘" theme="info">
  **Note**

  The ID field doesn't have to be on the first level of fields. It can also appear in the `metadata` field, for example:

  ```
  {
    "apiVersion": "aquasecurity.github.io/v1alpha1",
    "kind": "VulnerabilityReport",
    "metadata": {
      "name": "hostname01"
    },
    "report": {
      "other": "fields"
    }
  }
  ```
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use fetch time for Last Seen** - Select this option to set that all entities (devices and users) fetched by this adapter have their Last Seen set to the time the entity was fetched (fetch\_time).
2. **Do not add filename to entity IDs** - By default Axonius adds the filename to the ID of the entities created by the CSV file (device ID etc). Select this option to not add the filename to the entity ID.
3. **Parse entity fields dynamically** - This setting is enabled by default so that the adapter dynamically parses all of the fields of the entity fetched. Unselect to disable this setting.
4. **Custom Parsing** - see [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>