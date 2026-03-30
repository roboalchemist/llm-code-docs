# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started/partitioning-data-over-tables.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started/partitioning-data-over-tables.md

# Partitioning data over tables

The Table output step (double-click the step to open it) supports partitioning rows of data to different tables. When configured to accept the table name from a **Partitioning field**, the PDI client will output the rows to the appropriate table. You can also **Partition data per month** or **Partition data per day**. To ensure that all the necessary tables exist, we recommend creating them in a separate transformation.

![Table output step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-576c5ecbe85ffb29bca02ce3ac735ae7da4f791c%2FPDI_TableOutput_dialog.png?alt=media)
