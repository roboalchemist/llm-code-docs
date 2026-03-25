# Source: https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping.md

# Axonius to External Field Mapping

Use the field mapping Wizard to map Axonius fields to fields in external systems. In this way you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions; for example **Axonius to ServiceNow field mapping**. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

## Mapping Fields from External Systems to Axonius Fields

Use the Wizard to enter fields from External Systems and map them to Axonius fields.
**To map Axonius fields to fields from External Systems:**

Note: Screen captures in the example are from ServiceNow.

1. From the **Action Library**, click **Manage CMDB Assets**, and then click the name of the Enforcement Action set you want to configure.

2. Locate the section **Map Axonius fields to \ fields**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MapCMDB1.png)

3. In the text box with the prompt **Enter \ field**, enter the name of an external field.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MapCMDBEnterPrompt.png)

4. Click the **Adapters** list drop down and select an adapter. You can select the name of an aggregated field available on the system, or fields from one or more specific adapters.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MapCMDBAdapterList.png)

5. Click the drop down box to see fields available and select a field.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MapCMDBSelectFieldList.png)

6. Click **Add Field** to add another field to map.

7. If necessary, select more field/adapter combinations and set their priorities. By default, the first combination is assigned 1st priority. See [Setting Priority for Adapters and Fields](/docs/axonius-to-cmdb-field-mapping#setting-priority-for-adapters-and-fields) for more about how to set field priority.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldMapping2.png)

* Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIcon-gray.png) to delete a row.

<Callout icon="📘" theme="info">
  Note

  Each custom field is sent as is, and not converted to a different format (i.e. integers remain integers, and their format is not changed).
</Callout>

### Setting Priority for Adapters and Fields

When you choose specific adapters, the system can check whether the field/adapter combination is available according to priority that you can set. If the specific field/adapter combination is not available, additional field/adapter combinations are checked according to priority that you set. You can select different fields for each adapter and priority.

1. Choose an adapter and a field. **1st** appears in the drop down box
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MappingFirst-1.png)

2. Click **1st**  and choose **Add 2nd mapping priority**. A search box appears to the right.

   <Image alt="Add2ndMapping.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Add2ndMapping.png" />

3. In the Search box, type an adapter name or select one from the list.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MappingSearch\(2\).png)

4. In the field list, select a field. The field can be any field in the list.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MappingSearch-2.png)

5. Click **2nd** to add a third adapter and field.<br />
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldMappingFieldAdapCombo-small.png)

You can add as many adapter/field combinations as required.

### Loading a Table of Mapped Files from a CSV File

You can also load a CSV file with a list of mapped fields. The CSV file should contain three columns with the titles, 'Adapter', 'Axonius field', 'External field'.

* **Adapter** - the Axonius field adapter, if this is empty use Aggregated.
* **Axonius field** - the name of the Axonius field
* **External field** - the name of the field from the external system.

Axonius provides a template to create these CSV files

1. Click **Template** to download the  template.

<Image alt="MappingTEmpalte.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MappingTEmpalte.png" />

2. Click **Import CSV** to load a CSV file; a browser opens for you to upload a file.

   * If you have already mapped values, the imported file adds to the existing values.
   * If a field is mapped and also appears in the CSV file, the value in the CSV file overrides the value in the wizard.

## Switching between Wizard and JSON View

You can view and define field mapping using the wizard or by describing the adapters, fields, and priorities in JSON format.

* Click **JSON view** to see the mapping in JSON format or set the mapping using JSON.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldMapping-WizardToJSON.png)

* Click **Wizard view** to go back to the wizard.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldMapping-JSONToWizard.png)

### Mapping Format in JSON

You can set the mapping of Axonius fields to fields from external systems using JSON. The input format is key/value pairs in JSON format.
For example:

```text
{"axonius_field1":"servicenow_field1", "axonius_field2":"servicenow_field2"}
```

**Axonius Field Format**

* Axonius field names can be supplied in a **short name** or in a **full name** format. The following table provides examples for each format for each field type:

<Callout icon="📘" theme="info">
  Note

  If you open the JSON file in the Wizard, the Wizard converts the Axonius field names to  **short name** format. **Full name** is still supported.
</Callout>

| Field Level | Field Type | Field Label in GUI                                                                                  | Format - Short Name                             | Format - Full Name                                             | Comment                                                                         |
| ----------- | ---------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Aggregated  | Simple     | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1666\).png) | hostname                                        | specific\_data.data.hostname                                   |                                                                                 |
| Adapter     | Simple     | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1669\).png) | aws\_adapter:hostname                           | adapters\_data.aws\_adapter.hostname                           |                                                                                 |
| Aggregated  | Complex    | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1673\).png) | installed\_software:name                        | specific\_data.data.installed\_software.name                   | Mapping is supported only for the 1st level fields in a complex field hierarchy |
| Adapter     | Complex    | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1675\).png) | tanium\_asset\_adapter:installed\_software.name | adapters\_data.tanium\_asset\_adapter.installed\_software.name | Mapping is supported only for the 1st level fields in a complex field hierarchy |

* A field that contains multiple values will be mapped to a single string consisting of the various values separated by comma.
* The supplied field mapping can override any of the default mappings done when the external entity is created/updated.
* If the supplied Axonius field is not found, the specific key/value pair will be ignored.

**External System Field format**

* The External System field names are the External system technical name as defined in the relevant API.

#### Setting Priority in the JSON View

You can set priority in the JSON file, refer to [Setting Priority for Adapters](#setting-priority-for-adapters-and-fields)
To set priority use one of the following syntax options:
**Option 1:**

```text
"adapter1name, adapter2name, adapter3name: asset name”:”servicenow_assetname"
```

For example:

```text
"alibaba_adapter,aws_adapter,cisco_adapter :plugin_and_severities.nessus_instance.thorough_tests": "test"
```

**Option 2:**

```text
"adapter1name=field1name,adapter2name=field2name, adapter3name=field3name”:”servicenow_assetname"
```

For example:

```text
{
"service_now_adapter=hostname,jira_software_adapter=asset_name": "servicenow_assetname"
}
```

#### Mapping the Same Axonius Field to More than one External System Field

Use commas in the JSON file to map the same Axonius field to more than one External System field.
For example: "hostname": "test,dd"

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).