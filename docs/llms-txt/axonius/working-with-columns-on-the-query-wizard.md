# Source: https://docs.axonius.com/docs/working-with-columns-on-the-query-wizard.md

# Working With Columns and Rows on the Query Wizard

## Adding Fields to Column / Removing Fields from Column

On each row in the **Query Wizard**, the **Add Field to Column** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1549\).png) or **Remove Field from Column** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/platform/RemoveFieldFromColumn.png) button is present. This button is enabled after a field is selected for the expression.
Use this button to add or remove fields as columns in the asset table directly from the **Query Wizard**.
A column is always added as the second column in the table.
The state of this button (Add or Remove) is determined by whether the field already exists as a column in the table.

## Duplicating Rows

The **Duplicate Row** button ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1547\).png) is displayed on each row in the **Query Wizard**.

* Click **Duplicate** on the first row to duplicate the entire block.
* Click **Duplicate Row** on any of the inner rows to duplicate only the selected row.

## Disabling / Enabling Query Expression

<Image alt="ToggleEye_Query" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ToggleEye_Query.png" />

Toggle the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Eye_icon.png) **(Eye)** icon to disable/enable the query expression in a row. Use this to compare the results of a query expression without needing to delete it.

## Refine Field Values

You can either refine the field values by condition or by Asset Entity.
Click the **Refine Field Value** icon,  the **Refine values** menus appears. Select either **Refine value by condition** or **Refine asset entities by condition**.

<Image alt="NEW_Refinebyasset entity" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NEW_Refinebyasset%20entity.png" />

### Refining Field Values by Condition

Use  **Refine Field Values** to filter which values appear in the defined column. Sometimes the result of a query returns assets which have more than one value in some of the columns, for instance, installed software. You can create a filter for such columns when you create a query in the query wizard, and define which values will be searched for in these columns. When you click the **Refine value by condition** button, the asset display page shows only the values chosen in the column which is filtered.
Once you choose a field, the value is automatically added to the assets page, and saved as part of the saved query, when you save it.

To refine a field value,  the field you want to filter on must appear in the results table.
Click the **Refine Field Value** icon  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/columnFiltericon.png). The expression you created is now applied as a refinement rule for the items in the columns selected.
For instance the query below, shows Installed Software of a certain name.

<Image alt="ColumnFilterUpn.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ColumnFilterUpn.png" />

### Refine Asset Entities by Condition

You can use refine asset entities by condition to set the query to refine the contents of the asset entity that are displayed according to the rows, for instance, you can hide a row, an asset entity, which contains a Software Version with a specific value. Once you choose a field, the field is automatically added as a column to the assets page  and saved as part of the saved query, when you save it.  The query result will only show the asset entities that have this field with this value. For instance, if you select Host name that contains Win, the query result will only show rows that contain this hostname, only the rows that contain the fields and values defined in the query.
It is possible to select both **Refine value by condition** or **Refine asset entities by condition**.

* Once you click the **Refine Field Value** icon, it is displayed as ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ColumnFitlerIcRemove.png). Click the **Remove Filter** icon to remove the field value refinement, and display all information about all assets received in the query.

<Callout icon="📘" theme="info">
  Note

  The refining field values does not affect the data which is fetched, only the display.
</Callout>

### Refine by All Values

You can use **Refine by All Fields** to  refine all the conditions in the Query Wizard using a single button, without having to configure a specific data refinement for each row. All columns in the query are automatically added to the asset table, and saved as part of the query when you save it. When you select **Refine all Fields**,  you can select whether to refine the values by condition, or by asset entities, or both and  all the columns are added to the table, and the data is refined   for all  of the rows in the query in one go.

<Image alt="RefineAllFieldsNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefineAllFieldsNew.png" />

When you select **Clear all refinements**, the filters set are removed, but any columns added to the Assets table remain, and are saved as part of the query.