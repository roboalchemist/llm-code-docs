# Source: https://docs.pentaho.com/pba-report-designer/output-parameterization-by-report-designer-cp/simple-olap-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/output-parameterization-by-report-designer-cp/simple-olap-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-olap-output-parameterization.md

# Simple OLAP output parameterization

You can add dynamic interactivity to a published report so when you execute or view it, you can specify how to constrain certain parts of the query data. This process is called parameterization.

This procedure requires a Pentaho Analysis (Mondrian) data source type. You must stablish this data source and a query before continuing with the instructions below.

Perform the following steps to parameterize an OLAP-based report.

1. Open the report you want to parameterize.
2. Right-click the **Parameters** item in the **Data** pane, then select **Add Parameter** from the context menu.

   The Add Parameter dialog box appears.
3. Select or change the options according to the definitions specified in [Simple SQL Output Parameterization](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization).
4. Edit your MDX query and add parameter functions and a `WHERE` statement, as in the example below.

   ```
   with 
     set [TopSelection] as
     'TopCount(FILTER([Customers].[All Customers].Children,[Measures].[Sales]>0), Parameter("TopCount", NUMERIC, 10, "Number of Customers to show"), [Measures].[Sales])'
     Member [Customers].[All Customers].[Total] as 'Sum([TopSelection])'
     Member [Customers].[All Customers].[Other Customers] as '[Customers].[All Customers] - [Customers].[Total]'
   select NON EMPTY {[Measures].[Sales],[Measures].[Quantity] } ON COLUMNS,
     { [TopSelection], [Customers].[All Customers].[Other Customers]} ON ROWS
   from [SteelWheelsSales]
   where 
   (
   strToMember(Parameter("sLine", STRING, "[Product].[All Products].[Classic Cars]")), 
   strToMember(Parameter("sMarket", STRING, "[Markets].[All Markets].[Japan]")), 
   strToMember(Parameter("sYear", STRING, "[Time].[All Years].[2003]"))
   )
   ```
5. Click **OK** to save the query.

   **Note:** Each parameter must have its own query or data table.
6. Include the parameterized fields in your report by moving them onto the canvas.
7. Publish or preview the report.

When you run this report, you are presented with an interactive field that specifies an adjustable constraint for the column or columns you specified.
