# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/perform-calculations-in-report-designer-cp/summarize-data-in-groups.md

# Summarize data in groups

You can sort data in multiple fields by creating groups.

Perform the following steps to summarize data in groups:

1. Double-click on your data source to open the query configuration dialog.
2. Reorder your query so that the fields you want to sort by are listed at the beginning of your `SELECT` statement.

   If you use the SQL Query Designer to do this, you can simply drag and drop the columns in your `SELECT` section to change their order; if you use the query window, you can carefully copy and paste the columns to reorder them.
3. Copy the same columns you reordered in the `SELECT` section into the **ORDER BY** section, in the same order you specified previously.

   ```
   SELECT
       `PRODUCTS`.`PRODUCTLINE`,
       `PRODUCTS`.`PRODUCTVENDOR`,
       `PRODUCTS`.`PRODUCTNAME`,
       `PRODUCTS`.`PRODUCTCODE`,
       `PRODUCTS`.`PRODUCTSCALE`,
       `PRODUCTS`.`PRODUCTSCALE`, 
       `PRODUCTS`.`PRODUCTDESCRIPTION`,
       `PRODUCTS`.`QUANTITYINSTOCK`,
       `PRODUCTS`.`BUYPRICE`,
       `PRODUCTS`.`MSRP`
   FROM
       `PRODUCTS`
   ORDER BY
       `PRODUCTS`.`PRODUCTLINE` ASC,
       `PRODUCTS`.`PRODUCTVENDOR` ASC,
       `PRODUCTS`.`PRODUCTNAME` ASC
   ```
4. Save the query and close the configuration window.
5. Right-click the **Groups** category in the **Structure** pane, and select **Add Group** from the context menu.
6. Type in a name for this group in the **Name** field.
7. In the **Available Fields** area on the left, select each row you want to add to the group, then click the arrow button to move it to the **Selected Fields** area on the right.
8. Select the **Data** pane, then click **Add Function**.
9. Double-click the **Sum** function category, then select **Sum**, then click **Add**.
10. Select the newly created **TotalGroupSumFunction** item in the **Functions** list, then click on the **Reset on Group Name** property in the lower right pane.
11. Click the **\[...]** button, select the group you just created in the list, then click **OK**.

You now have the proper Report Designer configuration to create a report with data sorted in groups. You can test this by adding text and number fields to your group and details bands, connecting them to the columns and functions you defined earlier, and previewing your report.
