# Source: https://docs.startree.ai/corecapabilities/manage-data/purge-task.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Segment Purge Task

> Selectively remove records from StarTree Pinot analytics tables using powerful Segment Purge Task strategies and Dry Run mode.

## Overview

As organizations face increasing data governance requirements, compliance mandates, and the need for precise data management, the Segment Purge Task in StarTree Pinot provides a powerful solution for selectively removing records from your analytics tables. The task enables fine-grained data deletion based on time windows, dimension predicates, or external input files, helping organizations meet regulatory requirements and maintain data quality without resorting to expensive full table reprocessing.

## Key Capabilities

### 1. Flexible Delete Strategies

The Segment Purge Task supports two primary strategies for identifying records to remove:

* **Input File Strategy:** Delete records matching keys from external input files (e.g., CSV files containing user IDs or transaction IDs to delete)
* **Predicate Strategy:** Delete records matching time windows and/or dimension predicates (e.g., delete all records where status = 'inactive' and timestamp \< '2024-01-01')

### 2. Multiple Selection Modes

When using the Predicate strategy, you can filter segments and records in multiple ways:

* **TIME Mode:** Delete records within a specific time window
* **DIMENSION Mode:** Delete records matching dimension field predicates
* **TIME\_DIMENSION Mode:** Delete records matching both time window and dimension predicates

### 3. Advanced Filtering Capabilities

* **Comparison Operators:** Supports `==` (equal), `!=` (not equal), `<` (less than), `<=` (less than or equal), `>` (greater than), `>=` (greater than or equal)
* **Logical Operators:** Supports && (AND) and || (OR) for combining multiple field conditions

### 4. Support for Regular and Upsert Tables

* **Regular Tables:** Physically removes records from segments
* **Upsert Tables:** Marks records as deleted (soft delete) using the configured delete column. The compaction task subsequently cleans these deleted records.

### 5. Incremental Processing

The task maintains processing state in Zookeeper metadata, enabling incremental processing of large datasets and efficient handling of ongoing purge operations.

## Dry-Run Mode

Dry Run mode lets you preview exactly what a Segment Purge Task would do, without creating tasks or modifying data. It runs the same validation, segment selection, and planning logic with the current watermark metadata for the task, but stops before execution. This provides a safe way to view which segments would be deleted, allowing you to fine-tune the scope before consuming compute resources.

### How to run the Purge Task in Dry-Run mode?

Use the below mentioned API to run the Purge Task in dry-run mode.

`POST /tasks/SegmentPurgeTask/<table-name-with-type>/dryRun`

Auth: Authorization: Bearer `<token>`
Query Parameter: verbose (optional, default: false) - When set to true, includes detailed per-segment information
Body: `<JSON map of task configs>`

#### Sample Request

```bash  theme={null}
curl -sS -X POST 'https://abc.xyz.startree.cloud/tasks/SegmentPurgeTask/myTable_OFFLINE/dryRun?verbose=true' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'content-type: application/json' \
  -d '{
    "purge.start.time.ms": "1609459200000",
    "purge.end.time.ms": "1640995200000",
    "purge.time.column": "timestamp"
  }'
```

#### Sample Response (`verbose=true`)

Once the Segment Purge Task is run in Dry Run mode, what you will get is a response similar to the following JSON:

