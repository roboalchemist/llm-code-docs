# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse/options-stop-snowflake-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/stop-snowflake-warehouse/options-stop-snowflake-warehouse.md

# Options

![Stop Snowflake warehouse dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-50dc7362271d691b9b12da65f5d4dd344557ac6a%2FPDI_StopSnowflakeWarehouse_Job.png?alt=media)

The following options are available for this entry:

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Database connection** | <p>Use the list to select the name of an existing Snowflake database connection.If you do not have an existing connection, click <strong>New</strong>. If you need to modify an existing connection, click <strong>Edit</strong>.</p><p><strong>Note</strong>: If timeout errors occur, see <a href="../../data-integration-issues/snowflake-timeout-errors-general-issues-in-troubleshooting">Snowflake timeout errors</a> to troubleshoot.</p> |
| **Warehouse**           | <p>Specify the Snowflake virtual warehouse that you want to stop by selecting one of the following methods:</p><ul><li><strong>Use default warehouse (defined in the database connection)</strong>: Suspend the warehouse defined by your database connection.</li><li><strong>Use an existing warehouse</strong>: Suspend an existing warehouse. Use the list to select the name of the existing warehouse.</li></ul>                           |
| **Activity settings**   | <p>Select the <strong>Fail if warehouse doesn’t exist</strong> check box if you want the PDI job to fail if the virtual warehouse does not exist (default).</p><p>Clear the <strong>Fail if warehouse doesn’t exist</strong> check box if you want the PDI job to continue and move to the next entry.</p>                                                                                                                                       |
