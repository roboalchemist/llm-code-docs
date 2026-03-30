# Source: https://docs.axonius.com/docs/using-the-syntax-helper.md

# Using the Syntax Helper

You can create a Dynamic Value statement (also referred to as "statement") to add dynamic values to the fields in an Enforcement Action configuration from the assets themselves. The Syntax Helper makes it easy to find the Enforcement Action fields that you want to populate, as well as the adapter fields (Asset and Relationship fields) that determine the values in the Enforcement Action fields.

Enforcement Action statements must include field names used in the Axonius database (and not the names displayed in the Axonius application).

To learn more about field syntax, see [Statement Concepts](/docs/condition-statement-concepts).

<Callout icon="📘" theme="info">
  Note

  * Autocomplete shows available options for Enforcement Action fields in the statement (but not for adapter fields - (asset and relationship fields)). You can choose a relevant action field name from the Autocomplete options instead of going into the Syntax Helper to find and copy the field name.

  * **Action Form** refers to the Enforcement action configuration dialog. The Syntax Helper **Action Form Fields** tab shows under **Field Name (UI)** the list of required and additional fields by their User Interface names in the configuration dialog of the selected Enforcement Action. Each Enforcement Action has its own set of fields, and only those field names appear in the Syntax Helper and in the Autocomplete options.

  * **Field Name in Statement** shows the corresponding field name in the Axonius database, and **Type** / **Value Type** shows the type of field (such as array, integer, string, bool).

  * An aggregated field or a field in a complex field is always defined as array.

  * When you use the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) to construct Dynamic Value statements, you choose the adapter and Enforcement Action fields from dropdowns, and do not need to use the Syntax Helper.
</Callout>

The following procedure describes how to construct a statement in the **Define the statement** text box using Syntax Helper and Autocomplete.

**To construct a statement using Syntax**

1. Above the **Define the statement** box, click **Syntax**.
2. Determine the [Asset fields](#adding-an-asset-field-to-a-statement) and/or [Relationship fields](#adding-a-relationship-field-to-a-statement) whose values you want to work with, using the **Syntax Helper** to get the correct database field names and copy them.

<Callout icon="📘" theme="info">
  Note

  Each retrieved database field name is enclosed in square brackets \[] so that it can be pasted into the statement as is according to the required statement syntax.
</Callout>

2. Determine the Action Form field you want to populate with values from the Asset and/or Relation fields, using one of the following methods:
   * Choose from the Autocomplete suggestions.
   * Use the Syntax Helper to get the correct field names and copy them. See below [how to add an action form field to the statement](#adding-an-action-form-field-to-a-statement).
3. With the help of Autocomplete, choose the [functions and operators](/docs/using-functions-and-keywords) necessary to produce the values that you want in the Action form field.
4. When you have completed entering the statement, click **Validate** for the system to [automatically verify the statement syntax](#validating-the-statement).
5. After validating the Dynamic Value Statement, you can click **Simulate** to [debug the statement](/docs/using-the-simulator).

## Adding an Asset Field to a Statement

The Syntax Helper enables you to select under the **Asset Fields** tab the adapter field used in the Dynamic Value statement to configure the field in the configuration dialog (form). This tab provides the following information for each selected asset field:

* **Field Type** - The type of field. For example, **Single Value**, **Multiple Values**, **Single Select**, **Multiple Select**.
* **Value Type** - The type of value in the field. For example, **bool**, **integer**, **float**, **string**, **date**, **array**, **array (string)**, **number**
* **Field Name in Statement** - The Axonius database name of the field enclosed in \[].

**To select and copy an Asset field into the statement**

1. Click **Syntax Helper** and in the screen that opens, click the **Asset Fields** tab. In the **Asset Fields** tab that opens, the **Module** dropdown is automatically filled with the asset type that you selected in the Enforcement Set query **Module** dropdown (in the **Select Assets** tab).

<Callout icon="📘" theme="info">
  Note

  It is not possible to select or change the asset type from the **Module** dropdown in the **Asset Fields** tab of the Syntax Helper. If you have not selected the asset type in the Enforcement Set Query, the Select field dropdown will not show relevant fields.
</Callout>

3. Under **Select Adapter Field**, from the Adapters dropdown, select an adapter, and then from the **Select Adapter Field** dropdown, select one of the adapter fields. The following is displayed for the selected field: **Field Type**, **Value Type**, and **Field Name in Statement**.

<Image alt="SyntaxHelperActionFormFieldsNewB" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperActionFormFieldsNewB.png" />

4. Click the Copy icon to the right, click **Close**, and then paste the field name into the statement.

<Callout icon="📘" theme="info">
  Note

  * The **Adapter Connection Label** field is not supported. Instead, you can use the **Last Fetched From Connection Label** field, which is set with the value of the existing connection label of the connection.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperLastFetchedIFTTT.png)
</Callout>

### Aggregated and Preferred Fields in the Syntax Helper

An **Aggregated field** contains data fetched from different adapters. For example, it can contain several Host Names, each one collected from a different adapter. As an Aggregated field can contain a list of values, it is defined as a list (array).
A **Preferred field** displays the most authoritative value for a specific piece of information when there are multiple values for a given asset. For example, the **Preferred Host Name** field has the most common host name value out of all the **Host Name** field values fetched for any given device. The Preferred fields values are calculated as part of each global discovery cycle and also every number of hours as specified.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperPreferred.png)

The field name is enclosed in \[] and ends with \_preferred. For example: *\[device.specificdata.data.hostnamepreferred]*

When creating a statement with concat, join, or other operators, it is important to choose the correct type of field (single value, list of values).

### Complex Fields in the Syntax Helper

A **Complex field** contains objects (subfields, keys), which can be of any data type, and can be complex fields themselves. You can include  in a Dynamic Value statement a complex field path, as well as its objects.

For example, in the following screen, the asset profile of a device shows the **Adapter Tags** complex field in **All Fields**.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetProfileAdapterTags.png)