```json  theme={null}
{
  "mode": "dry-run",
  "table": "myTable_OFFLINE",
  "summary": {
    "purgeCount": 2,
    "deleteCount": 1,
    "purgePercent": 10.0,
    "deletePercent": 5.0,
    "purgeTaskCount": 2,
    "totalTaskCount": 2,
    "totalIterationRequired": 1,
    "maxSubtasksPerIteration": 100,
    "warnings": [
      "[WIDE_TIME_WINDOW] Purge window spans a large portion of the table: touched=15.00% (purge=10.00%, delete=5.00%). Consider smaller batches.",
      "[DIMENSION_TOUCHES_MOST_SEGMENTS] DIMENSION selector touches 60.00% of active segments (600/1000). Consider TIME_DIMENSION or narrower predicates to reduce minion work."
    ]
  },
  "segments": [
    {
      "action": "DELETE",
      "segment": "myTable_OFFLINE_2023-09-01_2023-09-02_0",
      "reason": "segment window [2023-09-01T00:00:00Z, 2023-09-02T00:00:00Z) fully inside selection window [2023-09-01T00:00:00Z, 2023-09-10T00:00:00Z)"
    },
    {
      "action": "PURGE",
      "segment": "myTable_OFFLINE_2023-09-02_2023-09-03_0",
      "reason": "time predicate match `timestamp in [2023-09-01T00:00:00Z, 2023-09-10T00:00:00Z)`; segment window [2023-09-02T00:00:00Z, 2023-09-03T00:00:00Z)"
    }
  ],
  "inputFilesProcessing": [
    "s3://bucket/purge-keys/file1.csv",
    "s3://bucket/purge-keys/file2.csv"
  ]
}
```

#### Descriptions of the above response

* A summary with counts of segments to delete and purge, percentages, task counts, iterations, and any warnings.
* More details on each stage of the Purge Task (when verbose=true):
  * **DELETE** – lists segments that would be removed entirely, along with the reason a segment was selected (e.g., fully inside the selection window, or explicitly listed in purge.segment.list).
  * **PURGE** – lists segments that are partially deleted, which would also be rewritten to keep the rest of the records. (e.g., time windows, dimension filters like status='deleted' AND region='EU').
  * **inputFilesProcessing** – lists input files that would be processed (for the Input File strategy only, when verbose=true).

Please note that Dry Run does not generate task IDs, lineage IDs, progress logs, or build/upload URLs. It also does not provide per-segment row counts for deletion (since that requires reading segment data).

## Supported Warning Scenarios

Dry Run applies the same validations as a real run, returning errors for unsupported scenarios such as invalid predicates and time windows. When other tasks are active, it provides warnings with enough detail to help you decide whether to wait or adjust the scope. If selectors are too broad; for example, a DIMENSION filter that impacts more than half of the segments, Dry Run prompts you to refine them.

Importantly, the DELETE choices made in Dry Run always match those of a real run with the same configuration, ensuring consistency. Potential issues are clearly flagged with descriptive warning codes for easier troubleshooting. These warning codes are mentioned below:

| Category         | Code                                   | Description                                                                                                                                                                                                                    |
| :--------------- | :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Task State       | **ACTIVE\_TASKS\_PRESENT**             | Another conflicting task is currently running (SegmentRefreshTask, StartreeAlterTableTask, UpsertCompactionTask, UpsertSnapshotCreationTask, or another SegmentPurgeTask). Only checked for upsert tables with delete enabled. |
| Task State       | **ACTIVE\_TASKS\_UNKNOWN**             | Failed to compute active tasks for the table. Only checked for upsert tables with delete enabled.                                                                                                                              |
| Task State       | **INCOMPLETE\_TASKS**                  | Found incomplete purge tasks. Task generation would be skipped.                                                                                                                                                                |
| Selection Issues | **NO\_MATCH**                          | Selection matches no active segments. No tasks would be generated.                                                                                                                                                             |
| Selection Issues | **NO\_PURGE\_FILE\_FOUND**             | No eligible input files to process (Input File strategy). Tasks would not be generated.                                                                                                                                        |
| Selection Issues | **VALIDATION\_ERROR**                  | Task configuration validation failed.                                                                                                                                                                                          |
| Selection Issues | **DIMENSION\_TOUCHES\_MOST\_SEGMENTS** | DIMENSION selector impacts ≥50% of segments (purgePercent ≥ 50%).                                                                                                                                                              |
| Selection Issues | **WIDE\_TIME\_WINDOW**                 | Time selector covers ≥50% of segments (touchedPercent ≥ 50%).                                                                                                                                                                  |
| Selection Issues | **MOSTLY\_PARTIAL\_OVERLAP**           | ≥80% partial overlaps (purgeRatio ≥ 0.8). This is CPU/IO intensive on minions.                                                                                                                                                 |
| Selection Issues | **TIME\_WINDOW\_LARGE**                | Time window ≥30 days on large tables (≥10k segments).                                                                                                                                                                          |
| Selection Issues | **DIMENSION\_SCANS\_ALL**              | DIMENSION selector scans all segments (applied to very large tables ≥10k segments).                                                                                                                                            |

