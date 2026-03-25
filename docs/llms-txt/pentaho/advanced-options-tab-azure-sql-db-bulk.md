# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-azure-sql-db/options-azure-sql-db-bulk/advanced-options-tab-azure-sql-db-bulk.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-azure-sql-db/options-azure-sql-db-bulk/advanced-options-tab-azure-sql-db-bulk.md

# Advanced options tab

![Bulk load into Azure SQL DB Advanced options tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7104d7f835d7eb302825417a40f0b292774b6a32%2FBulk%20load%20into%20Azure%20SQL%20DB%20Advanced%20options%20tab.png?alt=media)

Use this tab to configure parameters for the Bulk load into Azure SQL DB. Any **Name/Value** pair added as a parameter is passed to the Azure SQL database as a parameter, but the validation of the parameter is the user’s responsibility. See the [Azure SQL documentation](https://docs.microsoft.com/en-us/azure/azure-sql/) for further details on these parameters. The `Force` parameter here is provided as an example.

| Option    | Description                                                                                                                                                                                                                                                                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Force** | <p>Specify whether to force loading of files into a database:</p><ul><li><strong>True</strong></li></ul><p>Loads data to the table even if the data was already loaded from that file before. This option can potentially duplicate data in a table.</p><ul><li><strong>False</strong></li></ul><p>Ignores staged data files already loaded into the table (default).</p> |
