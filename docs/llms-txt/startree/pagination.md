# Source: https://docs.startree.ai/corecapabilities/query_data/advanced_operations/pagination.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Pagination

> Pagination support in StarTree Cloud allows clients to consume query results in smaller chunks instead of fetching the entire result set in a single response.

> **Note:** APIs and configuration knobs may change in future releases.

This is useful when:

* The result set is large and you want to **limit memory usage** on the client.
* An application UI needs **paged navigation** through query results (tables, graphs, drilldowns).
* You want **simpler application logic** for scrolling or pagination instead of manually managing `LIMIT`/`OFFSET` in SQL.

Pagination should be used **through the StarTree Cloud Proxy service only**.

***

## How Pagination Work

A pagination-enabled query follows this lifecycle:

1. A query is executed **once** on the cluster.
2. The **full result set** is stored in a **temporary result store**.
3. The **first page** of results is returned as part of the query response.
4. The client then iterates through the results by calling pagination API with:
   * `offset` (start row)
   * `numRows` (page size)
5. The client can:
   * Move **forward or backward** in the result set.
   * Change page size (`numRows`) between calls.

***

## Result Store

The **Result Store** is responsible for storing query results for pagination-based access.

Supported storage options:

* `memory`
* `file` (local filesystem or deep store such as S3/GCS, depending on configuration)
* `s3`
* `gcs`

> **Important**
>
> * `memory` is **not suitable for production**.
> * `memory` and local filesystem storage do **not** work well with more than one broker, because pagination requests may be routed to brokers that do not hold the result set.

***

## Configuration

### Result Store Configuration

These configurations control where and how query results are stored.

| Configuration                        | Default                   | Description                                                       |
| ------------------------------------ | ------------------------- | ----------------------------------------------------------------- |
| `pinot.broker.pagination.protocol`   | `memory`                  | Protocol to use for storage (`memory`, `file`, `s3`, `gcs`).      |
| `pinot.broker.pagination.temp.dir`   | `/tmp/pinot/query/broker` | Local filesystem directory for temporary files.                   |
| `pinot.broker.pagination.<protocol>` | —                         | Configuration prefix for options required by the chosen protocol. |

#### Example: Local File Storage

```properties  theme={null}
pinot.broker.pagination.protocol=file
pinot.broker.pagination.temp.dir=/tmp/pinot/broker/query
pinot.broker.pagination.file.data.dir=file:///home/pinot/data/query
```

#### Example: File Storage Using S3

```properties  theme={null}
pinot.broker.storage.factory.s3.region=us-west-2
pinot.broker.storage.factory.class.s3=org.apache.pinot.plugin.filesystem.S3PinotFS
pinot.broker.pagination.protocol=file
pinot.broker.pagination.temp.dir=/tmp/pinot/broker/query_results
pinot.broker.pagination.file.data.dir=s3://bucket/dir/query-results/
```

***

## Storage Cleaner

StarTree supports two cleanup mechanisms:

### PaginationCleaner (Time-Based Cleanup)

PaginationCleaner is a periodic job that runs on the controller and deletes query results older than a configured TTL.
It must be able to call all brokers and therefore needs appropriate authentication configuration.

#### Example

```properties  theme={null}
controller.cluster.pagination.cleaner.frequencyPeriod=1h
controller.admin.auth.provider.class=org.apache.pinot.common.auth.UrlAuthProvider
controller.admin.auth.url=file:///var/run/secrets/kubernetes.io/serviceaccount/token
```

### Miscellaneous Settings

These settings control the default page size and expiry behavior for queries.

| Configuration                                           | Default | Description                                                  |
| :------------------------------------------------------ | :------ | :----------------------------------------------------------- |
| `pinot.broker.query.page.size`                          | 10000   | Page size if `numRows` is not specified in API calls.        |
| `pinot.broker.pagination.expiration`                    | 1h      | Time after which a query result will be deleted.             |
| `controller.cluster.pagination.cleaner.frequencyPeriod` | 1h      | Frequency of the periodic task that deletes expired results. |
| `controller.cluster.pagination.cleaner.initialDelay`    | random  | Initial delay before the first run of the cleaner task.      |

### Quota-Based Storage Cleaner

The Quota-Based Storage Cleaner automatically cleans up temporary query result storage when disk usage exceeds a configured limit. This prevents broker nodes from running out of disk due to:

* Long-running queries
* Many concurrent cursor queries
* Large result sets

