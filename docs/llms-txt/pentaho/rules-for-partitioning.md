# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning/rules-for-partitioning.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning/rules-for-partitioning.md

# Rules for partitioning

When you use partitioning, the logic used for distribution, repartitioning, and buffer allocations will be dependent upon the following rules:

* A partitioned step causes one step copy to be executed per partition in the partition schema.
* When a step needs to repartition the data, the step creates buffers (row sets) from each source step copy to each target step copy (partition).
* When rows of data pass from a non-partitioned step to a partitioned one, data is repartitioned and extra buffers are allocated.
* When rows of data, partitioned with the same partition schema, pass from a partitioned step to another partitioned step, data is not repartitioned.
* When rows of data, partitioned with a different partition schema, pass from a partitioned step to another partitioned step, data is repartitioned.