### How to run the Purge task in StarTree cloud?

You can run Purge Task either by using /execute API or /schedule API.

#### Using /schedule API

Add the Segment Purge Task config in the table configuration and use the /schedule API to run the Purge task. Sample for segment purge task config is mentioned in each section of the Purge Strategies.

##### Sample Request

```bash  theme={null}
curl 'https://pinot.abc.xyz.startree.cloud/tasks/schedule?taskType=SegmentPurgeTask&tableName=anshultestcsv_OFFLINE' \
  -X 'POST' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'content-type: application/json'
```

#### Using /execute API

Use the below mentioned API to run the Purge task in StarTree cloud.

##### Sample Request

```bash  theme={null}
curl -X 'POST' \
  'https://pinot.abc.xyz.startree.cloud/tasks/execute' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Database: default' \
  -d '{
   "taskType": "SegmentPurgeTask",
   "tableName": "<TABLE_NAME>",
   "taskId": "<UNIQUE_TASK_NAME>",
   "taskConfigs": {
        "purge.query.predicate": "WHERE country = 'US' AND org_id = 'org_id_1' or product IN ('WEB', 'MOBILE')"
    }
  }'
```

## Purge Strategies

### 1. Input File Strategy

**Purpose:** Remove records based on keys provided in external input files.

#### How it works

* You provide input files (CSV, JSON, etc.) containing purge keys (e.g., user IDs, transaction IDs)
* The task reads these files and builds a set of keys to match against
* For each record in segments, it computes a purge key from the specified fields
* Records with matching purge keys are removed
* Records with null or empty purge keys are skipped for safety

#### Use cases

* GDPR right-to-be-forgotten requests (bulk user deletion)
* Removing specific transactions or records identified in external systems
* Compliance-driven bulk deletions from external audit files

#### Sample Task Configuration

