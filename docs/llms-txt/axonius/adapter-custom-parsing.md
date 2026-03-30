# Source: https://docs.axonius.com/docs/adapter-custom-parsing.md

# Adapter Custom Parsing

Some adapters support the option of **Custom Parsing**, where you can define how to parse specific fields from the raw data fetched.  You can parse the data into an already existing field, or create a new one.

This option can be found in the adapter's **Advanced Configuration** section.

When adapters fetch multiple asset types, a separate **Custom Parsing** section exists for each asset type, as demonstrated below in the [CSV](/docs/csv) adapter example:

<Image alt="CSVcustomparsingenabled" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-PFVF7FAL.png" />

## Custom Parsing Parameters

Expand each asset type's Custom Parsing section to add fields. Then, for each field, specify the following:

* **Field Title** - Select a column title from the list. Note that you can also select nested fields of complex fields, for example: `Network Interfaces:Ips`.

* **Raw Path** - The path to the field in the raw data, for example: `my_path|my_sub_path`

* **Type** - Select a field type from the list: string, boolean, etc. Will be ignored for common fields.

* **Structure** - Specify whether the field is a single value or a list field. Will be ignored for common fields.

* **Software Registry Integration** – Mapping to the **Approval Status** field automatically adds the asset to the [Software Registry](/docs/software-approval-list), where it remains visible even if not detected on a device .

* **Advanced Options** *(optional)* - Click **Open Advanced Options** to open a dialog with more parsing options. Currently, the only available option is **Hyperlinks**. This allows you to create a hyperlink (clickable field) for items in the asset table that redirect to a different page within the system. In the **Advanced Options** dialog, provide the following parameters:
  * **Module** - The module (asset type) to link to. For example - Devices, Users, Networks, etc.
  * **AQL Expression** - An AQL expression to use in the link. Use `{{VALUE}}` as a placeholder for the field value.

<Image align="center" border={true} src="https://files.readme.io/8260983971b2cff7ce4a8669a2690e62f9154008d775e1f5a08e515660510645-image.png" className="border" />

**Hyperlink Example**

Assume you have a device with a username attribute linked to it, and you want to create a hyperlink that will direct you to that user.

1. Create a custom Devices field - for example, Linked User. Configure it like every other custom field. For more information, see [Managing Custom Fields](https://docs.axonius.com/axonius-help-docs/docs/managing-custom-fields).
2. Click **Open Advanced Options**. A dialog opens.

   1. For **Module**, select **Users**.
   2. In **AQL expression**, enter the following string: `("specific_data.data.username" == "{{VALUE}}")` so that the value of the Linked User field populate that expression.

   <Image align="center" border={false} width="400px" src="https://files.readme.io/26be153dd757d735cd673269366c3dc9715e1dddb22bc046e44f85be005f3ee0-image.png" />

   <Callout icon="📘" theme="info">
     **Notes**

     * Existing fields can't be set as hyperlinks - only new fields that you define.
     * Every valid AQL expression can be inserted. Axonius does not verify it before saving, so check the expression in advance.
   </Callout>
3. Click **+ Add Field** to add as many fields as you like, or **x** to delete the row.

### Using JMESPath as Raw Path

You have the option to populate **Raw Path** with a JMESPath (JSON Matching Expression paths) expression. JMESPath language is used to write path rules for selecting specific data fields in JSON.

The JMESPath expression you enter must start with "ax\_jmespath:".

**Example:**

The following parameters filter the list of serials to include only those with serial\_number\_type == 'system':

* **Field Title** = Device Manufacturer Serial
* **Raw Path** = "ax\_jmespath:ax\_sn\[?serial\_number\_type == 'system'].serial\_number"

If there is more than one item on the list where serial\_number\_type == 'system', the first one will be used.

To learn more, see [JMESPath Examples](https://jmespath.org/examples.html).

### Raw Path Examples

If your raw data is in *DOT\_DOT* notation, like the following example:

```
"\"Computer\"DOTDOT\"OS\"DOTDOT\"NT Info\"DOTDOT\"Server\"": "Yes",
"\"Computer\"DOTDOT\"Owner\"DOTDOT\"Display Name\"": "Josh Caruso",
"\"Computer\"DOTDOT\"Owner\"DOTDOT\"Lit Hold By Owner\"": null,
"\"Computer\"DOTDOT\"Owner\"DOTDOT\"Lit Hold By State\"": null,
"\"Computer\"DOTDOT\"Owner\"DOTDOT\"User Account Name\"": null,
"\"Computer\"DOTDOT\"Status\"": null,
"\"Computer\"DOTDOT\"Type\"": "Virtual Server"
```

Then the data you enter in the **Raw Path** field should be in the following format:

```
custom_fields|"Computer"."Status"
custom_fields|"Computer"."Type"
custom_fields|"Computer"."OS"."NT Info"."Server"
```

This format applies to both CSV and JSON.