# Source: https://docs.startree.ai/corecapabilities/manage-data/upsert-compaction-srt.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Compaction after Upserts

After enabling upserts, steps must be taken to optimize storage and maintain performance. Old and invalid documents are to be physically removed from the system rather than just being logically hidden. Merging small segments into larger ones reduces the number of segments scanned by queries, improving response times. Where applicable, rolling up records by time windows or other dimensions further reduces data volume and increases efficiency. Segments that no longer contain valid documents should also be cleaned up, since retaining them adds overhead without benefit. Together, these actions keep upsert-enabled tables performant and storage-efficient.

## How does StarTree Cloud solve it?

To simplify this process and reduce the burden on operators, **StarTree Cloud** provides the **Segment Refresh Task**. Instead of requiring manual compaction and cleanup, this task automates the entire process of segment replacement. It takes a set of input segments, processes them to generate new segments by merging, transforming, or rolling up the data, and then atomically replaces the old segments with the new ones. With this mechanism, queries always see a consistent dataset, even when replacement is in progress. The Segment Refresh Task, therefore, offers a better, more reliable way to manage upserts in Pinot, ensuring correctness while optimizing storage and performance.

## What is Segment Refresh Task and How It Works?

The Segment Refresh Task runs as a background minion task within **StarTree Cloud** and is designed to improve both storage and query efficiency.
For example, imagine a table with three segments: `S1`, `S2`, and `S3`. Over time, updates have invalidated many rows across these segments. When the Segment Refresh Task is executed, it collects `S1`, `S2`, and `S3` as input and creates a new merged segment, say `S3_refreshed`.