Here is a detailed reference table for the Segment Purge Task Configuration Parameters in StarTree Pinot. This table explains each parameter, its purpose, accepted values, and examples to help guide correct usage.

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "inputDirURI": "s3://my-bucket/purge-keys/",
        "inputFormat": "CSV",
        "input.fs.className": "org.apache.pinot.plugin.filesystem.S3PinotFS",
        "input.fs.prop.accessKey": "MY_ACCESS_KEY",
        "input.fs.prop.secretKey": "MY_SECRET_KEY",
        "input.fs.prop.region": "us-west-2",
        "max.num.purge.input.files": 10,
        "max.total.purge.input.file.size": 100000000
      }
    }
  }
}
```

| Parameter                       | Description                                          | Accepted Values / Format                         | Example                                        |
| :------------------------------ | :--------------------------------------------------- | :----------------------------------------------- | :--------------------------------------------- |
| inputDirURI                     | URI of directory containing purge key input files    | File system URI (e.g., s3://, hdfs\://, file://) | `"inputDirURI": "s3://bucket/purge-keys/"`     |
| inputFormat                     | Format of the input files                            | One of: CSV, JSON, AVRO, PARQUET, etc.           | `"inputFormat": "CSV"`                         |
| max.num.purge.input.files       | Maximum number of input files to process per cycle   | Positive integer                                 | `"max.num.purge.input.files": 10`              |
| max.total.purge.input.file.size | Maximum total size of input files in bytes per cycle | Positive integer (bytes)                         | `"max.total.purge.input.file.size": 100000000` |

### 2. Predicate Strategy

**Purpose:** Delete records for both simple and complex predicates. Simple predicates like matching time windows and/or dimension field, and complex predicates where there are multiple different logical operators involved with different fields.

#### Modes

* **QUERY Mode:** Remove all records matching a query predicate like "WHERE country = 'US' AND org\_id = 'org\_id\_1' or product IN ('WEB', 'MOBILE')"
* **TIME Mode:** Remove all records within a specified time range
* **DIMENSION Mode:** Remove records matching dimension field conditions (e.g., status = 'deleted', region = 'EU')
* **TIME\_DIMENSION Mode:** Remove records matching both time and dimension conditions

#### Use cases

* Time-based data retention policies (delete data older than X days)
* Removing records matching specific business conditions
* Cleaning up test or invalid data based on multiple criteria

#### Considerations

When using DIMENSION mode without a time filter, all segments in the table will be scanned, which can be less efficient for large tables. It is recommended to use TIME or TIME\_DIMENSION modes when possible.

Use QUERY mode when you have more than a couple of dimension columns with many different operators and values, which can make the other modes complex.

#### Sample Task Configuration

Here is a detailed reference table for the Segment Purge Task Configuration Parameters in StarTree Pinot. This table explains each parameter, its purpose, accepted values, and examples to help guide correct usage.

### Predicate Strategy: QUERY Mode

<Callout type="info">
  The support for query mode in Segment Purge Task will be available starting StarTree Cloud version 0.14.0
</Callout>

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.query.predicate": "WHERE country = 'US' AND org_id = 'org_id_1' or product IN ('WEB', 'MOBILE')"
      }
    }
  }
}
```

#### Configuration Parameters

| Parameter                | Description                                                                                                       | Accepted Values / Format             | Example                                                                                                   |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------- | :----------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| purge.query.predicate    | Mandatory. A complex Pinot query predicate used to identify rows to purge. Must start with a WHERE clause.        | Predicate starting with WHERE        | `"purge.query.predicate": "WHERE country = 'US' AND org_id = 'org_id_1' or product IN ('WEB', 'MOBILE')"` |
| purge.query.timeout.ms   | Optional. Bounds the query execution time to prevent long-running scans from impacting brokers and other queries. | Time in milliseconds. Default: 60000 | `"purge.query.timeout.ms": "120000"`                                                                      |
| purge.query.max-rows     | Optional. Maximum number of rows fetched per segment.                                                             | Numeric value. Default: 100000       | `"purge.query.max-rows": "100000"`                                                                        |
| purge.query.max-segments | Optional. Maximum number of segments the query result can include.                                                | Numeric value. Default: 30000        | `"purge.query.max-segments": "10000"`                                                                     |

#### Limitations

* JOINs, subqueries, DISTINCT, GROUP BY, HAVING, and aggregation functions or operators are not supported. The task will fail if used.
* Every column referenced in the WHERE clause must exist in the table schema.
* Every column referenced in the WHERE clause must be indexed. Supported indexes include inverted, range, sorted, or a time column configured in the table.

#### Recommendations

**Writing safe and efficient queries:**

* Use selective predicates on indexed columns, such as equality or range filters.
* Avoid wide OR chains or unindexed columns that force full scans.
* If more than 100000 records per segment are expected, increase purge.query.max-rows. If this limit is exceeded, the task fails with the error: "Stopping execution due to reaching max-rows threshold. Increase the limit or narrow the query and retry."
* When testing new predicates, add an explicit LIMIT to validate behavior before running large scans.
* Prefer deterministic filters, such as immutable status values or bounded time ranges, to avoid inconsistent results across runs.

#### Operational Behavior and Guardrails

* If collected rows reach purge.query.max-rows, the task fails to prevent runaway deletions.
* If the segment list reaches purge.query.max-segments, task generation fails before workers are scheduled.