#### Cleanup Behavior

1. Removes **expired results** first.
2. If storage is still above the target threshold, it cleans additional data based on size.

> **Note:** Configuration for this feature can be updated without restarting the broker.

#### Example Configuration

```properties  theme={null}
{
  "pinot.broker.pagination.file.enableStorageCleaner": "true",
  "pinot.broker.pagination.file.maxStoragePerBrokerMB": "1024",
  "pinot.broker.pagination.file.criticalStorageThresholdPercent": "90",
  "pinot.broker.pagination.file.targetStorageThresholdPercent": "60"
}
```

### Configuration Parameters

| Configuration                                                  | Default | Description                                                               |
| -------------------------------------------------------------- | ------- | ------------------------------------------------------------------------- |
| `pinot.broker.pagination.file.enableStorageCleaner`            | `false` | Enables or disables the storage cleaner.                                  |
| `pinot.broker.pagination.file.maxStoragePerBrokerMB`           | `1024`  | Maximum storage quota for query results per broker (in MB).               |
| `pinot.broker.pagination.file.criticalStorageThresholdPercent` | `90`    | Cleanup is triggered when usage exceeds this percentage of the max quota. |
| `pinot.broker.pagination.file.targetStorageThresholdPercent`   | `60`    | Cleaner attempts to reduce storage to this percentage of the max quota.   |

***

## User APIs

### Submit a Cursor-Enabled Query

**Endpoint**

```text  theme={null}
POST /query/sql
```

**Query Parameters**

* `doPaginate` (boolean): Enables cursor-based pagination when `true`.
* `numRows` (int, optional): Number of rows to return in the first page.

**Example Request**

```bash  theme={null}
curl -H "Content-Type: application/json" -X POST \
  -d '{"sql":"select * from upsertMeetupRsvpLLC limit 10"}' \
  "http://localhost:8099/query/sql?doPaginate=true&numRows=1"
```

**Example Response (truncated)**

```json  theme={null}
{
  "resultTable": {
    "dataSchema": {
      "columnNames": ["event_id", "mtime"],
      "columnDataTypes": ["STRING", "TIMESTAMP"]
    },
    "rows": [
      [
        "event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_3461491536",
        "2023-03-10 22:18:46.394"
      ]
    ]
  },
  "requestId": "1599500010000000000",
  "brokerId": "Broker_dogfood-newer-pinot-broker-0.dogfood-newer-pinot-broker-headless.managed.svc.cluster.local_8099",
  "numRowsResultSet": 10,
  "offset": 0,
  "nextOffsetParams": "offset=1&numRows=1",
  "numRows": 1,
  "exceptions": []
}
```

***

### Iterate Over Results

**Endpoint**

```text  theme={null}
GET /query/{requestId}/results
```

**Query Parameters**

* `offset` (int, required): Start offset of the page.
* `numRows` (int, optional): Number of rows in this page. Defaults to `pinot.broker.query.page.size`.

**Example Request**

```bash  theme={null}
curl -X GET \
  "http://localhost:8099/query/1599500010000000000/results?offset=1&numRows=1"
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer <redacted>" \\
  -H "FORWARD_HOST: <broker.host.name>" \\
  -H "FORWARD_PORT: 8099"
```

**Example Response (truncated)**

```json  theme={null}
{
  "resultTable": {
    "dataSchema": {
      "columnNames": ["event_id", "mtime"],
      "columnDataTypes": ["STRING", "TIMESTAMP"]
    },
    "rows": [
      [
        "event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_event_id_3458370505",
        "2023-03-11 01:57:26.394"
      ]
    ]
  },
  "requestId": "1599500010000000000",
  "brokerId": "Broker_dogfood-newer-pinot-broker-0.dogfood-newer-pinot-broker-headless.managed.svc.cluster.local_8099",
  "numRowsResultSet": 10,
  "offset": 1,
  "nextOffsetParams": "offset=2&numRows=1",
  "numRows": 1,
  "exceptions": []
}
```

**Cursor Fields**

* `requestId`: Unique ID for the query
* `offset`: First record in current response
* `numRows`: Number of rows in this page
* `nextOffsetParams`: Pre-filled query parameters for the next page

***

### Iterate Over Results for Local Filesystem

When using the broker's local filesystem as the result store, the StarTree Cloud Proxy must route calls to the correct broker.

Each response includes:

* `brokerHost`
* `brokerPort`

These must be included as request headers in subsequent pagination calls:

