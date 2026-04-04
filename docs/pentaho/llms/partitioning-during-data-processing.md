# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started/partitioning-during-data-processing.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started/partitioning-during-data-processing.md

# Partitioning during data processing

To take advantage of the processing resources in your server, you can scale up the transformation using the multi-threading option **Change Number of Copies to Start** to produce copies of the steps (right-click the step to access the menu). As shown below, the **x2** notation indicates that two copies will be started at runtime. By default, this data movement from the CSV file input step into the `count by state` step will be performed in round-robin order. This means that if there are 'N' copies, the first copy gets the first row, the second copy gets the second row, and the Nth copy receives the Nth row. Row N+1 goes to the first copy again, and so on until there are no more rows to distribute. Reading the data from the CSV file is done in parallel. Attempting to aggregate in parallel, however, produces incorrect results because the rows are split arbitrarily (without a specific rule) over the two copies of the `count by state` aggregation step, as shown in the preview data.

![Aggregate in parallel, data error example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-aadfde46ca6cf0b0f13d890a02538aef106f05bb%2Fpartitioning-usercase-parallel-error.png?alt=media)