#### Troubleshooting

* **"requires indexed columns"**: Add an index, any one of (inverted, range, sorted, or star-tree) on all columns used in the WHERE clause.
* **"unsupported construct"**: Remove joins, subqueries, DISTINCT, aggregations, GROUP BY, HAVING, or OFFSET clauses.
* **Max rows or segments reached**: Tighten predicates, or increase purge.query.max-rows and purge.query.max-segments only after confirming the cluster can handle the load.
* **Timeouts**: Simplify the predicate, verify broker and server health, or cautiously increase purge.query.timeout.ms.

### Predicate Strategy: TIME Mode

Sample task configuration:

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.start.time.ms": 1609459200000,
        "purge.end.time.ms": 1640995200000,
        "purge.time.column": "timestamp"
      }
    }
  }
}
```

| Parameter           | Description                              | Accepted Values / Format        | Example                                |
| :------------------ | :--------------------------------------- | :------------------------------ | :------------------------------------- |
| purge.start.time.ms | Start of time window for record deletion | Epoch timestamp in milliseconds | `"purge.start.time.ms": 1609459200000` |
| purge.end.time.ms   | End of time window for record deletion   | Epoch timestamp in milliseconds | `"purge.end.time.ms": 1640995200000`   |
| purge.time.column   | Name of the time column to evaluate      | Column name as string           | `"purge.time.column": "timestamp"`     |

### Predicate Strategy: DIMENSION Mode

Sample task configuration:

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.field.names": "status,region",
        "purge.field.values": "deleted,EU",
        "purge.comparison.operator": "==",
        "purge.logical.operator": "&&"
      }
    }
  }
}
```

| Parameter                 | Description                                                                 | Accepted Values / Format                          | Example                                  |         |                                  |
| :------------------------ | :-------------------------------------------------------------------------- | :------------------------------------------------ | :--------------------------------------- | ------- | -------------------------------- |
| purge.field.names         | Comma-separated field names to match                                        | Comma-separated list of field names               | `"purge.field.names": "userId,status"`   |         |                                  |
| purge.field.values        | Corresponding values for fields listed in field.names; matches positionally | Comma-separated list (same length as field.names) | `"purge.field.values": "12345,inactive"` |         |                                  |
| purge.comparison.operator | Comparison operator to use when evaluating field conditions                 | One of: `==`, `!=`, `<`, `<=`, `>`, `>=`          | `"purge.comparison.operator": "=="`      |         |                                  |
| purge.logical.operator    | Logical operator to combine multiple field conditions                       | `&&` (AND) or \`                                  |                                          | \` (OR) | `"purge.logical.operator": "&&"` |

### Predicate Strategy: TIME\_DIMENSION Mode

Combine all configuration keys from the TIME mode and the DIMENSION mode described above. Sample task configuration:

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.start.time.ms": 1609459200000,
        "purge.end.time.ms": 1640995200000,
        "purge.time.column": "timestamp",
        "purge.field.names": "status",
        "purge.field.values": "inactive",
        "purge.comparison.operator": "=="
      }
    }
  }
}
```

### Common Configuration

| Parameter           | Description                                   | Accepted Values / Format | Example                      |
| :------------------ | :-------------------------------------------- | :----------------------- | :--------------------------- |
| table.max.num.tasks | Maximum number of tasks to generate per table | Positive integer         | `"table.max.num.tasks": 100` |

## Key Use Case Scenarios

The Segment Purge Task supports a wide range of data deletion scenarios within Pinot tables. These use cases provide granular control over data removal, helping maintain compliance and data quality.

Below are the core supported scenarios:

### 1. Delete Based on Complex Predicates

Use query mode for filtering and deleting records based on complex predicates.

**Example Use Case:**