Clicking the **Adapter Tags** complex field opens the **Adapter Tags** table with one column per object - **Tag Key**, **Key Value**, **Tag Source**.

<Image alt="AdapterTagsComplexField" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterTagsComplexField.png" />

You can copy a complex field path and its objects into a Dynamic Value Statement using the Syntax Helper.

**To copy a complex field and its objects into a Dynamic Value statement**

1. In the Syntax Helper, select an adapter from the Adapters list, and in **Select Adapter Field**, search for or select the complex field (in this example, **Adapter Tags**).
2. Copy the field for use in the statement, as follows:
   * To copy a complex field path: Select the complex field required for the statement and then click the adjacent Copy icon. The complex field's Axonius database full path name is copied.
   * To copy an object of a complex field: Selecting a complex field shows all its objects. Select the object required for the statement  (screen below) and then click the adjacent Copy icon. The object's Axonius database full name - path followed by object, is copied, enclosed in \[].
3. Click **Close**.
4. In the Enforcement Action configuration dialog, paste the copied field into the statement.
   * For the complex field path (as in \[adapter\_complex\_field\_path] in the by\_key function), use the name from the Syntax Helper as is.
   * For an object of a complex field (as in key\_to\_search\_by and key\_to\_pick in the by\_key function),  you can remove the full path preceding the object name in the statement. For example, for **AWS Tags: AWS Tag Key**, instead of using the full syntax **device.adapters\_data.aws\_adapter.aws\_tags.key**, you can use **tags.key** in the statement.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperAdapterTagsDropDown.png)

