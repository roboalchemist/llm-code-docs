# Source: https://docs.startree.ai/corecapabilities/manage-data/segment-refresh-task.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment Refresh Task

The `SegmentRefreshTask` reads the latest table config and refreshes the segments if they are not consistent with the table config. When an inconsistency between segments and table config is detected, it will download the segments from the deep store, process and regenerate the segments, and then push them back to replace the old segments atomically.

## Supported Operations

The following operations can be applied to the segments to match the table config:

* Time partitioning: Re-partition the segments to be time partitioned (all the records within a segment are in the same time bucket).
* Value partitioning: Re-partition the segments according to the partitioning config.
* Merge/Split: Merge small segments or split large segments (with rollup support) to ensure segments are properly sized.
* Other table config changes that cannot be applied on the server side with segment reload:
  * Change time column
  * Change sorted column
  * Change column data type
  * Change column encoding

<Warning>
  complexTypeConfig transforms are not supported with the Segment Refresh Task. The `complexTypeConfig` configuration is used as a part of the `ingestionConfig` to flatten and process complex-type data. **Do not** use the Segment Refresh Task when the `complexTypeConfig` configuration is enabled. This may result in records being duplicated and unintended changes to tables.
</Warning>

## How to configure the SegmentRefreshTask

Configure the SegmentRefreshTask under the `taskConfig` section in the table configuration.

| Property Name           | Required            | Description                                                                                                                                                                                                                         |
| ----------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucketTimePeriod        | Yes                 | Time bucket for segments (e.g. 1d).                                                                                                                                                                                                 |
| maxNumRecordsPerSegment | No (default 5M)     | Max (desired) number of records in each segment. The task will try to resize all segments to this size after applying the partitioning constraints.                                                                                 |
| skipSegmentIndexCheck   | No (default false)  | If set to true, the index check (see the next section) will be skipped. This check requires pulling all segments' metadata from the servers, which can be costly for large table.                                                   |
| tableMaxNumTasks        | No (default 10)     | Max number of parallel tasks a table can run at each schedule. This value can be tuned based on the Minion instances in the cluster. It has to be positive.                                                                         |
| maxNumRecordsPerTask    | No (default 50M)    | Max number of records processed in a single task. Each task is executed by a single Minion instance, so the records processed should be limited to prevent the Minion from running out of resources. It has to be a positive value. |
| maxDataSizePerTask      | No (default 5 GB)   | Max size of data provided to a single task.                                                                                                                                                                                         |
| desiredSegmentSize      | No (default 500 MB) | User specified size for a segment.                                                                                                                                                                                                  |
| batchSegmentUpload      | No                  | Boolean field for which the default value is `false`. When the value is set to `true` segments are uploaded in batch mode which is faster than uploading segments one after the other.                                              |
| mergeType               | No                  | Same definition as in the [MergeRollupTask](https://docs.pinot.apache.org/operators/operating-pinot/minion-merge-rollup-task#config).                                                                                               |
| roundBucketTimePeriod   | No                  | Same definition as in the [MergeRollupTask](https://docs.pinot.apache.org/operators/operating-pinot/minion-merge-rollup-task#config).                                                                                               |
| \*.aggregationType      | No                  | Same definition as in the [MergeRollupTask](https://docs.pinot.apache.org/operators/operating-pinot/minion-merge-rollup-task#config).                                                                                               |

## Segment Index Check

When segment index check is enabled, the task generator will pull the segment metadata for each segment from the servers, and compare it with the table config. If the segment metadata is not consistent with the table config, the segment will be refreshed.

The following properties are compared between the segment metadata and the table config:

* Whether the time column is the same.
* Whether the partitioning info matches:
  * Same partition column
  * Same partition function
  * Same partition count
  * Segment belong to a single partition
* Sorted column in the table config is sorted in the segment.
* Checks for all columns:
  * Column is added (while this can be handled through a server reload, the task has been extended, so that it can be performed in one go and through Minions.)
  * Column is deleted.
  * Column field type change.
  * Column data type change.
  * Column SV/MV change.
  * Column encoding change.

## Example Configuration

```json  theme={null}
    "task": {
      "taskTypeConfigsMap": {
        "SegmentRefreshTask": {
          "bucketTimePeriod": "1d",
          "maxNumRecordsPerSegment": "2000000",
          "maxNumRecordsPerTask": "10000000",
          "schedule": "0 */30 * * * ?"
        }
      }
    }
```

## Real-time Tables

For real-time tables, the SegmentRefreshTask considers segments which are in COMPLETED state. The consuming segments are left untouched.

### Upsert Table

This task can work with real-time table enabled Upserts as well. The task can compact segments, i.e. removing invalid docs; and then merge segments into bigger one. There are some limitations when this task is enabled for upsert tables, mainly due to the complexity from managing the upsert metadata consistently for upsert to work.

1. Records can't be rolled up because the primary keys must be kept intact before and after refreshing.
2. The task performs M:1 merging, i.e. combining multiple input segments into one new segment, to simplify failure handling for tracking upsert metadata consistently. With M:1 mapping, data repartitioning and bucketizing are not supported.

Most of the task configs described above are ignored, except `"maxNumRecordsPerSegment": "2000000"` . This setting configures how large the output segment should be, and the input segments are automatically decided for each task, based on how many valid records they have.

In addition to adding the SegmentRefreshTask configurations to enable the minion task for the upsert table, the "rocksdb.segmentmerge.enable" setting must also be specified under the upsertConfig section of the table configuration, as shown below. This flag ensures that during upsert, the system uses the 'refreshed\_' segment in case of identical seqId values—favoring it over older segments based on creation time.

Note that a server restart is required for this configuration to take effect. The flag is currently set to false by default to allow incremental adoption of the feature. It will be enabled (true) by default in future releases.

```json  theme={null}
  "upsertConfig" : {
        ...
        "metadataManagerConfigs": {
            "rocksdb.segmentmerge.enable": "true"
            ...
        }
    }
```

Order of operations when enabling the SegmentRefreshTask on an upsert enabled table:

1. Set the feature flag
2. Restart the servers
3. Enable the SegmentRefreshTask

## Note

It is necessary to validate whether this task is compatible with real-time tables that have deduplication enabled.
Given that the Segment Refresh Task already performs both compaction and segment merging, introducing the UpsertCompactionTask—which is limited to compaction—should be avoided to prevent redundant processing.

Built with [Mintlify](https://mintlify.com).
