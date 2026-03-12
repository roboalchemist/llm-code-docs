# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-azure-sql-db/options-azure-sql-db-bulk/output-tab-azure-sql-db-bulk.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-azure-sql-db/options-azure-sql-db-bulk/output-tab-azure-sql-db-bulk.md

# Output tab

![Bulk load into Azure SQL DB Output tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b22d45f46081074fee421492e1fc7077a1b49e1b%2FBulk%20load%20into%20Azure%20SQL%20DB%20Output%20tab.png?alt=media)

Enter the following information on the **Output** tab to specify the output destination of the source data:

| Option                  | Description                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Database connection** | <p>Select your database connection from a list of existing Azure SQL DB connections.</p><p>If you do not have an existing connection, click <strong>New</strong>. If you need to modify an existing connection, click <strong>Edit.</strong></p><p>See the <strong>Install Pentaho Data Integration and Analytics</strong> document.</p> |
| **Schema**              | Select the schema to use for the bulk load. The **Bulk load into Azure SQL DB** entry reads the schemas that exist in the database to populate this list.                                                                                                                                                                                |
| **Table name**          | Select the name of the table to bulk load. The **Bulk load into Azure SQL DB** entry reads the table names from your selected schema to populate this list.                                                                                                                                                                              |
| **Columns**             | Preview of the column names and associated data types within your selected table.                                                                                                                                                                                                                                                        |

\*\*Note:\*\* You can use variables in the schema and table name fields.
