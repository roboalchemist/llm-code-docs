# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/inspect-your-data/get-started.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started.md

# Get started

By default, each step in a transformation is executed in parallel in a single separate thread. Consider, for example, the transformation below. With a single copy of each step, the data is read from the CSV file input step and then aggregated in the `count by state` step. The results of which can be verified by examining the preview data.

![Partitioning use case example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d77b55150cb5f17e2ca2ed94dd904a7ccaa58db5%2Fpartitioning-usercase-simple.png?alt=media)