See [a detailed example of a dynamic value statement using the by\_key function with complex field path and objects](/docs/using-functions-and-keywords#using-the-by-key-function-for-complex-field-objects).

### Custom Data Fields in the Syntax Helper

You can [add custom data fields to selected assets on an Asset page from the **Actions** menu](/docs/working-with-custom-data#adding-a-custom-field-to-assets), or to all assets returned by a query using the [**Axonius - Add Custom Data to Assets**](/docs/add-custom-data) enforcement action.
To learn more about using existing custom data fields and creating new ones, see [Working with Custom Data](/docs/working-with-custom-data).

When you create a Custom Data field, the field name assigned to it depends on the selected field type.

You can use a Custom Data field in a Dynamic Value statement.

**To select a Custom Data field from the Syntax Helper**

1. In the **Asset Fields** tab, from the adapter dropdown, select the **Custom Data** adapter.
2. From the **Select Adapter Field** dropdown, select a relevant field, and from under **Field Name in Statement**, click the Copy icon to copy the relevant field (enclosed in \[]) into the statement.

<Image alt="SyntaxHelperCustomData" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperCustomData.png" />

## Adding a Relationship Field to a Statement

In the **Relationship Fields** tab of the Syntax Helper, you input the related asset type, relationship, and related asset field, and the system automatically returns the syntax of the Relationship field, i.e., the syntax of the adapter field in the related asset (i.e., an asset that is related to the Enforcement Action asset) based on a [Relationship](/docs/exploring-connections-and-asset-relationships). You can then copy the related asset field directly into the Dynamic Value statement so that its value can be used to configure the field in the configuration dialog (form).

**To select and copy a related asset field into the statement**

1. Above the Dynamic Value statement, click **Syntax Helper**, and in the dialog that opens, click the **Relationship Fields** tab.
2. From the **Select Asset Type** dropdown, select the type of the related asset from which to fetch the field.
3. From the **Select Relationship** dropdown, select a Relationship.
4. Under **Select Field**, from the Adapters dropdown, select an adapter, and then from the **Select field** dropdown, select one of the adapter fields. The information for the selected related asset field is displayed under the following columns:
   * **Field Type** - The type of field. For example, **Single Value**, **Multiple Values**, **Single Select**, **Multiple Select**.
   * **Value Type** - The type of value in the field. For example, **bool**, **integer**, **float**, **string**, **date**, **array**, **array (string)**, **number**
   * **Field Name in Statement** - The Axonius database name of the field in the format *relation.asset type("relationship name").adapter\_field* enclosed in \[].
5. Click the copy icon to the right, click **Close**, and then paste the field name into the Dynamic Value statement.

In the following example:

* In **Select Asset Type**, select **Disks** as the asset type of the related asset.

* In **Select Relationship**, select **Has**, a defined Relationship.

* In **Select Field**, select the **Asset Type** field from the Axonius adapter.

The Field Type, Value Type, and Database Field Name of the Disk asset type are displayed.

<Image alt="SyntaxHelperRelationshipField" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperRelationshipField.png" />

You can copy the related asset field name into the Dynamic Value statement.

```
device all then form.field_value set_value [relation.disk("Has").specific_data.data.asset_type]
```

## Adding an Action Form Field to a Statement

The Syntax Helper presents under the **Action Form Fields** tab all the field names used in the configuration dialog (form) available for all Field type, Value type combinations. This tab includes the following information:

* **Field Name (UI)** - Field name used in the user interface
* **Type** - The field type
* **Field name in statement** - The Axonius database name with an adjacent copy icon, enabling you to copy the field directly from the Syntax Helper into the statement.

The [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) and Autocomplete also present all possible choices. From this list, you should choose a field name that corresponds to the Field type, Value type combination configured in the Enforcement Action.

The following table includes the field names for some **Field type, Value type** combinations (first column in the table) in the Add Custom Data EC, followed by the three columns as they appear in the Syntax Helper under **Action Form Fields** (**Field Name (UI)**, **Type**, and **Field name in statement**).

| Field type, Value type (in EC) | Name in GUI | Type    | Field name in statement         |
| ------------------------------ | ----------- | ------- | ------------------------------- |
| Single value, String           | Field value | string  | form.field\_value               |
| Single value, Date             | Set date    | string  | form.field\_date.specific       |
| Single value, Float            | Field value | number  | form.field\_number              |
| Single value, Integer          | Field value | integer | form.field\_integer             |
| Single value, Boolean          | Field value | bool    | form.field\_on                  |
| Multiple values, String        | Field value | array   | form.field\_list.value          |
| Multiple values, Date          | Field value | array   | form.field\_list\_date.value    |
| Multiple values, Float         | Field value | array   | form.field\_list\_number.value  |
| Multiple values, Integer       | Field value | array   | form.field\_list\_integer.value |

<Callout icon="📘" theme="info">
  Note

  When you create a Dynamic Value Statement for adding a custom date field, make sure to use **form.field\_date.specific** with **Date type** set to **Specific date**, as a dynamic date can be written only to this type of Date field. Do not use **form.field\_date.now** or a field with **Date type** set to **Now**, as this type of field cannot accept dynamic input and regardless of the statement, its value is always the action runtime.
</Callout>

**To copy an Action form field into the statement (using Syntax Helper)**

1. Click **Syntax Helper**. The fields from the selected Enforcement Action configuration dialog are listed in the **Action Form Fields** section under the **Field Name (UI)** column.
2. Hover over one of the Action form fields and click the copy icon that appears to the right of the **Field name in statement** entry. The field name is copied to the system clipboard.
3. Click **Close** and paste the field name into the statement.

   <Image align="center" alt="SyntaxHelper-ActionFormField.png" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelper-ActionFormField.png" />

## Validating the Dynamic Value Statement

Once you have completed entering a Dynamic Value statement in the **Define the statement** box, you can click **Validate** for the system to automatically verify that the statement syntax is valid.

* If the statement syntax is correct, the following notification appears in green under the **Define the statement** box: *Statement was validated successfully*.
* If the statement syntax is incorrect, the following notification appears in red under the **Define the statement** box: *Statement validation failed at* followed by the location of the error and the error. In this case, correct the error and **Validate** again.