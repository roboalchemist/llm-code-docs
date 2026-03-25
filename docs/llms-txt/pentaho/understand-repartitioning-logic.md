# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started/understand-repartitioning-logic.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/get-started/understand-repartitioning-logic.md

# Understand repartitioning logic

Data distribution in the steps is shown in the following table.

![Data distributions by steps](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-950f60c4d33d218cfef224f039286d63094af107%2Fpartitioning-usrecase-distribution.png?alt=media)

As you can see, the CSV file input step divides the work between two step copies and each copy reads 50 rows of data. However, these 2 step copies also need to make sure that the rows end up on the correct `count by state`step copy where they arrive in a 43/57 split. Because of that, it is a general rule that the step performing the repartitioning (row redistribution) of the data (a non-partitioned step before a partitioned one) has internal buffers from every source step copy to every target step copy, as shown below.

![Work division between step copies with partitioning](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-d7148dc8199eb2be684b4e566ce6f28da4c02c15%2Fpartitioning-distribution-2.png?alt=media)

This is where partitioning data becomes a useful concept, as it applies specific rule-based direction for aggregation, directing rows from the same state to the same step copy, so that the rows are not split arbitrarily. In the example below, a partition schema called `State` was applied to the `count by state` step and the Remainder of division partitioning rule was applied to the `State` field. Now, the `count by state` aggregation step produces consistent correct results because the rows were split up according to the partition schema and rule, as shown in the preview data.

![Partitioning data using rule-based aggregation](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b9d1acbe9f55e87e01984a372871ebac748b01f9%2Fpartitioning-usercase-partitioned.png?alt=media)

**Note:** To view this transformation in the PDI client, open the `Pentaho/…/design-tools/data-integration/samples/transformations/General - parallel reading and aggregation.ktr` sample file.
