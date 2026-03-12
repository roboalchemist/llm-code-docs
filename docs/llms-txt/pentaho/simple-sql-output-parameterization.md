# Source: https://docs.pentaho.com/pba-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization.md

# Simple SQL output parameterization

You can add dynamic interactivity to a published report such that when you execute or view it, you can specify how to constrain certain parts of the query data. This is called parameterization. This procedure requires a JDBC data source type.

**Note:** You can only use this procedure to parameterize data returned by a query. You cannot use a `WHERE` statement to dynamically choose columns or change the structure of tabular data. If you need to go beyond the capabilities of the method explained in this section, see [Advanced SQL output parameterization](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/advanced-sql-output-parameterization) to create a custom formula instead.

Perform the following steps to parameterize a report by adding an SQL `WHERE` statement to your query.

1. Open the report you want to parameterize.
2. Click the **Data** tab in the upper right pane.
3. Right-click the **Parameters** item in the **Data** pane, then select **Add Parameter** from the context menu.

   The Add Parameter dialog box appears.

   ![Add Parameter dialog](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-846c9ed9de53bde5d4b024437c45fd5e7c51c559%2FReportDesigner_AddParameterDialog.png?alt=media)
4. The table below describes each of the options for configuring the parameters:

   | Field                       | Purpose                                                                                                                                                                                                                              |
   | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | **Name**                    | The name of the parameter in Report Designer.                                                                                                                                                                                        |
   | **Label**                   | The label of the parameter that is shown to report readers.                                                                                                                                                                          |
   | **Label formula**           | A formula that dynamically changes the name of the parameter on the report.                                                                                                                                                          |
   | **Value Type**              | The data type of the column you selected in the **Value** field.                                                                                                                                                                     |
   | **Data Format**             | Determines how the data specified by the **Value Type** is formatted. This field is especially useful when formatting dates and timestamps.                                                                                          |
   | **Data Format formula**     | A formula that dynamically changes the value of the **Data Format**.                                                                                                                                                                 |
   | **Default Value**           | The default value for the parameter. For a parameter with multiple values, the values are specified as arrays.                                                                                                                       |
   | **Default Value Formula**   | A formula that dynamically changes the **Default Value** or values.                                                                                                                                                                  |
   | **Post-Processing Formula** | A formula that updates a selected parameter. This formula is executed when a parameter is submitted, and can be used to validate parameter input. For example, you can change all text to be upper case.                             |
   | **Mandatory**               | Specifies whether this parameter is required to display any data in the report.                                                                                                                                                      |
   | **Hidden**                  | Specifies whether to hide the parameter from displaying when the value is already passed in a session variable. This option can be used in combination with the **Post-Processing Formula** option to create a calculated parameter. |
   | **Hidden formula**          | A formula to hide a parameter when the formula evaluates to TRUE. If left blank, the selected parameter is hidden when the **Hidden** check box is selected.                                                                         |
   | **Display Type**            | The parameter type.                                                                                                                                                                                                                  |
   | **Query**                   | A list of queries that you have already defined. Use the toolbar above the left pane to define a new query.                                                                                                                          |
   | **Value**                   | Field in the data source that is substituted in the query.                                                                                                                                                                           |
   | **Display Value Formula**   | A formula that changes the contents inside the list or drop-down menu in the report.                                                                                                                                                 |
5. Edit your target data source by double-clicking its entry in the **Structure** pane.
6. Below your **FROM** statement, add a `WHERE` statement that specifies which column you would like to query the user about. Assign it to a parameter that has a name descriptive enough for users to understand.

   This column should be one of the columns you have a `SELECT` statement for in the same query.
7. Click **OK** to save the query.
8. Include the parameterized fields in your report by dragging them onto the canvas.
9. Publish or preview your report.

When you run this report, you are presented with an interactive field that specifies an adjustable constraint for the column you specified.

In the example below, the constraint would be a specific product line from the `PRODUCTLINE` column of the `PRODUCTS` table.

```
SELECT
                PRODUCTLINE,
                PRODUCTVENDOR,
                PRODUCTCODE,
                PRODUCTNAME,
                PRODUCTSCALE,
                PRODUCTDESCRIPTION,
                QUANTITYINSTOCK,
                BUYPRICE,
                MSRP
FROM
                PRODUCTS
WHERE PRODUCTLINE = ${ENTER_PRODUCTLINE}
ORDER BY
                PRODUCTLINE ASC,
                PRODUCTVENDOR ASC,
                PRODUCTCODE ASC
```
