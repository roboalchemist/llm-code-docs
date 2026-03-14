# Source: https://docs.pinot.apache.org/release-0.10.0/basics/components/deep-store.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/components/deep-store.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/components/deep-store.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/components/deep-store.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/components/table/segment/deep-store.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/components/table/segment/deep-store.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/concepts/components/table/segment/deep-store.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/concepts/components/table/segment/deep-store.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/concepts/components/table/segment/deep-store.md

# Source: https://docs.pinot.apache.org/basics/concepts/components/table/segment/deep-store.md

# Deep Store

The deep store (or deep storage) is the permanent store for [segment](https://docs.pinot.apache.org/basics/concepts/components/table/segment) files.

It is used for backup and restore operations. New [server](https://docs.pinot.apache.org/basics/concepts/components/cluster/server) nodes in a cluster will pull down a copy of segment files from the deep store. If the local segment files on a server gets damaged in some way (or accidentally deleted), a new copy will be pulled down from the deep store on server restart.

The deep store stores a compressed version of the segment files and it typically won't include any indexes. These compressed files can be stored on a local file system or on a variety of other file systems. For more details on supported file systems, see [File Systems](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system).

<mark style="color:red;">Note:</mark> Deep store by itself is not sufficient for restore operations. Pinot stores metadata such as table config, schema, segment metadata in Zookeeper. For restore operations, both Deep Store as well as Zookeeper metadata are required.

## How do segments get into the deep store?

There are several different ways that segments are persisted in the deep store.

For offline tables, the batch ingestion job writes the segment directly into the deep store, as shown in the diagram below:

![Batch job writing a segment into the deep store](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FjlfIv84ZPFG8Co9W562y%2Fbatch-deep-store.png?alt=media\&token=d733fd05-e795-4bbf-870b-8979cadbe391)

The ingestion job then sends a notification about the new segment to the controller, which in turn notifies the appropriate server to pull down that segment.

For real-time tables, by default, a segment is first built-in memory by the server. It is then uploaded to the lead controller (as part of the Segment Completion Protocol sequence), which writes the segment into the deep store, as shown in the diagram below:

![Server sends segment to Controller, which writes segments into the deep store](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2F6hIS4scf3lDNIwekZ0TA%2Fserver-controller-deep-store.png?alt=media\&token=eca72874-dd8b-4af6-be18-4cffa678ddf5)

Having all segments go through the controller can become a system bottleneck under heavy load, in which case you can use the peer download policy, as described in [Decoupling Controller from the Data Path](https://docs.pinot.apache.org/operators/operating-pinot/decoupling-controller-from-the-data-path).

When using this configuration, the server will directly write a completed segment to the deep store, as shown in the diagram below:

![Server writing a segment into the deep store](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FEFtKE7J6oBPxXGWuFny1%2Fserver-deep-store.png?alt=media\&token=2152c984-d0f4-429b-81f0-68a7b1a009a5)

## Configuring the deep store

For hands-on examples of how to configure the deep store, see the following tutorials:

* [Use OSS as Deep Storage for Pinot](https://docs.pinot.apache.org/users/tutorials/use-oss-as-deep-storage-for-pinot)
* [Use S3 as Deep Storage for Pinot](https://docs.pinot.apache.org/users/tutorials/use-s3-as-deep-store-for-pinot)
