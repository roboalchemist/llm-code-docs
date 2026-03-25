# Source: https://docs.startree.ai/corecapabilities/manage-data/alter-table-task.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Alter Table Task

The `AlterTableTask` ensures that segments remain in sync with the latest Pinot table configuration by detecting inconsistencies, processing changes (such as re-sorting, re-partitioning, or adding indexes), and replacing outdated segments atomically. It acts as an auto-optimizer for the table by transitioning it from its current state to the desired state, ensuring optimal performance.

## How is the Alter Table Task different from the Segment Refresh Task?

The StarTree Alter Table Task is an improved alternative to the [Segment Refresh Task](/corecapabilities/manage-data/segment-refresh-task), and is designed for more efficient, batch-wise segment refreshes.

The Segment Refresh Task performs the map and segment generation phases locally, which leads to inefficiencies due to redundant segment creation and merging. The StarTree Alter Table Task optimizes this process by writing all mapper output files to a single location, allowing segments to be generated directly from the output. This approach eliminates the extra merge step, reducing overhead and improving performance.

In addition, the Alter Table task follows a structured Map → Reduce → Upload workflow. This workflow ensures better resource utilization and fault tolerance. Built-in retries that dynamically adjust parameters provide a more scalable and reliable approach for large table refreshes.

## When is the Alter Table Task used?

* Re-partitioning in case of a change in the partition columns.
* Re-sorting by changing the sorted column.
* Merge/Split: Merge small segments or split large segments (with rollup support) to ensure segments are properly sized.
* Change column Data Type.
* Change column Encoding.
* Adding new indexes.
* Other table config changes that cannot be applied on the server side with segment reload.

## How does the Alter Table Task work?

