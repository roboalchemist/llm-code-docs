# Source: https://docs.pentaho.com/pba-report-designer/create-queries-report-designer-cp/create-queries-with-sql-query-designer-create-queries-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-queries-report-designer-cp/create-queries-with-sql-query-designer-create-queries-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/create-queries-with-sql-query-designer-create-queries-in-prd.md

# Create queries with SQL Query Designer

You can use the SQL Query Designer interface to create a SQL query to get data. The SQL Query Designer is only available through the JDBC Data Source window. You must already have a JDBC data source configured and tested before using the SQL Query Designer. See [Connect to a Data Source](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp) for more information on connecting to a JDBC data source.

**Note:** SQL Query Designer does not work with Hadoop Hive data sources.

For instructions on creating queries with SQL Query Designer, see the following sections:

* [Access the SQL Query Designer](#access-the-sql-query-designer)
* [Apply query filters](#apply-query-filters)
* [Refine the query](#refine-the-query)
* [Analyze results](#analyze-results)
* [Create sub-queries with SQL Query Designer](#create-sub-queries-with-sql-query-designer)

## Access the SQL Query Designer

Perform the following steps to access the SQL Query Designer:

1. In the **Data** tab, right-click on **Data Sets** and select JDBC.

   The JDBC Data Source window appears.
2. Select your data source in the **Connections** pane on the left, then click the round green **+** icon above the **Available Queries** pane on the right.
3. Type a concise yet sufficiently descriptive name for your query in the **Query Name** field.
4. Click the pencil icon above the upper right corner of the **Query** field.

   The SQL Query Designer tool appears, as shown in the following example:

   ![SQL Query Designer](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-adc70146d07f6f836c3f6b38ae3063b0ae5ad3fb%2FReportDesigner_Queries_SQLQueryDesigner.png?alt=media)

## Apply query filters

Perform the following steps to apply filters to your query:

1. Select a schema filter in the menu above the lower left pane and ensure the type filter is set to **Tables**.
2. In the lower left pane, click to select the first table from which you want to refine data, then double-click it to move it to the query workspace.

   As shown in the following example, the table you selected appears in the workspace as a sub-window containing all its rows:

   ![Query filters in the SQL Query Designer](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-6b7461aa129c52bba16b21985308c5f1ba95baa8%2FReportDesigner_Queries_SQLQueryDesigner_Table.png?alt=media)
3. Check all the rows you want to include in the query.

   By default, all rows are selected. If you only want to select a few rows (or a single row) in your query, click the table name at the top of the sub-window, then click deselect all in the popup menu, and check only the rows you want to include in your query.
4. Repeat the previous step for other tables you want to include in the SQL query.

## Refine the query

Depending on how you might want to further refine your query, you can perform the following steps to join tables, apply conditions, or group and order rows:

1. To create an SQL `JOIN` between tables, select a reference key in one table, then drag it to the appropriate row in another table.

   To modify the `JOIN`, right-click its red square, then click **edit** in the popup menu.
2. To add a condition or expression, right-click a row in the query workspace, and select the appropriate action from the menu.
3. To order or group by a specific row, drag a statement from the `SELECT` category in the upper left pane and drop it into the **GROUP BY** or **ORDER BY** category.

## Analyze results

Perform the following steps to analyze the resulting query:

1. To edit the SQL syntax directly, click the syntax tab in the bottom left corner of the SQL Query Designer window.
2. Click **Preview** to view the unformatted query results.
3. Click **OK** to finish working on the query.

You now have a data source and at least one query that will return a data set that you can use for reporting.

## Create sub-queries with SQL Query Designer

You can also design an SQL sub-query for your data source with SQL Query Designer by performing the following steps:

1. Right-click on the query and select **add where condition** or **add having condition**.

   The condition.edit window appears.
2. Click on the arrow next to the working query so that the whole path is expanded. Type in the condition and click **OK**.
3. Click **Preview** to ensure the query is working. Click **OK** to exit the condition.edit window.
4. Drag the queries you have created into the workspace, in the **Details** row. Preview the report to ensure that everything is working as expected.

You now have an SQL sub-query that returns a data set that you can use for reporting.
