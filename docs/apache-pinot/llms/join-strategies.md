# Source: https://docs.pinot.apache.org/release-1.3.0/for-users/user-guide-query/multi-stage-query/join-strategies.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-users/user-guide-query/multi-stage-query/join-strategies.md

# Source: https://docs.pinot.apache.org/users/user-guide-query/multi-stage-query/join-strategies.md

# Join strategies

In order to execute a join, all the rows of the tables to be joined need to be in the same place. In classical databases like Postgres this is not a problem, as there is usually a single server (or all servers have all the data). But in distributed databases like Pinot, where rows of the tables are distributed across servers, data needs to be shuffled between servers (at least in the general case). This data shuffle is expensive and can be a bottleneck for the query performance.

The most simple way to execute the join would be to move all data into a single server, as shown in the diagram below.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FYeB90rDo8FDxJvKnwZoH%2Fimage.png?alt=media&#x26;token=aecb7443-ff75-42a0-998c-0b898f4c6e87" alt="" width="563"><figcaption><p>Dotted arrows mean shuffle while solid arrows mean in-server transfer</p></figcaption></figure>

This approach may work for small tables, but it would not scale for large tables that do not fit into a single server. Pinot assumes this is going to be the common case, so it never uses this technique. It is shown here only to help understand the shuffling problem.

What Pinot does is to create *virtual partitions* at query time. These virtual partitions are created in such a way that Pinot can guarantee that rows that need to be joined are sent to the same server but at the same time it tries to minimize the amount of data that needs to be shuffled between servers.

There are several strategies Pinot can use to reduce data shuffle. Some of them are so effective that they can be used to execute the join without any data shuffle at all, but they are only applicable in some cases.

The strategies, in order of effectiveness, are:

1. [Lookup joins](https://docs.pinot.apache.org/users/user-guide-query/multi-stage-query/join-strategies/lookup-join-strategy)
2. [Colocated joins](https://docs.pinot.apache.org/users/user-guide-query/multi-stage-query/join-strategies/colocated-join-strategy)
3. [Query time partition join](https://docs.pinot.apache.org/users/user-guide-query/multi-stage-query/join-strategies/query-time-partition-join-strategy)
4. [Random + broadcast join](https://docs.pinot.apache.org/users/user-guide-query/multi-stage-query/join-strategies/random-+-broadcast-join-strategy)

These techniques are explained in more detail in the their own pages. More join strategies will be added in the future. They are listed in the GitHub issue [#14518](https://github.com/apache/pinot/issues/14518).