Implement a policy to delete all records older than 90 days for organisations "org\_id\_1" and country is US for WEB and MOBILE products.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.query.predicate": "WHERE \"timestamp\" <= 1761644708000 AND country = 'US' AND org_id = 'org_id_1' or product IN ('WEB', 'MOBILE')",
        "purge.query.timeout.ms": "120000",
        "purge.query.max-rows": "100000",
        "purge.query.max-segments": "10000"
      }
    }
  }
}
```

### 2. Delete Records Based on Dimension Filters

Remove records matching specific dimension field conditions.

**Example Use Case 1: Single Field Condition**

Delete all records where status equals 'deleted'.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.field.names": "status",
        "purge.field.values": "deleted",
        "purge.comparison.operator": "=="
      }
    }
  }
}
```

**Example Use Case 2: Multiple Field Conditions (AND)**

Delete records where status equals 'inactive' AND region equals 'EU'.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.field.names": "status,region",
        "purge.field.values": "inactive,EU",
        "purge.comparison.operator": "==",
        "purge.logical.operator": "&&"
      }
    }
  }
}
```

**Example Use Case 3: Multiple Field Conditions (OR)**

Delete records where currency equals 'EUR' OR currency equals 'GBP'.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.field.names": "currency,currency",
        "purge.field.values": "EUR,GBP",
        "purge.comparison.operator": "==",
        "purge.logical.operator": "||"
      }
    }
  }
}
```

**Example Use Case 4: Not Equal Condition**

Delete all records where status is not equal to 'active'.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.field.names": "status",
        "purge.field.values": "active",
        "purge.comparison.operator": "!="
      }
    }
  }
}
```

### 3. Delete Records Using Input File Keys

Remove records based on keys provided in external input files.

**Example Use Case:**

A user receives a GDPR right-to-be-forgotten request with a list of user IDs that need to be deleted from the system.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "inputDirURI": "s3://compliance-bucket/gdpr-requests/2024-01-15/",
        "inputFormat": "CSV",
        "input.fs.className": "org.apache.pinot.plugin.filesystem.S3PinotFS",
        "input.fs.prop.accessKey": "MY_ACCESS_KEY",
        "input.fs.prop.secretKey": "MY_SECRET_KEY",
        "input.fs.prop.region": "us-west-2"
      }
    }
  }
}
```

### 4. Delete Entire Segments

Remove complete segments by explicitly listing segment names.

**Example Use Case:**

A user wants to delete specific segments that are known to contain corrupted or invalid data.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.segment.list": "segment_2024_01_15,segment_2024_01_16"
      }
    }
  }
}
```

### 5. GDPR/Compliance Data Removal

Combine time and dimension filters to remove records for compliance purposes.

**Example Use Case:**

Delete all records for EU region users that are older than 3 years to comply with GDPR data retention requirements.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.start.time.ms": "<three_years_ago_timestamp>",
        "purge.end.time.ms": "<current_timestamp>",
        "purge.time.column": "timestamp",
        "purge.field.names": "region",
        "purge.field.values": "EU",
        "purge.comparison.operator": "=="
      }
    }
  }
}
```

### 6. Time-Based Data Retention Policies

Automatically remove old data based on age criteria.

**Example Use Case:**

