# Source: https://docs.axonius.com/docs/managing-custom-enrichment.md

# Managing Custom Enrichment

Axonius supports **Custom Enrichment Management** to enable managing *all* Custom Enrichment fields created in the system from one central location. This includes Custom Enrichment fields that have been created using the [Custom Enrichment - Enrich assets with CSV file](/docs/add-enrichment) Enforcement Action (recommended) and those created from [System Settings](/docs/configuring-enrichment-settings).

The **Custom Enrichment Management** table shows information on each field, and enables you to navigate directly from the row of a Custom Enrichment field to the assets enriched with this field.

Only users assigned the **Update system settings** permission (default for admins) can manage Custom Enrichment fields.

Custom Enrichment fields are supported for all asset types.

**To manage Custom Enrichment fields**

1. From the top right corner of any page, click ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the **System Settings** page, expand **Data**, and select **Custom Enrichment Management**. The **Custom Enrichment Management** page opens.

![CustomeEnrichmentManagementTableB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomeEnrichmentManagementTableB.png)

By default, the table includes all Custom Enrichment fields - those with and without affected assets. To see a list of fields with no affected assets only, toggle on **Show fields with no Affected Assets**. The list updates automatically every hour. The **Last updated** field indicates the date and time that the list was last updated.

The following information is included for each field:

* **Field Name** - The name of the field.
* **Field Type** - The type of field.
* **Value Type** - The type of data the field accepts.
* **Asset Type** - The asset type to which the field applies.
* **Adapter** - The icon of the adapter from which the field was fetched.
* **Affected Assets** - The number of affected assets for which the field has values. You can click the number link to navigate to the Assets page showing the assets enriched with the Custom Enrichment field.
* **Field Values** - The values assigned to the field. Values appear when the Custom Enrichment field is assigned to assets. The first few values are displayed in the column followed by a blue number link showing the number of additional values, if they exist. You can hover over the link to view a table of all field values.

## Refreshing the Table

The table updates automatically every hour or when you create a new Custom Enrichment field.
Click the Refresh icon ![RefreshSymbol.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefreshSymbol.png) at any time to manually update the table.

![RefreshSymbol(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefreshSymbol\(1\).png)

## Filtering and Searching for Custom Enrichment Fields

Use the filter bar at the top of the page to select criteria to filter the **Custom Enrichment Management** table. The table can be filtered by:

* **Field Type** - Display one or more of the following types of Custom Enrichment fields: *Single Value*, *Single Select*, or *Multiple Values*.

* **Value Type** - Display one or more of the following types of values that the Custom Enrichment fields accept: *String*, *Date*, *Float*, *Integer*, or *Boolean*.

* **Asset Type** - Display Custom Enrichment fields relevant for the selected asset type.
  * From the **Asset Type** dropdown, select one or more asset types to return the Custom Enrichment fields that apply to these asset types. For example: *Users*, *Application Settings*, *Devices*, *Tickets*. The assets in the dropdown are listed according to asset category (as on the Assets page). In addition, it is possible to type and search to easily locate in the dropdown, the asset type required.
    ![ModulesCustomDataManagement](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ModulesCustomDataManagement.png)

* **Adapter** - Display Custom Enrichment fields from one or more adapters.

You can also search the table according to **Field Name**, **Field Type**, or **Asset Type** by entering a search string in the **Search** field.

This table is updated as soon as filter criteria are selected or a search string entered.

Click the column headers to sort the table.

## Exporting the List of Custom Enrichment Fields to CSV

You can export the list of Custom Enrichment fields to a CSV file. Only the currently listed items are exported.

**To export the list of Custom Enrichment fields**

* Click **Export CSV**. The file is generated and downloaded to the local computer.

## Performing Actions on Custom Enrichment Fields

### Deleting Custom Enrichment Fields

From the **Custom Enrichment Management** table, you can delete one or more Custom Enrichment fields. The deleted fields are removed from all affected assets.

**To delete a Custom Enrichment field**

1. In the **Custom Enrichment Management** table, hover over the row of a Custom Enrichment field, and then at the end of the row, click the **Delete** icon ![DeleteIconB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteIconB.png) or select the checkboxes of one or more Custom Enrichment fields (the number of selected records is displayed next to the **Total** results), and then on the top right of the table, click the **Delete** action ![DeleteAction(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteAction\(1\).png).
   You can also select all records on the page (mark the top left checkbox) or in the table (**Select All**), or clear your entire selection (**Clear All**).
   The system asks you to confirm the deletion.

![DeleteFieldConfirmation](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteFieldConfirmation.png)

2. Click **Delete Fields**. The selected Custom Enrichment fields are completely deleted from the system. This cannot be undone.