**Initial Query Request**

```bash  theme={null}
curl -H "Content-Type: application/json" -X POST \
  -d '{"sql":"select * from upsertMeetupRsvpLLC limit 10"}' \
  "http://<proxy>/query/sql?doPaginate=true&numRows=1"
```

**Example Response Fragment**

```json  theme={null}
{
  "brokerHost": "broker.host.name",
  "brokerPort": 8443
}
```

**Subsequent Pagination Request**

```bash  theme={null}
curl -X GET "http://<proxy>/query/1599500010000000000/results?offset=1&numRows=1"
    -H "Content-Type: application/json" \\
    -H "Authorization: Bearer <redacted>" \\
    -H "FORWARD_HOST: <broker.host.name>" \\
    -H "FORWARD_PORT: 8443"
```

***

### Retrieve Query Metadata

**Endpoint**

```text  theme={null}
GET /query/{requestId}/metadata
```

**Example Request**

```bash  theme={null}
curl -H "Content-Type: application/json" -X GET \
  "http://localhost:8099/query/1599500010000000000/metadata"
```

**Example Response (truncated)**
This returns the broker response metadata for the query, such as:

```json  theme={null}
[
  {
    "requestId": "1599500010000000000",
    "brokerId": "Broker_dogfood-newer-pinot-broker-0.dogfood-newer-pinot-broker-headless.managed.svc.cluster.local_8099",
    "exceptions": [],
    "numServersQueried": 1,
    "numServersResponded": 1,
    "numSegmentsQueried": 24,
    "numSegmentsProcessed": 22,
    "numSegmentsMatched": 2,
    "numConsumingSegmentsQueried": 2,
    "numConsumingSegmentsProcessed": 2,
    "numConsumingSegmentsMatched": 0,
    "numDocsScanned": 20,
    "numEntriesScannedInFilter": 0,
    "numEntriesScannedPostFilter": 40,
    "numGroupsLimitReached": false,
    "maxRowsInJoinReached": false,
    "totalDocs": 10030562,
    "timeUsedMs": 416,
    "offlineThreadCpuTimeNs": 0,
    "realtimeThreadCpuTimeNs": 0,
    "offlineSystemActivitiesCpuTimeNs": 0,
    "realtimeSystemActivitiesCpuTimeNs": 0,
    "offlineResponseSerializationCpuTimeNs": 0,
    "realtimeResponseSerializationCpuTimeNs": 0,
    "offlineTotalCpuTimeNs": 0,
    "realtimeTotalCpuTimeNs": 0,
    "brokerReduceTimeMs": 12,
    "segmentStatistics": [],
    "traceInfo": {},
    "partialResult": false,
    "numRowsResultSet": 0,
    "minConsumingFreshnessTimeMs": 1715864004434,
    "explainPlanNumEmptyFilterSegments": 0,
    "numSegmentsPrunedByServer": 2,
    "numSegmentsPrunedInvalid": 0,
    "numSegmentsPrunedByLimit": 0,
    "numSegmentsPrunedByValue": 0,
    "explainPlanNumMatchAllFilterSegments": 0,
    "numSegmentsPrunedByBroker": 0
  }
]
```

***

## Admin APIs

### List Stored Query Results

**Endpoint**

```text  theme={null}
GET /query/resultStore
```

**Example Request**

```bash  theme={null}
curl -H "Content-Type: application/json" -X GET \
  "http://localhost:8099/query/resultStore/"
```

**Example Response (truncated)**

```json  theme={null}
{
  "resultMetadataList": [
    {
      "requestId": "1599500010000000000",
      "brokerId": "Broker.local_8099",
      "submissionTimeMs": 1715864073212,
      "expirationTimeMs": 1715864076812,
      "responseMetadata": [
        {
          "type": "fs",
          "numRows": 10,
          "dataFile": "s3://.../query-results//1599500010000000000/resultTable_0.json",
          "metadataFile": "s3://.../query-results//1599500010000000000/response_0.json"
        }
      ]
    }
  ]
}
```

***

### Delete Query Results

**Endpoint**

```text  theme={null}
DELETE /query/resultStore/{requestId}
```

**Example Request**

```bash  theme={null}
curl -H "Content-Type: application/json" -X DELETE \
  "http://localhost:8099/query/resultStore/1599500010000000000"
```

**Example Response**

```text  theme={null}
Query Results for 1599500010000000000 deleted.
```

Built with [Mintlify](https://mintlify.com).
