# Source: https://docs.pinecone.io/guides/index-data/data-ingestion-overview.md

# Data ingestion overview

> Learn about the different ways to ingest data into Pinecone.

<Tip>
  To control costs when ingesting large datasets (10,000,000+ records), use [import](/guides/index-data/import-data) instead of upsert.
</Tip>

## Import from object storage

[Importing from object storage](/guides/index-data/import-data) is the most efficient and cost-effective method to load large numbers of records into an index. You store your data as Parquet files in object storage, integrate your object storage with Pinecone, and then start an asynchronous, long-running operation that imports and indexes your records.

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

## Upsert

For ongoing ingestion into an index, either one record at a time or in batches, use the [upsert](/guides/index-data/upsert-data) operation. [Batch upserting](/guides/index-data/upsert-data#upsert-in-batches) can improve throughput performance and is a good option for larger numbers of records if you cannot work around import's current [limitations](/guides/index-data/import-data#import-limits).

## Ingestion cost

* To understand how cost is calculated for imports, see [Import cost](/guides/manage-cost/understanding-cost#imports).
* To understand how cost is calculated for upserts, see [Upsert cost](/guides/manage-cost/understanding-cost#upsert).
* For up-to-date pricing information, see [Pricing](https://www.pinecone.io/pricing/).

## Data freshness

Pinecone is eventually consistent, so there can be a slight delay before new or changed records are visible to queries. You can view index stats to [check data freshness](/guides/index-data/check-data-freshness).