The Alter Table Task is a [Minion](/corecapabilities/ingestdata/adv-concepts/batch/overview#pinot-minions%3A-cluster-native-ingestion-%26-processing) task in Apache Pinot, designed to run asynchronously without affecting real-time or offline ingestion.

The Alter Table Task refreshes table segments in batches. In each batch, the task selects a subset of segments, processes them, and replaces them in the original table. The process repeats until all segments are updated.

<Note>
  If new segments requiring a refresh arrive during an ongoing batch, they are deferred until the current batch completes.
</Note>

### Example Workflow

Suppose we need to refresh a 10TB table, with the following table configuration:

* **tableMaxNumTasks**:  100 (this is the default value)
* **desiredSegmentSize**: 500MB

The Alter Table Task workflow splits the table into batches based on this formula:

* Each task processes data volumes up to 3 times the desiredSegmentSize (or maxNumRecordsPerSegment). In our example, this will be 3 \* 500MB = \~1.5GB.
* We can run a maximum of 100 concurrent tasks for the table, or \~150GB in each batch for our table.
* Therefore, it will take approximately 70 batches (10TB / \~150GB = \~70) to process our 10TB table.

### Batch Processing Stages

Here's a brief description of each of the stages within a single batch:

* The **Map Phase** reads input segments and generates intermediate files. Each subtask partitions the data (`partition_timeBucket`) and uploads the files to deep storage.
* The **Reduce Phase** downloads the necessary intermediate files, processes them to generate new segments and metadata, and then uploads both to deep storage.
* The **Upload Phase** retrieves the list of `fromSegments` from metadata, determines `toSegments` from deep storage, and performs batch segment replacement. By default, batch upload is used as it is the most efficient mode.

All stages are associated with the same **session ID**, ensuring continuity and data integrity.

## Enabling the Alter Table Task

<Warning>
  complexTypeConfig transforms are not supported with the Alter Table Task. The `complexTypeConfig` configuration is used as a part of the `ingestionConfig` to flatten and process complex-type data. **Do not** use the Alter Table Task when the `complexTypeConfig` configuration is enabled. This may result in records being duplicated and unintended changes to tables.
</Warning>

To enable the Alter Table Task, simply configure it in your table configuration as follows:

1. In the **“taskTypeConfigMap”** add a new object called **“StarTreeAlterTableTask”** (the JSON path in the Pinot table config should be: `task.taskTypeConfigsMap.StarTreeAlterTableTask`).
2. Add the following configuration:

```json  theme={null}
{
 ...,
 "taskTypeConfigsMap": {
  "StarTreeAlterTableTask": {
      "bucketTimePeriod": "1d",
   "desiredSegmentSize": "500MB",
           "schedule": "0 */10 * ? * * *"
        },
 ...
 },
 ...
}
```

1. Run the task immediately using the **/tasks/execute** POST API, or wait for the cron job to trigger it (in the example above, this would be every 10 minutes).

## Configuration Parameters

| Parameter          | Required | Default Value | Description                                                                                                                                                                                                                                      |
| ------------------ | -------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| bucketTimePeriod   | Yes      | 1d            | Defines the time interval for creating new segments. Multiple segments can be generated within the same bucketTimePeriod if they exceed the maximum segment size. However, a single segment should never span beyond its assigned bucket period. |
| desiredSegmentSize | No       | 500MB         | Defines the desired output segment size. Larger segments improve query performance by reducing segment lookups, but may increase scan time.                                                                                                      |
| schedule           | Yes      |               | How often to run the task. It should typically be every 10 minutes.                                                                                                                                                                              |

## Monitoring

You can monitor the StarTree Alter Table Task in two levels of granularity:

* **Batch-Level**: Monitoring individual task batches.
* **Cycle-Level**: Tracking overall task cycles.

### Batch-Level Monitoring

Batch-level monitoring can be done using the Minion Task Manager or Minion Metadata.

* **Name-Based Task Monitoring**: Each task name contains two key details:
  * **Session ID**: Identifies a specific batch within a cycle.
  * **Task Phase**: Indicates whether the task is in the Map, Reduce, or Upload phase.
  * Since multiple batches can run within a cycle, they are linked together using the session ID.
* **Minion Metadata-Based Monitoring**: Minion Metadata provides real-time batch tracking through Zookeeper:
  * **Path**: Zookeeper Browser -> MINION\_TASK\_METADATA -> TableName -> StarTreeAlterTableTask.
  * Each batch has a fixed list of input segments, which remains unchanged during processing.

### Cycle-Level Monitoring

Cycle-level monitoring helps track the overall progress of the Alter Table Task across multiple batches.

**Progress Tracking & Estimation API:**

* **Endpoint**: `/alterTable/tableNameWithType/estimatedTime`
* **Method**: GET

**Sample Response**:

```json  theme={null}
{
  "estimatedCompletionTimeMs": "123456789",
  "percentProgress": "50.37"
}
```

### New Timer Metrics for Observability

Additional metrics have been introduced for better tracking of each task phase:

* **ALTER\_TABLE\_MAP\_PHASE\_DURATION\_MS**: Time taken for the **Map** phase.
* **ALTER\_TABLE\_REDUCE\_PHASE\_DURATION\_MS**: Time taken for the **Reduce** phase.
* **ALTER\_TABLE\_UPLOAD\_PHASE\_DURATION\_MS**: Time taken for the **Upload** phase.

These metrics help monitor task performance and identifying potential bottlenecks during execution.

## Migrating from the Segment Refresh Task

<Info>
  To migrate, simply change the task name from SegmentRefreshTask to StarTreeAlterTableTask.
</Info>

The Alter Table Task configuration is backward compatible with the Segment Refresh Task. Only one of these tasks is needed, so there is no need to run both.

<Tip>
  The Alter Table Task will eventually replace the Segment Refresh Task as the default.
</Tip>

## Handling Task Failures and Retries

Minion subtasks can fail due to various reasons. When this happens, tasks are automatically retried with adjusted configurations to improve success rates:

* **Map Phase**: maxBatchBytes = maxBatchBytes/(retryCount + 1).
* **Reduce Phase**: numSegmentGenerationThreads = numSegmentGenerationThreads/2, with a minimum value of 1.

By handling failures efficiently, the system ensures seamless segment refreshes with minimal disruptions.

Built with [Mintlify](https://mintlify.com).
