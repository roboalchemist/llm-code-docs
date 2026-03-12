# Source: https://docs.pentaho.com/pba-report-designer/perform-calculations-in-report-designer-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/perform-calculations-in-report-designer-cp.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/perform-calculations-in-report-designer-cp.md

# Perform calculations

To use the Formula Editor, and group, summarize, and associate multiple report elements, see the following topics:&#x20;

* [Use the Formula Editor](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/perform-calculations-in-report-designer-cp/use-the-formula-editor)
* [Summarize data in groups](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/perform-calculations-in-report-designer-cp/summarize-data-in-groups)

**Note:** To create common formulas and learn how to use functions, see the topic, [Formulas and functions](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/formulas-and-functions).

## Use the Formula Editor

When adding conditional formatting or other constraints on data-driven report elements, you have the option of using a built-in Formula Editor to help you build an expression with a graphical interface. All element properties in Report Designer can have formulas. You can type in your own formula by hand, but it's much easier to use the built-in Formula Editor to build an expression.

The Formula Editor provides you with basic math and comparison operators so that you don't have to enter them manually. Also provided are concatenate and percent functions. Click the **Field Selector** to select fields in the report.

Follow the instructions below to use Formula Editor:

1. Click on the element you want to add a condition or constraint to.
2. In the **Style** pane, select the property you want to add a constraint to, then click the round green **+** icon on the right side of the field.
3. Click the **...** button.

   The Formula Editor window appears.
4. Select a function category from the drop-down box.

   The default category is All.
5. Select a function from the **Functions** list.

   If you click on a function, a description of what it does will appear in the tan-colored field at the bottom of the window.
6. Double-click on a function to bring up the option fields.
7. Erase the default values in the option fields, and replace them with your own settings.

   If you need to associate a column with a function, click the **Select Field** button to the right of the field, then select the data or function you want to use. Follow proper SQL syntax in your options; all values must be in quotes, and all column names must be in uppercase letters and enclosed in square brackets.
8. When you're done, click **OK**, then click **Close**.

You have applied a formula to a report element.

**Note:** If you want more information on formula functions, conditionals, and operators, refer to the OASIS OpenFormula reference: <http://www.oasis-open.org/committees/download.php/16826/openformula-spec-20060221.html>. Pentaho does not implement all OpenFormula functions, but the functions Report Designer includes are documented on the OASIS website.

## Summarize data in groups

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