This new segment is immediately made visible to queries, while the old segments with no valid documents are removed eventually. The result is that queries only need to scan the refreshed segment, which reduces latency and saves storage space. Importantly, this process guarantees **atomicity**: queries never encounter a partial replacement where some data is missing or duplicated.
Read more about [Segment Refresh Task](https://docs.startree.ai/corecapabilities/manage-data/segment-refresh-task)

## How StarTree Segment Refresh Task competes with Apache Pinot Upsert Compaction Task?

### Segment Refresh Task automatically compacts and merges segments while rebuilding indexes, ensuring new data stays optimized

Unlike the Upsert Compaction Task, which only handled basic compaction, the Segment Refresh Task goes further by merging small, fragmented segments into larger ones, dropping invalidated records, and rebuilding indexes in the same process. This not only reduces storage overhead but also ensures that queries benefit from fully optimized index structures on refreshed data, leading to consistently faster response times even as datasets grow.

### Segments are replaced atomically across servers, so queries continue to run smoothly while Minion rolls out the refreshed segments in the background

For upsert tables, this atomicity is achieved by leveraging bitmaps instead of just lineage-based routing flips. New segments are made visible to queries immediately, but their bitmaps start empty and fill as updates are applied, while old segments gradually drain to empty. This guarantees that queries never see partial data or miss valid documents. Because replacement happens atomically across all servers, query consistency is preserved end-to-end, even while Minion is refreshing and swapping segments in the background.

## Things to Keep an Eye On While Configuring the Segment Refresh Task

While the Segment Refresh Task is powerful, careful configuration is key to getting the best results. Running the task too frequently can put unnecessary strain on the system, as it may end up processing nearly all segments repeatedly. On the other hand, running it too infrequently can cause storage to grow and query performance to degrade.

It is important to configure thresholds that determine when segments should be refreshed, ensuring that only segments with a significant number of invalid documents are selected. Another consideration is the **buffer period**, which allows the system to skip the most recent segments that are still ingesting new records. This avoids conflicts between ingestion and refresh.

Segment naming conventions also matter, as consistently naming refreshed segments makes tie-breaking deterministic when conflicts arise.

## Example: Configuring Segment Refresh Task for Upsert Table

You can configure the Segment Refresh Task as shown below. Include this in your table config:

```json  theme={null}
"tasks": {
  "SegmentRefreshTask": {
    "schedule": "0 0 2 * * ?",       // Cron schedule (here: run daily at 2 AM)
    "bufferTimePeriod": "1h",      // Skip segments committed in the last 1 hour
    "invalidRecordsThresholdPercent": 20,   // Refresh only if more than 20% records are invalid
    "desiredSegmentSize": "500MB", // Target size of  output segment
    "tableMaxNumTasks": "100"
   }
}
```

### Explanation of Key Parameters

* **schedule**: Defines when the task should run. In the above example, it runs every day at 2 AM.
* **bufferTimePeriod**: Ensures the most recent segments are skipped, so ingestion is not disrupted. (This is required because the EndOffset of the latest committed segment is used to resume ingestion and hence this segment shouldn’t be merged)
* **invalidRecordsThresholdPercent**: Only triggers a refresh if a large enough portion of the segment’s records have been invalidated by upserts.
* **maxNumRecordsPerSegment**: Prevents the creation of overly large output segments by setting a record count limit.
* **desiredSegmentSize**: Defines the desired output segment size. Larger segments improve query performance by reducing segment lookups, but may increase scan time. The default size is 500 MB.
* **tableMaxNumTasks**: Max number of sub tasks a table can run at each schedule. Refer best practices for details on how to configure this

## Best Practices for Running Segment Refresh Task (SRT) on Upsert Tables

Use SRT scheduling and configuration as part of your table lifecycle management strategy.
Balancing frequency, task limits, and cleanup intervals ensures stable performance and predictable cluster behavior over time.

### 1. Schedule SRT and Upsert Snapshot Tasks Carefully

Ensure that the **Upsert Snapshot Task** is scheduled **after** the **SRT task** completes.
This ensures that snapshots are created using the latest segments produced by SRT, avoiding inconsistencies between snapshot data and segment versions.

***

### 2. Tune SRT Frequency and Parallelism

Running SRT efficiently requires balancing **Minion task cost**, **query performance**, and **cluster stability**.
Use the following two-step approach to optimize configuration.

#### a. Optimize SRT Frequency

Understand the trade-off between **minion cost** (to run SRT) and **query performance** (affected by segment growth).

* **Recommended setup:** Schedule SRT based on the average rate of data updates.
  * Example: If data updates every 12 hours, run SRT every 12 hours.
* Adjust SRT frequency up or down to balance Minion compute cost with acceptable query latency.

#### b. Set an Appropriate `tableMaxNumTasks`

Avoid spawning too many subtasks, which can degrade **controller performance**, cause **Helix state transition delays**, and extend **segment replacement times** — potentially impacting availability.

Use the following guideline to determine a safe `tableMaxNumTasks` value:

| Symbol | Description                                                           | Example |
| ------ | --------------------------------------------------------------------- | ------- |
| **X**  | Time to replace a segment in the server (approx. 30 seconds)          | 30      |
| **Y**  | Parallelism (25% of total CPU cores)                                  | —       |
| **Z**  | `pinot.broker.new.segment.expiration.seconds` (default: 3600 seconds) | 3600    |
| **A**  | Number of servers where the table is hosted                           | —       |
| **B**  | Table replication factor                                              | —       |

**Recommended formula:**

```text  theme={null}
tableMaxNumTasks = (Z * Y * A / X / B) * 0.75

Note: The 0.75 multiplier adds a buffer for random variance in timing.
```

If tableMaxNumTasks is insufficient to complete SRT in a single run, **increase SRT frequency** to trigger multiple runs within the desired schedule determined by step (a).

#### c. First-Time SRT Execution

If running SRT for the first time on an existing table (with many old segments), temporarily increase
pinot.broker.new\.segment.expiration.seconds to **\~12 hours**.

This prevents throttling and server-side congestion, since the initial SRT run may pick up a large number of old segments from the same partition.

***

### 3. Manage Segment Cleanup Between SRT Runs

To maintain data freshness and prevent segment buildup, ensure the table commits **one segment per partition** between consecutive SRT runs.
This helps cleanup the older segments and ensures subsequent SRT runs execute efficiently.

Built with [Mintlify](https://mintlify.com).
