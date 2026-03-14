# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/pauseless-consumption.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pauseless Consumption

# Introduction

Pauseless consumption enhances real-time analytics by minimizing ingestion delays. By allowing data ingestion to continue while the previous segment is being built and uploaded, it significantly reduces the latency gap between data arrival and query availability.

## How to Enable Pauseless Consumption

Enabling this feature involves two major phases: preparing the cluster/table and updating the configurations.

### Step 1: Preparation (Existing Tables Only)

If you are creating a new table from scratch, you may skip to Step 2. This step is mandatory for existing tables that currently consume data from a stream.

#### Pause Ingestion

Stop data ingestion to ensure all current segments are committed across all servers/replicas.

**API**: `POST /tables/{tableName}/pauseConsumption`

#### Verify Inactive State

Confirm that no consuming segments are active before proceeding.

* Ideal State: Verify that all segments are marked as ONLINE.
* Consuming Info: Use the API below to check for active segments.

**API**: `GET /tables/{tableName}/consumingSegmentsInfo`
<br /> **Success Criteria**: The field `_segmentToConsumingInfoMap` in the response must be empty.

### Step 2: Cluster & Controller Configuration

These changes are applied at the system level and require a restart of the Servers and Controllers.

a. **Enable Peer Download**: Ensure peer segment download is enabled on your cluster. Follow this documentation to do so.
<br />b. **Configure Deep Store Retry Interval**: The default deep store retry frequency is 24 hours (86400 seconds). For pauseless consumption, this must be reduced to 2 hours.
<br />c. **Update Cluster Configuration**: Add the following parameters to your cluster configuration to handle deep store uploads and the pauseless FSM scheme.

**API**: `POST /cluster/configs`
<br />Use the payload below to the API:

```json  theme={null}
{
    "controller.realtime.segment.deepStoreUploadRetryEnabled": "true",
    "pinot.server.instance.segment.upload.to.deep.store": "true",
    "pinot.controller.segment.completion.fsm.scheme.pauseless": "org.apache.pinot.controller.helix.core.realtime.PauselessSegmentCompletionFSM",
    "controller.segment.level.validation.intervalPeriod" : "7200s"
}
```

### Step 3: Table Configuration

Update the table configuration to enable the pauseless flag.

**Important**: The pauselessConsumptionEnabled flag must be placed outside of the streamConfigMaps array, directly under streamIngestionConfig.

```json  theme={null}
"ingestionConfig": {
  "streamIngestionConfig": {
    "pauselessConsumptionEnabled": true,
    "streamConfigMaps": [
      {
        "streamType": "kafka",
        "stream.kafka.topic.name": "githubEvents",
        "segment.completion.fsm.scheme": "pauseless"
      }
    ]
  }
}
```

### Step 4: Resume Ingestion

Once the configurations are applied and the system is restarted (if applicable), activate pauseless ingestion by resuming the table.

Use **API**: `POST /tables/{tableName}/resumeConsumption`

## How to Enable Pauseless Consumption for Dedup-enabled Table

Deduplication (Dedup) ensures data correctness by removing duplicate records based on primary keys during ingestion. When combined with Pauseless Consumption, users achieve both low-latency ingestion and data integrity. Dedup is available since the StarTree plugin release, 1.4.0-ST.39. Pauseless mode normally runs background tasks (build/commit) parallel to ingestion. However, because Dedup relies on knowing the exact state of previous data to identify duplicates, strict enforcement of ordering is required across replicas.

#### Step 1: Cluster Configuration

If enabling Dedup, you must add this flag to the controller config in addition to the above mentioned configuration:
controller.segment.error.autoReset=true

#### Step 2: Table Configuration

To enable dedup with pauseless, you need to add the following configs in addition to the above mentioned configuration:

