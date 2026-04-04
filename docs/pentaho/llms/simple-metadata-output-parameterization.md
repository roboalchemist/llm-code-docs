# Source: https://docs.pentaho.com/pba-report-designer/output-parameterization-by-report-designer-cp/simple-metadata-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/output-parameterization-by-report-designer-cp/simple-metadata-output-parameterization.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-metadata-output-parameterization.md

# Simple metadata output parameterization

You can add dynamic interactivity to a published report so when you execute or view it, you can specify how to constrain specific parts of the query data. This process is called parameterization.

This procedure requires a metadata data source type. You must stablish this data source and a query before continuing with the instructions below.

Perform the following steps to parameterize a metadata-based report.

1. Open the report you want to parameterize.
2. Right-click the **Parameters** item in the **Data** pane, then select **Add Parameter** from the context menu.

   The Add Parameter dialog box appears.
3. Select or change the options according to the definitions specified in [Simple SQL Output Parameterization](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/output-parameterization-by-report-designer-cp/simple-sql-output-parameterization).
4. Edit your query and add the columns you want to parameterize to the **Conditions** field.
5. Create a parameter token in the **Value** field of each row in the **Conditions** area, and a valid default value in the **Default** field.

   Parameter tokens are in braces {} and do not contain spaces.
6. Click **OK** to save the query.
7. Include the parameterized fields in your report by moving them onto the canvas.
8. Publish or preview the report.

When you run this report, you are presented with an interactive field that specifies an adjustable constraint for the column or columns you specified.
