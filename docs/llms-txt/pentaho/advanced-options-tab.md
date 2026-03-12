# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake/options-snowflake-bulk-loader/advanced-options-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/bulk-load-into-snowflake/options-snowflake-bulk-loader/advanced-options-tab.md

# Advanced options tab

![Advanced Options tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2f46e247ac62666e0413d13a9fae3ac8ae1306f0%2FPDI_JobEntry_Snowflake_BulkLoader_Advanced_Options_tab.png?alt=media)

Use this tab to configure parameters for the Snowflake COPY INTO command. Any **Name/Value** pair added as a parameter is passed to Snowflake as a parameter, but the validation of the parameter is the user’s responsibility. See [Snowflake’s documentation](https://docs.snowflake.net/manuals/index.html) for further details on these parameters. The `Force` parameter here is provided as an example.

| Parameter | Description                                                                                                                                                                                                                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Force** | <p>Specify to force loading of files into a database:- <strong>True</strong>: Loads data to the table even if the data has already been loaded from that file before. This option can potentially duplicate data in a table.</p><ul><li><strong>False</strong>: Ignores staged data files already loaded into the table (default).</li></ul> |