Implement a policy to delete all transaction records older than 90 days to maintain optimal query performance and reduce storage costs.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.start.time.ms": "<ninety_days_ago_timestamp>",
        "purge.end.time.ms": "<current_timestamp>",
        "purge.time.column": "transaction_timestamp"
      }
    }
  }
}
```

### 7. Delete Records Based on Time Range

Remove all records within a specific time window.

**Example Use Case:**

A user wants to implement a data retention policy that deletes all records older than 2 years to comply with storage optimization requirements.

**Configuration Sample:**

```json  theme={null}
{
  "task": {
    "taskTypeConfigsMap": {
      "SegmentPurgeTask": {
        "purge.start.time.ms": "<start_timestamp_ms>",
        "purge.end.time.ms": "<end_timestamp_ms>",
        "purge.time.column": "timestamp"
      }
    }
  }
}
```

## How Does it Work?

The Segment Purge Task operates through a two-phase process that ensures data integrity and efficient processing:

### 1. Task Generation (Controller)

The Pinot Controller generates purge tasks based on your configuration:

* Reads processing state from Zookeeper metadata for incremental processing
* Selects eligible segments based on the configured purge strategy
* Generates individual PinotTaskConfig instances for each segment that needs processing
* Updates Zookeeper metadata to track processing progress

### 2. Task Execution (Minion)

Minion workers execute the purge operations:

* Download the segment that needs to be processed
* Build a RecordProcessor based on the configured strategy (Input File or Predicate)
* Process each record, applying the purge criteria to determine which records should be removed
* Create a new segment containing only the records that should be retained
* Upload the new segment using the same segment name, effectively replacing the original segment at the segment level

## FAQs & Recommendations

### 1. What is the most efficient way to run the Segment Purge Task?

The most efficient approach is to use TIME or TIME\_DIMENSION modes when possible, as they allow the task to efficiently identify which segments need processing based on time partitioning. If no time filter is provided (DIMENSION mode only), all segments in the table will be scanned, which can be less efficient for large tables.

### 2. Is custom dimension partitioning necessary to run the Purge Task efficiently?

No, the data does not need to be physically partitioned by dimensions. The task performs record-level scans within segments. However, having a time column configured and using time-based filters will significantly improve efficiency by limiting which segments need to be processed.

### 3. How does the Purge Task handle upsert tables differently from regular tables?

For regular tables, records are physically removed from segments. For upsert tables, records are marked as deleted (soft delete) using the configured delete column. The delete column must be configured in the table's upsertConfig. The matching records from the CONSUMING segments won't be marked for deletion; in case it is required, do run the Purge Task again to remove all the matching records.

### 4. Can I use the Purge Task to delete records based on multiple conditions?

Yes, you can combine multiple field conditions using a single logical operator (`&&` for AND, `||` for OR) and a single comparison operator (`==`, `!=`, `<`, `<=`, `>`, `>=`) that applies to all specified fields in DIMENSION and TIME\_DIMENSION modes. You can also combine time windows with dimension filters using TIME\_DIMENSION mode. You can use any number of conditions in QUERY mode.

### 5. What happens if I run the Purge Task while other tasks are running on the same table?

The Segment Purge Task cannot run concurrently with SegmentRefreshTask, StartreeAlterTableTask, UpsertCompactionTask, UpsertSnapshotCreationTask, or another Segment Purge Task instance on the same table.

### 6. How does the Input File strategy work with incremental processing?

The Input File strategy maintains state in Zookeeper metadata, tracking which input files have been processed. This allows you to add new files to the input directory over time, and the task will process only the new files in subsequent runs, enabling incremental bulk deletions.

### 7. Can I preview what will be deleted before running the task?

Yes, the Segment Purge Task supports a dry-run mode that provides a preview of what will be affected. Use the `POST /tasks/SegmentPurgeTask/{tableNameWithType}/dryRun` API endpoint with your task configuration. The dry-run returns a summary including the number of segments to purge and delete, percentages of affected segments, estimated task counts, and warnings about potential issues. When verbose mode is enabled, it also lists the specific segments that would be affected, along with the reasons for each action. See the "Dry-Run Mode" section above for detailed API documentation and response structure.

### 8. How do I schedule the Purge Task for regular data retention policies?

The task does not support native scheduling within Pinot. You will need to use external orchestration tools (e.g., cron, Airflow, Kubernetes CronJobs) to trigger the task via the controller's execution API on a regular schedule.

### 9. What is the difference between deleting segments and purging records?

Deleting segments removes entire segments from the table (used when all data in a segment should be removed). Purging records removes only specific records within segments while keeping the segment structure intact (used for fine-grained deletion).

Built with [Mintlify](https://mintlify.com).
