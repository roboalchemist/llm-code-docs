# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-database-explorer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/use-the-database-explorer.md

# Use the Database Explorer

The Database Explorer allows you to explore configured database connections. The Database Explorer also supports tables, views, and synonyms along with the catalog, schema, or both to which the table belongs.

A right-click on the selected table provides quick access to the following features:

| Feature               | Description                                                                                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Preview first 100** | Returns the first 100 rows from the selected table.                                                                                                                                                  |
| **Preview x Rows**    | Prompts you for the number of rows to return from the selected table.                                                                                                                                |
| **Row Count**         | Specifies the total number of rows in the selected table.                                                                                                                                            |
| **Show Layout**       | Displays a list of column names, data types, and so on from the selected table.                                                                                                                      |
| **DDL**               | Generates the DDL to create the selected table based on the current connection type, the drop-down.                                                                                                  |
| **View SQL**          | Launches the Simple SQL Editor for the selected table.                                                                                                                                               |
| **Truncate Table**    | <p>Generates a TRUNCATE table statement for the current table.</p><p><strong>Note:</strong> The statement is commented out by default to prevent users from accidentally deleting the table data</p> |
| **Data Profile**      | Provides basic information about the data.                                                                                                                                                           |

You can open the Database Explorer in the Database Connections dialog box. In the PDI client, navigate to the \*\*View\*\* tab in the \*\*Explorer\*\* pane, and then double-click on the \`Database connections\` folder.
