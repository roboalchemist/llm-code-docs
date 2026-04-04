# Source: https://docs.pentaho.com/pba-report-designer/create-queries-report-designer-cp/create-mdx-queries-create-report-designer-queries.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-queries-report-designer-cp/create-mdx-queries-create-report-designer-queries.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/create-mdx-queries-create-report-designer-queries.md

# Create MDX queries

For Pentaho Analyzer data sets, such as OLAP and OLAP (advanced), you can create MDX queries by specifying a Mondrian cube definition schema file.

You must be in the Data Source Configuration window to follow this process. You should also have configured a JNDI data source connection.

Perform the following steps to add a MDX query:

1. In the **Data** tab, right-click on **Data Sets** and select one of the following options to access the Pentaho Analyzer Data Source Editor window:
   * **OLAP** > **Pentaho Analysis**
   * **OLAP** > **Pentaho Analysis (Denormalized)**
2. Specify a Mondrian cube definition schema file for Pentaho Analysis Schema File.

   You can use the Pentaho Schema Workbench to create this file.
3. Select your data source in the **Connections** pane on the left, then click the round green **+** icon above the **Available Queries** pane on the right.
4. Type a concise yet sufficiently descriptive name for your query in the **Query Name** field.
5. Type an MDX query into the **Query** pane on the right.
6. Click **Preview** to view the unformatted query results.
7. Click **OK** to finish working on the query.
