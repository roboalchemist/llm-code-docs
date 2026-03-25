# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/metadata-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/metadata-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/metadata-connecting-to-a-data-source-in-prd.md

# Metadata

Follow this procedure to add a Pentaho Metadata XMI file as a data source in Report Designer:

1. Select the **Data** tab in the upper right pane.

   By default, Report Designer starts in the **Structure** tab, which shares a pane with **Data**.
2. Click the yellow cylinder icon in the upper left part of the **Data** pane, or right-click **Data Sets**.

   A drop-down menu with a list of supported data source types will appear.
3. Select **Metadata** from the drop-down menu.

   The Metadata Data Source Editor window will appear.
4. Click **Browse**, navigate to your XMI metadata definition file, then click **Open**.
5. Click the round green **+** icon to add a query, then type in a name for the new query in the **Query Name** field.
6. Type in the name of the solution directory this metadata file pertains to into the **Domain Id** field.
   * If this XMI file was created with Pentaho Metadata Editor, then the domain ID must be the root directory for this solution -- the directory one level above `pentaho-solutions`, typically.
   * If you created this XMI with Pentaho Data Integration, then the domain ID must be set to the full solution path to the XMI, which would be something like this: `example-solution/resources/metadata/mymeta.xmi`.
   * If the domain ID is not properly defined, you will be able to preview the report, but you will not be able to publish it to the Pentaho Server.
7. Click the pencil icon on the right above the **Query** field to start Metadata Query Editor, or type in your query directly into the **Query** field.

   See [Create queries with Metadata Query Editor](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PRD/Create%20queries/Create%20queries%20\(Report%20Designer%20cp\)/Create%20queries%20with%20Metadata%20Query%20Editor%20\(Create%20queries%20in%20PRD\)=GUID-64947C4F-6535-4495-B71E-7D9AD18E74F9=3=en=.md) for more details on Metadata Query Editor. You can also design a dynamic query via a script; see [Dynamic query scripting](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/dynamic-query-scripting).
8. Click **OK** when your query is complete.
