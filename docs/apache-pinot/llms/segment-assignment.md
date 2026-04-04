# Source: https://docs.pinot.apache.org/release-0.9.0/operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/operating-pinot/segment-assignment.md

# Source: https://docs.pinot.apache.org/operators/operating-pinot/segment-assignment.md

# Segment Assignment

Segment assignment refers to the strategy of assigning each segment from a table to the servers hosting the table. Picking the best segment assignment strategy can help reduce the overhead of the query routing, thus providing better performance.

## Balanced Segment Assignment

Balanced Segment Assignment is the default assignment strategy, where each segment is assigned to the server with the least segments already assigned. With this strategy, each server will have balanced query load, and each query will be routed to all the servers. It requires minimum configuration, and works well for small use cases.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MJZnXu9U-el7FnXDTy4%2F-MJZrK5swEqt0b8wTFAu%2FBalanced.png?alt=media\&token=1fe62795-80d4-4326-a4f7-97cc7871a019)

## Replica-Group Segment Assignment

Balanced Segment Assignment is ideal for small use cases with a small number of servers, but as the number of servers increases, routing each query to all the servers could harm the query performance due to the overhead of the increased fanout.

Replica-Group Segment Assignment is introduced to solve the horizontal scalability problem of the large use cases, which makes Pinot linearly scalable. This strategy breaks the servers into multiple replica-groups, where each replica-group contains a full copy of all the segments.

When executing queries, each query will only be routed to the servers within the same replica-group. In order to scale up the cluster, more replica-groups can be added without affecting the fanout of the query, thus not impacting the query performance but increasing the overall throughput linearly.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MEhNqPntb48j8ly2mg8%2F-MEhOFwwkdxK7zYZzlX2%2Freplica-group.png?alt=media\&token=51eeb8f7-8529-483a-9870-3c22d11efe5d)

## Partitioned Replica-Group Segment Assignment

In order to further increase the query performance, we can reduce the number of segments processed for each query by partitioning the data and use the Partitioned Replica-Group Segment Assignment.

Partitioned Replica-Group Segment Assignment extends the Replica-Group Segment Assignment by assigning the segments from the same partition to the same set of servers. To solve a query which hits only one partition (e.g. `SELECT * FROM myTable WHERE memberId = 123` where `myTable` is partitioned with `memberId` column), the query only needs to be routed to the servers for the targeting partition, which can significantly reduce the number of segments to be processed. This strategy is especially useful to achieve high throughput and low latency for use cases that filter on an id field.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MJZnXu9U-el7FnXDTy4%2F-MJZxyRBwDPmxPSV2TyR%2FPartitioned.png?alt=media\&token=29228847-a79d-4143-91f3-3bc2b4faaf73)

## Configure Segment Assignment

Segment assignment is configured along with the instance assignment, check [Instance Assignment](https://docs.pinot.apache.org/operators/operating-pinot/instance-assignment) for details.
