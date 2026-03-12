# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs/explore-configure-database-connections.md

# Explore configure database connections

The Database Explorer allows you to explore configured database connections. The Database Explorer also supports tables, views, and synonyms along with the catalog, schema, or both to which the table belongs.

1. With a transformation or job open, on the left side of the Pipeline Designer interface, click the **View** icon. The **View** pane opens with the Transformations folder expanded, containing the **Database Connections** list.
2. Expand **Database Connections**, find the database connection you want to explore, and click the **More Actions** icon.&#x20;
3. Select **Explore**. The Database Explorer window opens.&#x20;
4. (Optional) Click the refresh icon to refresh the list.
5. Expand the folders and find the item you want to review.
6. Click **Actions**, and then select one of the following features:&#x20;

   <table><thead><tr><th width="162">Feature</th><th>Description</th></tr></thead><tbody><tr><td><strong>Preview first 100</strong></td><td>Returns the first 100 rows from the selected table.</td></tr><tr><td><strong>Preview x Rows</strong></td><td>Prompts you for the number of rows to return from the selected table.</td></tr><tr><td><strong>Row Count</strong></td><td>Specifies the total number of rows in the selected table.</td></tr><tr><td><strong>Show Layout</strong></td><td>Displays a list of column names, data types, and so on from the selected table.</td></tr><tr><td><strong>DDL</strong></td><td>Generates the DDL to create the selected table based on the current connection type, the drop-down.</td></tr><tr><td><strong>View SQL</strong></td><td>Launches the Simple SQL Editor for the selected table.</td></tr><tr><td><strong>Truncate Table</strong></td><td>Generates a TRUNCATE table statement for the current table.<strong>Note:</strong> The statement is commented out by default to prevent users from accidentally deleting the table data</td></tr><tr><td><strong>Data Profile</strong></td><td>Provides basic information about the data.</td></tr></tbody></table>
7. When you finish exploring the database connection, click **Ok**. The Database Explorer window closes.
