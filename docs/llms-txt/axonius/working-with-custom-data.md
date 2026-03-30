# Source: https://docs.axonius.com/docs/working-with-custom-data.md

# Working with Custom Data

Custom fields allow you to add extra data to an asset. There are two types of custom fields:

* **Common Fields** - Also known as **Axonius Fields**, these are fields from the adapter. The field type and available values are determined by the selected field.

* **Specific Fields** - Also known as **Custom Fields**, these are tailormade fields that you create. A specific field is added only to the selected assets.

* Custom fields appear in the list of fields in the **Query Wizard** and in the **[Custom Data](/docs/asset-profile-page#managing-custom-fields)**  tab under **Adapter Connections** on the **Asset Profile** page. Custom fields can also be displayed in an asset table and [edited inline](#inline-editing-a-custom-field-on-the-assets-page).

* You can also use the <Anchor label="Axonius - Add Custom Data to Assets" target="_blank" href="/docs/add-custom-data">Axonius - Add Custom Data to Assets</Anchor> and [Axonius - Remove Custom Data from Assets](/docs/remove-custom-data) enforcement actions to add/remove custom data to/from assets returned by a query or assets selected on a relevant page.

* When you add or edit custom data or custom data fields directly from within assets pages, it can take up to 5 minutes for the new data to appear.  Until the data appears, it will not be available for use in queries.

**Permissions**

* To work with custom data on a given asset type, you need the 'Edit tags and custom data' permission enabled for that asset type.

## Adding a Custom Field to Assets

You can add a single custom field to one or more selected assets at the same time.

<Callout icon="📘" theme="info">
  Note

  It is currently not possible to add a valid IP/IPv4 address to a newly added *Network Interfaces: IPs* /*Network Interfaces: IPv4s* field.
</Callout>

**To add a custom field to assets**

1. On the relevant [Assets page](/docs/assets-page), select one or more assets.
2. From the **More Actions** menu, select **Add Custom Field**. The **Add Custom Fields** dialog opens.

<Image alt="AddNewCustomField-blank.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddNewCustomField-blank.png" />

3. Optionally, from the **Field** dropdown, [filter the list of fields](#filtering-the-list-of-fields).

4. From the **Field** dropdown, select an existing field. The **Field Type** and **Value Type** are preset (determined by the field itself).
   You can also define new custom fields. See [Creating New Custom Fields](#creating-new-custom-fields).

5. In the text field to the right, type or select a value for the field. The value must match the **Field Type** and **Value Type**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddNewCustomField-blank-red.png)
   * For **Single Value** fields, type a value.
   * For **Single Select** fields, select a predefined value.
   * For **Multiple Values** fields, add a list of values with the values separated by pressing **Enter**, a comma, or semicolon.

6. Click **Apply**. The custom field is added to the selected assets. The custom field can be selected as a column in the asset table. For each asset, the value of the field is displayed.

### Filtering the List of Fields

You can filter the list of fields so that the **Fields** dropdown displays only Custom fields, only Axonius fields, or all fields.

**To filter the list of fields**

1. Click the **Field** dropdown, and then click the Filter ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Filtericon\(1\).png) icon.

2. From the **Filter by** menu that opens, select  **Custom Fields**, **Axonius Fields**, or **All Fields** (the default). The **Field** dropdown now lists fields of the chosen Custom Field type.

<Image alt="CustomFieldsFilter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomFieldsFilter.png" />

## Creating New Custom Fields

You can create as many custom fields as you need of types **Single Value** or **Multiple Values**. These fields can be used just like any other system or adapter field.

<Callout icon="📘" theme="info">
  Note

  1. You cannot create **Single Select** custom fields from an Assets page. You can only create such fields from the [Custom Data Management](/docs/managing-custom-fields) page.
  2. Once you create a field, you can never change its **Field Type**.
</Callout>

**To add a new custom field to the system**

1. On the relevant [Assets page](/docs/assets-page), select one or more assets.

2. From the **Actions** menu, select **Add Custom Field**. The **Add Custom Fields** dialog opens (see screen in step 2 of [Adding Custom Fields to Assets](#adding-custom-fields-to-assets) above).

3. Start typing a field name in the **Field** box. It is recommended to include in a custom field name characters A-Z and 0-9 only.
   If a field of that name already exists, it is displayed. Continue to type the full name of the new field and at the bottom of the **Field** list, click **+ New Field Name**.

   <Image alt="AddNewCustomField.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddNewCustomField.png" />

<Callout icon="📘" theme="info">
  Note

  Although it is recommended to include in a Custom Field name characters A-Z and 0-9 only, special characters (i.e., characters other than A-Z and 0-9) are also supported.
  The only limitation is that the system does not support giving a new custom field a name that is the same as an existing custom field name besides for different special characters. For example: If *CustomField\*1* is a defined custom field, it is not possible to name new custom fields *CustomField$1* or *CustomField#1*.
  If you do give similar field names, when you click **Apply** to save the changes, the following notification is displayed: *Failed to Save Field*, and the field is dropped.
</Callout>

4. In **Field Type**, select one of the following:
   * **Single Value** - To create a single-value field.
   * **Multiple Values** - To create a list field.

5. In the **Value Type** list, select one of the available types:
   * When **Field Type** is **Single Value**, the following **Value Types** are available:
     * String
     * Date - See [Adding a Custom Date Field](#adding-a-custom-date-field).
     * Float
     * Integer
     * Boolean
   * When **Field Type** is **Multiple Values**, the following **Value Types** are available:
     * String
     * Date - See [Adding a Custom Date Field](#adding-a-custom-date-field).
     * Float
     * Integer

6. FIll in a value or values in the text box:
   * When the **Field Type** is **Single Value**, type a single value in the empty text box. The value is determined by the **Value Type**.
   * When the **Field Type** is **Multiple Values**, in the **Add** text box, type the list of field values. Press **Enter**, comma, or semicolon to add another value. You can click the **x** of a value to remove it, or click a value to edit it.

<Image alt="CustomFieldsList" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomFieldsList.png" />

Custom fields are marked with a user ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomFieldUserIcon.png) icon in the list of fields.

7. Click **Apply** to add the new field to the selected assets.

8. If you have **Admin** permissions, you can manage all custom fields in the system. Click **Manage Custom Fields**. You will be taken to the [**Managing Custom Fields**](/docs/managing-custom-fields) page.

## Adding a Custom Date Field

You can add one or more dates in a custom field. This is useful for instance, to identify the first time an asset was noncompliant. You can add a single or multiple date field.

**To add a single date or a list of dates**

1. On the relevant [Assets page](/docs/assets-page), select one or more assets.

2. From the **Actions** menu, select **Add Custom Field**. The **Add Custom Fields** dialog opens (see screen in step 2 of [Adding Custom Fields to Assets](#adding-custom-fields-to-assets) above).

3. Start typing in the **Field** box. If a field of that name already exists it is displayed. Continue to type the full name of the new field and at the bottom of the **Field** list, click **+ New Field Name**.

4. In **Field Type**, select one of the following:
   * **Single Value** - To add a single date.
   * **Multiple Values** - To add a list of dates.

5. Select **Date** as the **Value Type**.

6. In the rightmost text box, add a date or dates:
   * For a **Single Value** date field: Click **Select Date**.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomSingleDate.png)

   * For a **Multiple Values** date field: Click **Add Date**.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomMultipleDates.png)

7. In the Date Picker that opens, select a date in the past, present, or future.

8. Optionally, select the time on the current date. By default, the current time is 00:00 for the selected date.

9. Click **Ok** to set the date and time.

10. For  a **Multiple Values** date field, for each additional date that you want to add to the field, click **Add Date** and select a date and time (see steps 7 to 9 above).

11. Click **Apply** to add the new date field to the selected assets.

## Editing Existing Single Value or Multiple Values Custom Fields

You can edit the value of an existing custom field of type **Single Value** or **Multiple Values**, whether common (Axonius field) or specific (Custom field). You cannot edit its **Field Type**.

### Editing a Custom Field from the Add Custom Fields Dialog

**To edit a value of an existing custom field from the Add Custom Fields dialog**

1. On the relevant [Assets page](/docs/assets-page), select one or more assets.

2. From the **Actions** menu, select **Add Custom Field**. The **Add Custom Fields** dialog opens  (see screen in step 2 of [Adding Custom Fields to Assets](#adding-custom-fields-to-assets) above).

3. Optionally, from the **Field** dropdown,[filter the list of fields](#filtering-the-list-of-fields).

4. From the **Field** dropdown, select the field that you want to edit.

5. Click the **Value** field, and type the new value.

6. When you are finished adding or editing custom fields, click **Apply**.

### Inline Editing a Custom Field on the Assets Page

You can use inline editing to modify an existing value of a custom field or add a value to an empty custom field.

**To edit an existing value or add a value using inline editing**

1. On the relevant [Assets page](/docs/assets-page), configure the columns to display the custom fields you want to edit. See [Setting Page Columns Display](/docs/setting-page-columns-display) on how to configure the page columns.
2. Hover over the empty space or existing value of an asset's custom field and click the pencil icon that appears.

<Image align="center" alt="CustomField-InlineEdit.png" border={false} width="300px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomField-InlineEdit(1).png" />

3. In the **Edit** dialog, add or change the value according to the field type and click **Save Changes**.

## Editing Existing Single Select Custom Fields

You can modify, delete, or add values of an existing custom field of type **Single Select**, whether common or specific, from the Custom Data management table in System Settings.
For a complete explanation, see [Managing Custom Fields](/docs/managing-custom-fields).

## Adding Custom Fields to Query or Filter Results with a Quick Enforcement Action

You can use a quick Enforcement Action to add custom fields to all assets returned by a query.

**To add custom fields to assets using a quick Enforcement Action**

1. On the relevant [Assets page](/docs/assets-page), run a saved query or filter the Assets list.

2. From the **EC Actions** menu, select **Add custom field**. The **Add Custom Field** dialog opens.

3. In the **Enforcement Set name** field, a default value is provided. You can change this to fit your needs.

4. In **Field name**, type a name for the custom field (see **Field** in [Creating New Custom Fields](#creating-new-custom-fields)). Then, select a **Field type** and **Value type**.

5. In the **Field value** text box, type a value for the field.

6. To have this field removed from assets that do not match the query parameters, select **Remove this custom data field from entities not found in the query results (True/False)**, and then select one of the following options that open:

   * **Remove entire field** - Remove the complete custom field.
   * **Remove values field** - Remove values added to the custom field.

   A safeguard is displayed. Click **Confirm** if you want to continue.

7. To run this Enforcement Set on a schedule, toggle on **Select a Schedule Plan**  and configure the schedule you want. To learn more about running Enforcement Sets on a schedule, see [Scheduling Enforcement Set Runs](/docs/scheduling-ec-set-runs).

8. Click **Save and Run**. The custom field is saved and the notification 'Action Created Successfully' is displayed.

## Managing Custom Fields for a Specific Asset

This section describes how to view and manage all the custom data fields configured for a specific asset.

**To manage an asset's custom fields**

1. On the relevant [Assets page](/docs/assets-page), click an asset to navigate to its **Asset Profile** page.

2. In the left navigation pane, under **Adapter Connections**, select **Custom Data**.

3. In the upper-right of the Asset Profile **Custom Data**, select **Add Custom Data** `>` **Manage Custom Fields**.

<Image alt="ManageCustomFields" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-YFNM6R4C.png" />

In the **Manage Asset Custom Fields** dialog, all the custom fields related to this asset are listed.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageCustomFieldsUser.png)

From this screen, you can do the following:

* Add custom fields - Click **+ Add Custom Field** at the bottom left of the screen (scroll down), and in the field that opens,[add an existing Axonius or Custom field to the asset](#adding-a-custom-field-to-assets), or create a new Custom field ([date](#adding-a-custom-date-field) or [other](#creating-new-custom-fields)) to add to the asset.
* Delete existing custom fields - Click the trashcan icon to the right of the field.
* Add values to custom fields - Click inside the **Value** box of the field and add a value:
  * For a Single Value Boolean field, select True/False. For other Single Value fields, overtype the value with a new value.
  * For a Multiple Values field, for each value that you want to add, click **Add** and type the new value, or in the case of a Date field, click **Add Date**, and add a new date.
* Remove values from Multiple Values custom fields - Click the **x** in the tiles of the values that you want to delete. Make sure that at least one value remains.

4. When you are finished making changes, click **Save Changes**.

<Callout icon="📘" theme="info">
  Note

  * A custom field (**Single Value** or **Multiple Values**) must be defined with at least one value. If you delete all values of a custom field, clicking **Save Changes** fails and keeps the previous configuration. You can remove all values of a custom field only by removing the entire custom field from the system.

  * At the bottom left of the screen (scroll down), click **Manage Custom Fields** to open the [Custom Data Management screen](/docs/managing-custom-fields) where you can manage all Custom Fields in the system from one central location.
</Callout>