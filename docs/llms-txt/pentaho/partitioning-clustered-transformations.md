# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/partitioning-clustered-transformations.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/partitioning-clustered-transformations.md

# Partitioning clustered transformations

Partitioning data allows your transformations to scale out on a cluster of slave servers to maximize the resources of machines operating in parallel. When a step is assigned to run on a Carte master node (that is, non-clustered in a clustered transformation), the same rules apply as described in [Rules for partitioning](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning/rules-for-partitioning).

In case a clustered step is partitioned, the partitions are distributed over the number of slave servers. As a result, the number of partitions needs to be equal to or higher than the number of slave servers in the cluster schema. It is, therefore, recommended to allow the PDI client to create the partition schema dynamically in a clustered environment.

You should always limit repartitioning on a cluster to a minimum, as high amounts of networking and CPU overhead can be incurred, which is caused by the massive amounts of data passing from one server to another over TCP/IP sockets. Also, to get optimal performance on a cluster, try to keep the data in swimlanes, described in [Use data swimlanes](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/partitioning-data/use-partitioning/use-data-swimlanes), for as long as possible.

![Partitioning schema dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b99a2dc8c750a5a854a679eae1d9d370b503ce93%2Fpartitioning-clustered-dynamic.png?alt=media)
