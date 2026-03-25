# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning/use-data-swimlanes.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning/use-data-swimlanes.md

# Use data swimlanes

When a partitioned step passes data to another partitioned step with the same partition schema, the data is kept in swimlanes because no repartitioning needs to be done. As illustrated below, no extra buffers (row sets) are allocated between the copies of steps `count by state` and `Replace in string`.

![Data swimlanes](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-30238d126d12f017bda9d660db9279bc0ca20254%2Fpartitioning-swim-lanes.png?alt=media)

The step copies remain isolated from one another and the rows of data travel in swimlanes. No extra work needs to be done to keep the data partitioned, so you can chain as many partitioned steps as needed. This will internally be executed as shown in the following illustration.

![Internal execution of partitioned steps](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d6bbbdc33b7a86853597a3f5875fa0014ba43c59%2Fpartitioning-swimlanes-explained.png?alt=media)
