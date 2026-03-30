# Source: https://docs.pentaho.com/pba-report-designer/output-parameterization-by-report-designer-cp/advanced-sql-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/output-parameterization-by-report-designer-cp/advanced-sql-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/advanced-sql-output-parameterization.md

# Advanced SQL output parameterization

You can add dynamic interactivity to a published report so when you execute or view it, you can specify how to constrain specific parts of the query data. This process is called parameterization.

This procedure requires a JDBC (Custom) data source type. You must establish this data source before continuing with the instructions below. You do not need to construct a query yet.

**Note:** This option allows you to parameterize both structure and values. If you only need to parameterize values, see [Simple SQL output parameterization](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization) instead.

Perform the following steps to parameterize a report by creating a custom formula.

1. Open the report you want to parameterize.
2. Right-click the **Parameters** item in the **Data** pane, then select **Add Parameter** from the context menu.

   The Add Parameter dialog box appears.
3. Select or change the options according to the definitions specified in [Simple SQL Output Parameterization](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization).
4. Go to the **Structure** pane, then select **Master Report**.
5. In the **Attributes** pane, click the round green Plus Sign (**+**) in the name field of the **Query** section.

   The Expression window appears.
6. Click the Ellipses button .

   The Formula Editor appears.
7. In the **Formula** field, use a `SELECT DISTINCT` statement to parameterize the data structure with your previously defined parameter, as shown in the example below.

   ```
   ="SELECT DISTINCT " & *\[paramexample\]* & " AS COL1 FROM PRODUCTS"
   ```

   The *paramexample* is a placeholder for the name of the parameter you created earlier. `COL1` is the example name of the element to be parameterized in your report, and `PRODUCTS` is an example table name in your database.

   **Note:** The spaces after `DISTINCT` and before `AS` are important. Do not omit them.
8. Click **OK** when you are done with the query, then click **Close** in the Expression window.
9. Add a field of the applicable data type to your report, and name it according to the `AS` statement you defined in your query.

   In the example above, the name of the text field would be `COL1`.
10. Publish or preview the report.

When you run this report, you are presented with an interactive field that specifies the source of the column you specified.
