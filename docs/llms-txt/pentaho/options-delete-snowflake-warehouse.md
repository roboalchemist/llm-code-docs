# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/delete-snowflake-warehouse/options-delete-snowflake-warehouse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/delete-snowflake-warehouse/options-delete-snowflake-warehouse.md

# Options

![Delete Snowflake warehouse dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d90dc0d228b5aced3876ff6927111b161cdddda2%2FPDI_DeleteSnowflakeWarehouse_Job.png?alt=media)

The following options are available for this entry:

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Database connection** | <p>Use the list to select the name of an existing Snowflake database connection.If you do not have an existing connection, click <strong>New</strong>. If you need to modify an existing connection, click <strong>Edit</strong>.</p><p><strong>Note</strong>: If timeout errors occur, see <a href="../../data-integration-issues/snowflake-timeout-errors-general-issues-in-troubleshooting">Snowflake timeout errors</a> to troubleshoot.</p> |
| **Warehouse**           | Use the list to select the name of the virtual warehouse to be deleted.                                                                                                                                                                                                                                                                                                                                                                          |
| **Activity settings**   | <p>Select the <strong>Fail if warehouse doesn’t exist</strong> check box if you want the PDI job to fail if the virtual warehouse does not exist (default).</p><p>Clear the <strong>Fail if warehouse doesn’t exist</strong> check box if you want the PDI job to continue and move to the next entry.</p>                                                                                                                                       |
