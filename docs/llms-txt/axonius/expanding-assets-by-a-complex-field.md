# Source: https://docs.axonius.com/docs/expanding-assets-by-a-complex-field.md

# Expanding Assets by a Complex Field

Generally, each row in an Assets table represents an asset entity containing data from every adapter connection. However, you can choose instead to expand each row by data from a complex field that is most interesting to you, and explore assets in the context of that specific field.
Complex fields are fields that are made up of a number of different parameters (nested fields) and can be presented in a table view. For a detailed explanation on complex fields and how to view and manage them, see [Asset Profile Page - Complex Fields](/docs/asset-profile-page-complex-fields).

<Callout icon="📘" theme="info">
  Note

  This capability is available for all asset types.
</Callout>

## Selecting a Complex Field to Expand Assets By

From any **Assets** page:

1. Click **Edit Table**, then select **Expand Assets by**.
   ![EditTableExpandAssetsBy](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-CBS3EHRT.png)

2. Select a complex field from the dropdown list. You can only select one field at a time.
   The complex fields available for selection depend on the columns currently displayed in the table. You can only select a complex field that has at least one of its nested fields displayed in the table. In the example shown here, the **Network Interfaces** complex field is available for selection because two of its nested fields are displayed in the table: **Network Interfaces: MAC** and **Network Interfaces: IPs**.

![expand2](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ZGIU6OUM.png)

3. To expand assets by a different complex field, first you need to add one of its nested fields to the table. Click **Edit Table** and then select **Edit Columns**.
   For example, to expand assets by the **Installed Software** complex field, add the **Installed Software: Software Name** field (or any other nested field) to the table.

<Image align="center" alt="expand3" width="800px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-W7VRIE4Q.png" />

For more information, see [Adding or Removing Fields](/docs/expanding-assets-by-a-complex-field#/adding-or-removing-fields).

<Callout icon="📘" theme="info">
  Note

  The **Adapter Connections** field is the default option to expand assets by.
</Callout>

## Exploring the Expanded Assets

In the following example, we expanded the **Devices** table by the **Installed Software** complex field. In the updated view, expanding each device’s row displays a list of all software installed on this device. For each row, the source adapter is displayed under the **Adapter Connections** column.

![expand4](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-NKSD9Q24.png)

If there are more than 50 rows on the list, click **View all X Results** at the bottom of the 50th row to view the full list of results in the **Asset Profile** page.

<Image align="center" alt="expand5" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/expand5.png" />

This view lists all software installed on the device and their details, such as version, vendor, source, etc.

![expand6](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/expand6.png)

To go back to the original view, select **Expand by** `>` **Adapter Connections** (the default option) or click **Reset**.

### Adding or Removing Fields

You can add to the table as many nested fields of the expanded complex field as you like, and the expanded view will update accordingly.
For example, if you add both the **Installed Software: Software Name** and **Installed Software: Software Vendor** fields, and select **Expand assets by** `>` **Installed Software**; in the updated view, each expanded row lists all software installed on the device **and** their vendors.

<Image align="center" alt="expand7" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/expand7.png" />

If you remove one of the nested fields, the table is still expanded by the same complex field and shows data from the remaining nested fields.
For example, if you remove the **Installed Software: Software Name** field from the above view, each expanded row still lists the software vendors.
If you remove all nested fields, the table goes back to its original view, and the option to expand assets by the complex field you selected is no longer available.

### Filtering Expanded Asset Data

Filter the data listed in the nested fields using the Query Wizard so that it only shows values that interest you.
In the following example, the **Devices** table is expanded by the **Installed Software** complex field. Each row lists data regarding the software installed on each device, such as Software Name, Vendor, End-of-Life/Support information, etc.

<Image align="center" alt="ExpandedInstalledSoftwareTable" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_profile/Expanded_InstalledSoftware.png" />

To filter data by, for example, devices whose Installed Software Vendor is Apache, run the following query. To hide every other vendor from view, click the **Refine Data** button next to the Software Vendor filter and select **Refine value by condition**.

<Image align="center" alt="RefineDataByVendorQuery" width="600px" src="https://files.readme.io/3d0adb88042f1e440a4dbe13cb8c5a1dd469c938a9be741b67b71f489cb3d005-image.png" />

Now, in each expanded row, the **Installed Software: Software Vendor** field is empty for each vendor other than Apache.

<Image align="center" alt="RefinedVendorResult" width="600px" src="https://files.readme.io/ba7a66e509792d61a0626b0cf16c568f9fe0a38af52fcdbf49171eb142f6a7fe-image.png" />

While filtering and refining data from the Query Wizard is most recommended, you can also do it from the **Refine Data Display** dialog. Note that the complex field tab is automatically added to the dialog when you choose this option, and you can apply filters from there. For more information, see [Refining the Data Displayed in Table Columns and Rows](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows).

### Sorting Expanded Asset Data

You can sort the data listed in the nested fields so that the rows will be displayed in an ascending or descending order. Hover over the sorting icon to the right of each column header to sort the data as you like. For example, sort the **Installed Software: Software Version** column in a descending order of version:

<Image align="center" alt="SortExpandedDataDescending" width="250px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_profile/ExpandedSorted.png" />

## Exporting Asset Data to CSV

An expanded view does not affect the functionality of exporting asset data to CSV or the structure of the CSV file. For complex fields and lists, you can create a CSV file where the values of complex fields and lists are represented as separate rows in the file. Do this by selecting  **Split by field value** in the **Export Data** dialog. For more information, see [Exporting Asset Data to CSV](/docs/exporting-devices-data-to-csv).

## Saved Views with Expanded Assets

You can save a view with a selected complex field to expand the assets by. Every time you apply this view from your **Saved Views** list, the assets are expanded by this field by default.

For more information on saved views and how to create them, see [Saved Views](/docs/setting-page-columns-display#saved-views).

The option to expand assets by a complex field is displayed at the bottom of the **New View** dialog.

1. Click **Expand Assets by**.
2. A **Select column** dropdown appears. Select the complex field you want to expand assets by.
3. Remember that the complex fields available for selection depend on the columns currently displayed in the table. To expand assets by a different complex field, add one of its nested fields within the **New View** dialog, and the **Select column** list will update accordingly, as demonstrated below.

   ![NewViewExpandAssetsBy](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_profile/ExpandedExpandBy.png)
4. Click **Save**.

## Saved Queries with Expanded Assets

You can save a query with a selected complex field to expand the assets by. Every time you run this query, the assets are expanded by this field by default.

For more information on how to save queries, edit and manage them, see [Saved Queries](/docs/saved-queries-devices).

The fact that a query has expanded assets is indicated inside the **Saved Query** drawer. Refer to [Viewing and Editing Query Details](/docs/managing-queries#viewing-and-editing-query-details) to learn more about this component.

In the following user query example, the bottom of the query drawer that assets are expanded by the **Associated Devices** complex field. Note that this is possible due to the fact that the **Associated Devices: Device Name** nested field is included in the table, as listed under **Query Column Display**.

![QueryExpanded](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-VNMQMN2L.png)