```json  theme={null}
{
  "routing": {
    "instanceSelectorType": "strictReplicaGroup"
  },
  "segmentsConfig": {
    "peerSegmentDownloadScheme": "https"
  },
  "dedupConfig": {
    "dedupEnabled": true,
    "allowDedupConsumptionDuringCommit": false
  },
  "task": {
    "taskTypeConfigsMap": {
      "DedupSnapshotCreationTask": {
        "schedule": "0 0 12 * * ?"
      }
    }
  },
  "ingestionConfig": {
    "streamIngestionConfig": {
      "pauselessConsumptionEnabled": true,
      "enforceConsumptionInOrder": true,
      "useIdealStateToCalculatePreviousSegment": false,
      "parallelSegmentConsumptionPolicy": "ALLOW_DURING_BUILD_ONLY"
    }
  }
}
```

### Configuration Parameters

| Parameter                               | Value                      | Reason                                                                                                                             |
| :-------------------------------------- | :------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| dedupEnabled                            | true                       | Activates record-level deduplication.                                                                                              |
| allowDedupConsumptionDuringCommit       | false                      | Critical. Prevents new segments from consuming while the previous one is committing to ensure the dedup state is consistent.       |
| enforceConsumptionInOrder               | true                       | Ensures Segment N+1 cannot start until Segment N finishes. Prevents data gaps if a server lags.                                    |
| useIdealStateToCalculatePreviousSegment | false                      | Reduces Zookeeper load. The system has a built-in safety check (3-minute timeout) that handles this automatically.                 |
| parallelSegmentConsumptionPolicy        | ALLOW\_DURING\_BUILD\_ONLY | Ensures the semaphore is released only when the server keeps its exact local copy of data (the build phase), ensuring correctness. |

## Observability

| Metric Name                                       | Type              | Unit          | Description                                                                                     | Usage                                                                                                                                   |
| :------------------------------------------------ | :---------------- | :------------ | :---------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Controller Metrics**                            |                   |               |                                                                                                 |                                                                                                                                         |
| `PAUSELESS_CONSUMPTION_ENABLED`                   | Gauge (per-table) | Boolean (0/1) | Indicates whether pauseless consumption is enabled for the table.                               | Quick verification if pauseless mode is active for a table.                                                                             |
| `PAUSELESS_SEGMENTS_IN_ERROR_COUNT`               | Gauge (per-table) | Count         | Number of segments where ALL replicas are in ERROR state.                                       | Critical metric to detect when segments are completely failed across all replicas. Non-zero value indicates immediate attention needed. |
| `PAUSELESS_SEGMENTS_IN_UNRECOVERABLE_ERROR_COUNT` | Gauge (per-table) | Count         | Number of segments in COMMITTING state with all replicas in ERROR that cannot be auto-repaired. | Tracks segments that need manual recovery, typically for tables with dedup/partial upsert where auto-repair is disabled.                |
| **Server Metrics**                                |                   |               |                                                                                                 |                                                                                                                                         |
| `PAUSELESS_CONSUMPTION_ENABLED`                   | Gauge (per-table) | Boolean (0/1) | Server-side indicator of pauseless consumption status.                                          | Verify server and controller are in sync about pauseless mode.                                                                          |

### Measuring Ingestion Lag

To assess the impact of pauseless consumption, monitor the offset lag during ingestion using Grafana. Update the query for the metric, “Realtime Ingestion Delay in Ms (Avg)”,  as follows:

#### Ingestion Lag Query (Grafana)

```sql  theme={null}
    avg by (${GroupBy:csv}) (pinot_server_realtimeIngestionOffsetLag_Value{kubernetes_pod_name=~"$Server$" , table=~"$Tables$"})
```

### Debugging APIs

#### 1. Get Pauseless Debug Information

**Description:** Retrieves diagnostic information to identify segments that are stuck in COMMITTING or are in ERROR state.

**Usage:**

* **Error detection:** Identify which servers have segments in ERROR state.
* **Commit tracking:** Monitor segments that are stuck in the COMMITTING state.
* **Debugging hangs:** If commits appear stalled, check whether segments remain in the `committingSegments` list for extended periods.

**API**: `GET /tables/{tableName}/pauselessDebugInfo`

**Response**

