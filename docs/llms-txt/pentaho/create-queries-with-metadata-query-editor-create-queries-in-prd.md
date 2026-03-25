# Source: https://docs.pentaho.com/pba-report-designer/create-queries-report-designer-cp/create-queries-with-metadata-query-editor-create-queries-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-queries-report-designer-cp/create-queries-with-metadata-query-editor-create-queries-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/create-queries-with-metadata-query-editor-create-queries-in-prd.md

# Create queries with Metadata Query Editor

You can create a metadata query to get data using the Metadata Query Editor. The Metadata Query Editor is only available through the Metadata Data Source Editor window. You must already have a metadata data source configured and tested before using the Metadata Query Designer. See [Connect to a Data Source](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp) for more information on connecting to a metadata data source.

Perform the following step to design a metadata query for your data source with the Metadata Query Editor:

1. In the **Data** tab, right-click on **Data Sets** and select **Metadata**.

   The Metadata Data Source Editor window appears.
2. Specify your XMI file and solution name, then click the round green **+** icon above the **Available Queries** pane on the right.
3. Type a concise yet sufficiently descriptive name for your query in the **Query Name** field.
4. With all your metadata data source options properly typed in, click the pencil icon above the upper right corner of the **Query** field.

   The Query Editor window appears, as shown in the following example:

   ![Query Editor](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-c34dd621309aee4037089694b37173a51fd9db42%2FReportDesigner_Queries_MetadataQueryDesigner.png?alt=media)

   **Note:** If the pencil icon is greyed out, then your data source is misconfigured.
5. Select a data set from the **Business Models** menu.

   The list of available tables and columns will update appropriately.
6. Double-click a table to display its columns, click on a column that you want to select, then click the arrow next to the **Selected Columns** box.

   You can select multiple columns by holding down the Ctrl key while clicking on the columns.

   **Note:** To define a parameter, specify the parameter's name by using curly brackets, `{Parameter Name}` for example. The parameter name must reference the parameter you created in your report. The **Default** value column is used to preview data in the Metadata Data Source Editor, only. To specify, multiple values for a parameter use a "`|`" (pipe) between your values as shown in the following example:

   ![](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-61f8631b418cce22d2e18359b90f242fa31c3a0e%2FReportDesigner_Queries_MetadataQueryDesigner_Conditions.png?alt=media)
7. Repeat this process to create conditions for the additional columns by moving a column over to the **Conditions** box.

   Condition values must be in double quotes (") to be validated in the Query Editor.
8. Move the column by which you want to order your results into the **Order By** box.
9. Click **OK** to finalize the query.

   Your new query will appear in the **Query** field of the data source configuration window. The **Query** field is editable. If needed, you can modify the query before continuing.
10. Click **OK** to close the Metadata Data Source Editor.

You now have a data source and at least one query that will return a data set that you can use for reporting.
