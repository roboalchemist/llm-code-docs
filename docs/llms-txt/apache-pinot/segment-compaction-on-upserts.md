# Source: https://docs.pinot.apache.org/release-1.1.0/basics/data-import/segment-compaction-on-upserts.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/data-import/segment-compaction-on-upserts.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/data-import/segment-compaction-on-upserts.md

# Source: https://docs.pinot.apache.org/release-1.4.0/manage-data/data-import/upsert-and-dedup/segment-compaction-on-upserts.md

# Source: https://docs.pinot.apache.org/manage-data/data-import/upsert-and-dedup/segment-compaction-on-upserts.md

# Segment compaction on upserts

## Overview of segment compaction

Compacting a segment replaces the completed segment with a compacted segment that only contains the latest version of records. For more information about how to use upserts on a real-time table in Pinot, see [Stream Ingestion with Upsert](https://docs.pinot.apache.org/manage-data/data-import/upsert-and-dedup/upsert).

The Pinot upsert feature stores all versions of the record ingested into immutable segments on disk. Even though the previous versions are not queried, they continue to add to the storage overhead. To remove older records (no longer used in query results) and reclaim storage space, we need to compact Pinot segments periodically. Segment compaction is done via a new minion task. To schedule Pinot tasks periodically, see the [Minion documentation](https://docs.pinot.apache.org/basics/concepts/components/cluster/minion).

## Compact segments on upserts in a real-time table

To compact segments on upserts, complete the following steps:

1. Ensure task scheduling is enabled and a minion is available.
2. Add the following to your table configuration. These configurations (except `schedule)`determine which segments to compact.

```
"task": {
  "taskTypeConfigsMap": {
    "UpsertCompactionTask": {
      "schedule": "0 */5 * ? * *",
      "bufferTimePeriod": "7d",
      "invalidRecordsThresholdPercent": "30",
      "invalidRecordsThresholdCount": "100000",
      "tableMaxNumTasks": "100",
      "validDocIdsType": "SNAPSHOT"
    }
  }
}
```

* `bufferTimePeriod:` To compact segments once they are complete, set to `“0d”`. To delay compaction (as the configuration above shows by 7 days (`"7d"`)), specify the number of days to delay compaction after a segment completes.
* `invalidRecordsThresholdPercent` (Optional) Limits the older records allowed in the completed segment as a percentage of the total number of records in the segment. In the example above, the completed segment may be selected for compaction when 30% of the records in the segment are old.
* `invalidRecordsThresholdCount` (Optional) Limits the older records allowed in the completed segment by record count. In the example above, if the segment contains more than 100K records, it may be selected for compaction.
* `tableMaxNumTasks` (Optional) Limits the number of tasks allowed to be scheduled.
* `validDocIdsType` (Optional) Specifies the source of validDocIds to fetch when running the data compaction. The valid types are `SNAPSHOT`, `IN_MEMORY`, `IN_MEMORY_WITH_DELETE`
  * `SNAPSHOT`: Default validDocIds type. This indicates that the validDocIds bitmap is loaded from the snapshot from the Pinot segment. UpsertConfig's `enableSnapshot` must be enabled for this type.
  * `IN_MEMORY`: This indicates that the validDocIds bitmap is loaded from the real-time server's in-memory.&#x20;
  * `IN_MEMORY_WITH_DELETE`: This indicates that the validDocIds bitmap is read from the real-time server's in-memory. The valid document ids here does take account into the deleted records. UpsertConfig's `deleteRecordColumn` must be provided for this type.

{% hint style="warning" %}
When using the two in-memory types, if the server gets restarted, the upsert view gets back consistent once server re-ingests the data it has ingested before starting. The in-memory bitmaps are updated when server ingests data into consuming segment, even before the consuming segment gets committed. So if server gets restarted whlie still consuming data, the upsert view gets back consistent once it catches up the previously ingested data. Instead, the bitmap snapshots are only taken after committing the segment, thus can be more consistent on server restarts, but is eventually consistent as well if server gets restarted while ingesting data.
{% endhint %}

{% hint style="info" %}
Because segment compaction is an expensive operation, we **do not recommend** setting `invalidRecordsThresholdPercent and invalidRecordsThresholdCount` too low (close to 1). By default, all configurations above are `0`, so no thresholds are applied.
{% endhint %}

## Example

The following example includes a dataset with 24M records and 240K unique keys that have each been duplicated 100 times. After ingesting the data, there are 6 segments (5 completed segments and 1 consuming segment) with a total estimated size of 22.8MB.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fszeg8WTNWs2tGQaHtE2h%2FScreenshot%202023-09-28%20at%2012.00.05%20PM.png?alt=media&#x26;token=2cd08ac8-75b1-4569-98d6-dddd5ecd5020" alt=""><figcaption><p>Example dataset</p></figcaption></figure>

Submitting the query `“set skipUpsert=true; select count(*) from transcript_upsert”` before compaction produces 24,000,000 results:

<div align="left"><figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FQLMGdylZi9gbHAaukt8v%2FScreenshot%202023-09-28%20at%2012.04.07%20PM.png?alt=media&#x26;token=c6f1573a-06c5-4ab0-aac2-bf888b1ea99b" alt="" width="265"><figcaption><p>Results before segment compaction</p></figcaption></figure></div>

After the compaction tasks are complete, the [Minion Task Manager UI](https://docs.pinot.apache.org/basics/concepts/components/cluster/minion#task-manager-ui) reports the following.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2Fsjkr7NUzImwCfmrn6qTP%2FScreenshot%202023-09-28%20at%2012.07.22%20PM.png?alt=media&#x26;token=c7ff60fc-6691-473c-9886-4307c98742f8" alt=""><figcaption><p>Minion compaction task completed</p></figcaption></figure>

Segment compactions generates a task for each segment to compact. Five tasks were generated in this case because 90% of the records (3.6–4.5M records) are considered ready for compaction in the completed segments, exceeding the configured thresholds.

{% hint style="info" %}
If a completed segment only contains old records, Pinot immediately deletes the segment (rather than creating a task to compact it).
{% endhint %}

Submitting the query again shows the count matches the set of 240K unique keys.

<figure><img src="https://459170765-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LtH6nl58DdnZnelPdTc-887967055%2Fuploads%2FEyUY5mWduyYnRe9D96vC%2FScreenshot%202023-09-28%20at%2012.20.05%20PM.png?alt=media&#x26;token=eda5289b-2a9b-4bfc-9bd3-5abd90751e96" alt=""><figcaption><p>Results after segment compaction</p></figcaption></figure>

Once segment compaction has completed, the total number of segments remain the same and the total estimated size drops to 2.77MB.

{% hint style="info" %}
To further improve query latency, merge small segments into larger one.
{% endhint %}
