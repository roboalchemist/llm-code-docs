# Source: https://docs.startree.ai/corecapabilities/manage-data/set-up-tiered-storage/architecture.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tiered storage for Apache Pinot in StarTree Cloud

> Learn how tiered storage is built for Apache Pinot, effectively decoupling the storage from the compute in your Pinot cluster.

With Tiered storage, your Pinot cluster is now, **not limited to use just the disk/SSD storage**. We are no longer strictly tightly coupled. You can have multiple tiers of storage, with **support for using a cloud object storage like S3 as a storage tier**. You can **configure exactly which portion of your data you want to keep locally, and which is offloaded to the cloud tier storage**.

<p>
  <img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/manage-data/images/introducing-tiered-storage.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=4e7c73d340a25735234f786d2f9ab5b5" width="800px" alt="Introducing Tiered Storage for Apache Pinot in StarTree Cloud" title={true} data-path="corecapabilities/manage-data/images/introducing-tiered-storage.png" />
</p>

One popular way to split data across local vs cloud is by **data age**, so you could configure in your table config, that you want **data less than 30 days old to be on disk, rest to be on S3**.

Users can then **query the entire table, across local and remote data**, like any other Pinot dataset.

With this decoupling, you can now store as much data as you want in Pinot, without worrying about the cost. And this is super flexible and configurable: This threshold is dynamic and can be changed at any point in time and Pinot will automatically reflect the changes.

You can still operate Pinot in fully -tightly coupled mode if you want, or completely in decoupled mode, or a hybrid approach (like in the picture above), where some nodes are dedicated for local data, and some for remote data.

Here's a blog post which goes in more details about the motivation, and some initial benchmarks: [Speed of Apache Pinot at the cost of Cloud Object Storage](https://www.startree.ai/blog/introducing-tiered-storage)

## Frequently asked questions

Questions and clarifications about this feature:

### What is different between this and the Tiered Storage in open-source Apache Pinot?

In Apache Pinot open-source, we have limited support for tiered storage (read more in the doc: [Moving data from one tenant to another based on segment age](https://docs.pinot.apache.org/operators/operating-pinot/moving-segments-across-tenants)). It simply lets you use multiple tenants for the same table, where each tenant can be configured to have servers of different specs (e.g. use SSD nodes for tenant 1 and lower performant cheaper HDDs as tenant 2). But the tiering stops there. We can separate the compute nodes using tenants, but are still using local storage, making us tightly coupled in terms of storage and compute.

<p>
  <img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/manage-data/images/oss-vs-startree.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=7faea9ebbacf7e7eeec508d45256c85c" width="1100px" alt="Tiered storage in oss vs in StarTree Cloud" title={true} data-path="corecapabilities/manage-data/images/oss-vs-startree.png" />
</p>

### Doesn't Pinot already have deep store? I have set up Pinot with S3/GCS as my segment store, isn't that the same?

Many of you might be familiar with the architecture of Pinot or similar systems, and might know that these systems, along with their tightly coupled storage component, additionally also have a cloud object store like S3, GCS, ABS in their architecture. However, this segment store or deep store, **is only used for permanent backups, disaster recovery, and it is not involved in the query path**. With the tiered storage feature, for Apache Pinot we are now able to **use the cheap cloud storage directly in the query, and replace the disk/SSDs**.

<p>
  <img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/manage-data/images/not-deep-store.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=60e6bbfdf4bed58a9a8e9b5a97cd564e" width="700px" alt="Not to be confused with deep-store" title={true} data-path="corecapabilities/manage-data/images/not-deep-store.png" />
</p>

### Why can't we use the copy already in deep-store?

The segment in deep store is compressed, and typically will not have all indexes, especially if you've added indexes or derived columns to the segment later on. We use a separate location and copy for the tiered storage query execution, so we can keep it uncompressed and exactly in sync with what would have been on the server. Think of this S3 bucket as an exact replacement for the storage that would've been on the servers locally, with one major difference that we'll keep only 1 copy in S3 vs replication number of copies locally.

### Is this implemented like lazy loading?

One common way that other systems in data infra solve tiering, is by using lazy loading. In lazy loading, think of your shards/segments being stored in S3, and when your query needs a segment which is on S3, it will be downloaded entirely. This means that the first access will be very slow, and your second access would find the segment locally. However, in typical OLAP workloads,

1. more often than not, your next query will need completely different set of segments (think arbitrary slide n dice, point lookups on various dimensions)
2. or you will need more data for a single query than your local storage can keep
3. Predictable p99 query latency is crucial

So in an OLAP system with lazy loading, you'll end up with continuous churn and continuous segment downloads.
StarTree's approach is different, and strictly stays away from lazy loading. And while caches can be enabled as optimizations, the implementation doesn't rely on a cache or local storage to function.

### Are all indexes supported in Tiered Storage?

Yes, all indexes are supported. Text index support is very new (Beta) added in the StarTree 0.11.1 release.

## Architecture

### Lightboard session

<iframe width="560" height="315" src="https://www.youtube.com/embed/YUJXwzN2dok" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### Tech talk

<iframe width="560" height="315" src="https://www.youtube.com/embed/nEAvHAvh0tY" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Built with [Mintlify](https://mintlify.com).