```json  theme={null}
{
  "instanceToErrorSegmentsMap": {
    "Server_host1_8098": ["segment1", "segment2"],
    "Server_host2_8098": ["segment3"]
  },
  "committingSegments": [
    "tableName__0__123__20231201T1000Z",
    "tableName__1__456__20231201T1005Z"
  ]
}

```

#### 2. Get Re-ingestion Jobs

**Description:** Returns list of all currently running re-ingestion jobs.
<br /> **Usage:** Useful for monitoring auto-repair progress.
<br /> **API:** `GET /reingestSegment/jobs`

#### 3. Pauseless Debug Metadata Path

**Description:** Tracks all segments currently in COMMITTING state for debugging purposes.

**Usage:**

* Maintains a persisted list of segments that are currently in the commit process.
* Used by the controller to track the lifecycle of segment commits.
* Entries are automatically cleaned up once segments complete the commit.
* Useful for understanding which segments were in flight during failures and can be accessed using the API listed above.

**API:** `GET /PAUSELESS_DEBUG_METADATA/{tableNameWithType}`

**Response:**

```json  theme={null}
{
  "id": "tableName_REALTIME",
  "listFields": {
    "committingSegments": [
      "tableName__0__123__20231201T1000Z",
      "tableName__1__456__20231201T1005Z"
    ]
  }
}
```

## Operational Troubleshooting

### Ordering Enforcement

Pinot enforces segment ordering using a `ConsumerCoordinator` that serializes Helix `OFFLINE → CONSUMING` state transitions.

Consumers wait for prior segments to either finish consumption or be fully loaded before starting to consume new segments. This guarantees strict ordering and prevents gaps in data ingestion.

The enforcement strategy depends on the `useIdealStateToCalculatePreviousSegment` flag. It is strongly recommended to keep this flag set to `false` to avoid additional load on Zookeeper. Pinot includes a built-in safety mechanism that handles ordering without relying on IdealState.

### Segment Build Failures (Rollback)

In rare scenarios, such as a server crash before a segment is uploaded, it may be necessary to roll back ingestion to the last successfully committed segment.

To perform a rollback:

1. Pause ingestion for the table.
2. Identify the last valid committed segment.
3. Execute the delete operation using the Delete from Sequence Number API.

**API**: `DELETE /deleteSegmentsFromSequenceNum/{tableNameWithType}?segments=segmentA,segmentB`

This operation deletes all segments with a sequence ID greater than or equal to the specified segment.
4\. Resume ingestion for the table.

### Server Restart Hangs

If a server restarts and continues consuming data but does not transition to the `READY` state, follow these steps:

1. Pause ingestion for the table.
2. Wait for the server to transition to `READY`. This typically takes a few minutes.
3. Resume ingestion. Once resumed, the server will catch up quickly.

### Ingestion Lag Spikes

When enabling pauseless consumption, ingestion must be paused first. Resuming ingestion forces a commit of all active segments simultaneously.

During this transition, expect a temporary spike in controller load and ingestion lag. This behavior is expected and limited to the enablement phase.

### COMMITTING vs ERROR State

If a segment is in the `COMMITTING` state in Zookeeper but appears as `ERROR` or `OFFLINE` in the External View, corrective validation is required.

Run the Realtime Segment Validation job manually, or wait for the scheduled execution. The default schedule runs every 30 minutes.

### Key Logging Patterns for Debugging

#### Success Path Logs

* "Starting to commit changes to ZK and ideal state for the segment:{} during pauseless ingestion"
* "Successfully updated segment metadata for segment: {}"
* "Removing segment: {} from committing segment list"

#### Warning Logs

* "Committing segment: {} was not uploaded to deep store"
* "Found {} segments with at least one replica in ERROR state"
* "Segment: {} in table: {} is COMMITTING with all replicas in ERROR state"

#### Error Logs

* "Failed to update committing segments list for table: {}"
* "No alive server found to re-ingest segment: {} in table: {}"

Built with [Mintlify](https://mintlify.com).
