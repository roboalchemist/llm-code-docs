# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-database-connections/pdi-does-not-recognize-changes-made-to-a-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/troubleshooting-database-connections/pdi-does-not-recognize-changes-made-to-a-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/troubleshooting-database-connections/pdi-does-not-recognize-changes-made-to-a-table.md

# PDI does not recognize changes made to a table

If you edit the table layout outside of the PDI client, PDI is not aware of any field changes, deletions, or additions.

Clearing the cache addresses this issue. The cache needs to be cleared of database-related meta information (field names and their types in each used database table). PDI has this cache to increase processing speed. Perform the following steps to clear this information in the cache from within the PDI client:

1. Select the connection.
2. Use either of these methods to clear the cache:
   * **Tools** > **Database** > **Clear Cache**
   * **Database connections** > **Clear complete DB cache**
