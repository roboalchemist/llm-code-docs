# Source: https://docs.lancedb.com/indexing/reindexing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keeping Indexes Up-to-Date with Reindexing

> Learn how to keep your indexes up-to-date in LanceDB using incremental indexing, including best practices for adding new records without full reindexing.

export const ReindexingIncremental = "table = db.open_table(\"reindexing_incremental\")\ntable.add([{\"vector\": [3.1, 4.1], \"text\": \"Frodo was a happy puppy\"}])\ntable.optimize()\n";

As you add new data to your LanceDB tables, your indexes may become outdated.
Reindexing is the process of updating the index to account for new data -- this applies to either a full-text search (FTS) index or a vector index. Reindexing is an important operation to run periodically as your data grows, as it has performance implications.

As data is being added and a reindex operation is running, LanceDB will combine results from the existing index with exhaustive/flat search on the new data. This is done to ensure that you're still retrieving results over all your data, but it does come at a performance cost. The more data that you add without reindexing, the impact on latency (due to exhaustive search) can be noticeable.

Rather than dropping an existing index entirely and reindexing from scratch, LanceDB supports **incremental indexing**.

## Incremental Indexing

<Badge color="green">OSS</Badge>

In LanceDB OSS, you can manually trigger an incremental indexing operation using the `optimize()`
method on a table. This will perform compaction, pruning and updating of the index on the specified
table.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ReindexingIncremental}
  </CodeBlock>
</CodeGroup>

<Badge color="purple">Cloud</Badge>
<Badge color="red">Enterprise</Badge>

LanceDB Cloud/Enterprise support incremental reindexing through an automated background process. When new data is added to a table, the system automatically triggers a new index build. As the dataset grows, indexes are asynchronously updated in the background.

* While indexes are being rebuilt, queries use brute force methods on unindexed rows, which may temporarily increase latency. To avoid this, set `fast_search=True` to search only indexed data.
* Use `index_stats()` to view the number of unindexed rows. This will be zero when indexes are fully up-to-date.

<Tip>
  **Performance and simplicity**

  The benefit of using LanceDB Cloud & Enterprise is that they automate the reindexing process
  and operate continuously in the background, minimizing the impact on latency under high loads.
  In OSS, you must manually manage the reindexing cadence based on your data growth and performance needs.
</Tip>
