# Source: https://docs.lancedb.com/lance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lance format

> Open-source lakehouse format for multimodal AI.

[Lance](https://lance.org/) is an open-source lakehouse format, which provides the
foundation for LanceDB's capabilities. Lance combines the performance of Apache Arrow with advanced
features designed specifically for AI workloads.

<Card title="Lance format documentation" icon="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=1c7311e59aacc6a085345618f357d380" href="https://lance.org/quickstart" data-og-width="1820" width="1820" data-og-height="1790" height="1790" data-path="static/assets/logo/lance-logo-gray.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=ed448d64255aa056dc20667ba41b1ae5 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=39a717a458214da2e1b8aceed6105354 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=ae715fa3264b36868def4c0017d7bb64 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=c9c74bcca7784c7fbb57be2012e23701 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=8ada40df0308bbbc934cf36a2894e0cd 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=8611e35177202da4f179550c743d2270 2500w">
  Learn more about the Lance format by reading the docs.
</Card>

## How Lance Enables the Multimodal Lakehouse

Lance is a file format, table format, and catalog spec for multimodal AI, allowing developers to build a
complete open lakehouse on top of object storage to power AI workflows. The format brings
high-performance vector search, full-text search, random access, and feature engineering capabilities
to a single unified system, eliminating the need for multiple specialized databases.

Unlike traditional vector databases that only store embeddings alongside the metadata, LanceDB's
multimodal lakehouse stores both the original data (including image, video or audio bytes)
and its vector representations alongside traditional tabular data in the same efficient format.

## Advantages of the Lance format

| Advantage          | Description                                                               |
| ------------------ | ------------------------------------------------------------------------- |
| Multimodal storage | Efficiently holds vectors, images, videos, audio, text, and more          |
| Version control    | Built-in data versioning for reproducible ML experiments and data lineage |
| ML-optimized       | Designed for training and inference workloads with fast random access     |
| Query performance  | Columnar storage enables blazing-fast vector search and analytics         |
| Cloud-native       | Seamless integration with cloud object stores (S3, GCS, Azure Blob)       |

## Key concepts

The following concepts are core to the Lance format:

<Steps>
  <Step>
    Data storage is **columnar** and is **interoperable** with other columnar formats (such as Parquet) via Arrow
  </Step>

  <Step>
    Data is divided into **fragments** that represent a subset of the data. Fragments are chunks of data in a Lance dataset. Each fragment includes multiple files that contain several columns in the chunk of data that it represents.
  </Step>

  <Step>
    Data is **versioned**, with each insert operation creating a new version of the dataset and an update to the manifest that tracks versions via metadata
  </Step>
</Steps>

### Data versioning

Data in Lance tables are versioned -- this helps keep LanceDB scalable and consistent.
We do not immediately blow away old versions when creating new ones because other clients might be
in the middle of querying the old version. It's important to retain older versions for as long as they
might be queried.

Each version contains metadata and just the new/updated data in your transaction. So if you have 100
versions, they aren't 100 duplicates of the same data. However, they do have 100x the metadata overhead
of a single version, which can result in slower queries.

### Data compaction

As you insert more data, your dataset will grow and you'll need to perform compaction to maintain query
throughput (i.e., keep latencies down to a minimum). Compaction is the process of merging fragments
together to reduce the amount of metadata that needs to be managed, and to reduce the number of files
that need to be opened while scanning the dataset.

### Performance Optimization Through Compaction

Compaction performs the following tasks in the background:

* Removes deleted rows from fragments
* Removes dropped columns from fragments
* Merges small fragments into larger ones

### Data deletion and recovery

Although Lance allows you to delete rows from a dataset, it does not actually delete the data immediately.
It simply marks the row as deleted in the `DataFile` that represents a fragment.

For a given version of the dataset, each fragment can have up to one deletion file (if no rows were ever
deleted from that fragment, it will not have a deletion file). This is important to keep in mind because
it means that the data is still there, and can be recovered if needed, as long as that version still
exists based on your backup policy.

<Card title="Learn more about Lance" icon="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=1c7311e59aacc6a085345618f357d380" href="https://lance.org/quickstart" data-og-width="1820" width="1820" data-og-height="1790" height="1790" data-path="static/assets/logo/lance-logo-gray.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=ed448d64255aa056dc20667ba41b1ae5 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=39a717a458214da2e1b8aceed6105354 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=ae715fa3264b36868def4c0017d7bb64 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=c9c74bcca7784c7fbb57be2012e23701 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=8ada40df0308bbbc934cf36a2894e0cd 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/logo/lance-logo-gray.svg?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=8611e35177202da4f179550c743d2270 2500w">
  Lance is a separate open source project. Check out its documentation to learn more.
</Card>
