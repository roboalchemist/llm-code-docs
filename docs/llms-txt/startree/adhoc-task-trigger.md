# Source: https://docs.startree.ai/corecapabilities/manage-data/recipes/adhoc-task-trigger.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Adhoc Minion Tasks Programmatically

> Learn how to programmatically trigger and manage Pinot Minion tasks using Schedule and Execute APIs.

Pinot provides two primary APIs to programmatically trigger ad hoc Minion tasks. Choosing the right API and strategy depends on your task type, data source characteristics, and runtime requirements.

> **Note:** `Schedule API` uses the task config defined in the table config, whereas `Execute API` relies on the API payload. Other than this, there is no difference between these two APIs.

***

## Schedule API

**API Reference:** [`/tasks/schedule`](/api-reference/task/schedule-tasks-and-return-a-map-from-task-type-to-task-name-scheduled-if-task-type-is-missing-schedules-all-tasks-if-table-name-is-missing-schedules-tasks-for-all-tables-in-the-database-if-database-is-missing-in-headers-uses-default)

**Behavior:**
This API schedules tasks using parameters defined under the table’s task configs. Pinot internally determines eligible segments, generates subtasks accordingly, and executes them **immediately**.

**When to Use:**

* When a scheduled task needs to be run immediately instead of waiting for its next schedule.
* If periodic execution is not required or the task should only be externally triggered (e.g., by Airflow), remove the schedule parameter in the task config.
* Recommended for tasks predefined in table config like:
  * Delta Ingestion Task
  * File Ingestion Task
  * SQL Ingestion Task
  * Segment Backfill Task

**Caveats:**

* Ensure `tableMaxNumTasks = -1` so all sub-tasks are created within a single task.
* No built-in retry/recovery mechanism. Tasks must be re-triggered manually if failures occur.

***

## Execute API

**API Reference:** [`/tasks/execute`](/api-reference/task/execute-a-task-on-minion)

**Behavior:**
Executes a task using runtime-supplied configuration (API payload), giving full control over parameters like input paths, filters, and processing windows.

**When to Use:**

* Tasks that require dynamic parameters (input sources, delta ranges, etc.).
* Ideal for external orchestration (e.g., Airflow) of the following:
  * Delta Ingestion Task
  * File Ingestion Task
  * SQL Ingestion Task
  * Segment Backfill Task

**Caveats:**

* No built-in retry/recovery mechanism. Tasks must be re-triggered manually if failures occur.
* Avoid using this API for scheduled maintenance tasks like Segment Import, Segment Refresh, or Alter Table Tasks (use cron-based schedules instead).

***

## File Ingestion Task

The **File Ingestion Task** is used to ingest data from external sources (e.g., S3, GCS, ADLS).
It operates in two main modes - **Append Mode** and **Sync Mode**. Each mode also supports **Consistent Push Mode** and **Consistent Push Full Swap Mode** for atomic ingestion.

### Mode Overview

| Mode        | Consistent Push | Consistent Push Swap | Behavior                                                      | Segment to File Mapping |
| ----------- | --------------- | -------------------- | ------------------------------------------------------------- | ----------------------- |
| Sync Mode   | false           | false                | No atomicity is guaranteed within the batch                   | 1:1                     |
| Sync Mode   | true            | false                | Atomic batch ingestion, it is used for incremental ingestion. | 1:1                     |
| Sync Mode   | false           | true                 | Full table refresh, atomic per run                            | 1:1                     |
| Append Mode | true            | false                | Atomic batch ingestion, it is used for incremental ingestion. | m:n                     |
| Append Mode | false           | true                 | Full table refresh, atomic per run                            | m:n                     |

***

### Scaling and Stability Recommendations

| Parameter            | Description                       | Recommended Setting                   |
| -------------------- | --------------------------------- | ------------------------------------- |
| `tableMaxNumTasks`   | Max concurrent subtasks per table | 1000 (adjust per controller capacity) |
| `taskMaxDataSize`    | Max data processed per subtask    | 1–2 GB (default: 1 GB)                |
| `taskMaxNumFiles`    | Max files per subtask             | Increase for small-file datasets      |
| `desiredSegmentSize` | Target Pinot segment size         | 500 MB – 1 GB                         |

***

### Recommendations

#### 1. Large Ad-hoc Ingestion (\~2TB, `consistentPushSwapEnabled=false`)

* **Append Mode:** If `taskMaxDataSize = 1GB` and `tableMaxNumTasks = 1000`, a single batch can ingest 1TB. Run twice to complete 2TB ingestion.
* **Sync Mode:** If each file = 400 MB, with `tableMaxNumTasks = 1000`, total = 400 GB per batch → 5 batches required.
* **Tip:** Re-trigger `/tasks/schedule` or `/tasks/execute` in a loop until no subtasks are created. (No ingestion will take place unless there are new files).

#### 2. Full Table Refresh (`consistentPushSwapEnabled=true`)

* Refresh the whole table with new data.
* Ensures atomic ingestion for all or none.
* Atomicity applies only within a single task execution, not across batches.
* Set `tableMaxNumTasks = -1` to generate all subtasks in one batch.

#### 3. Atomic Table Ingestion (`consistentPushEnabled=true`)

* Similar atomic behavior as above; atomic only within one task execution.
* Set `tableMaxNumTasks = -1` to generate all subtasks in one batch.

#### 4. Rerun on Failure

* Use the [Debug API](/api-reference/task/fetch-information-for-the-given-task-name) to verify task status.
* If subtasks show `FAILED` or `TIMED_OUT`, re-trigger with the same config.
* Once all subtasks are `COMPLETED`, reruns have no effect (idempotent).

***

## Delta Ingestion Task

* Generates 1:1 mapping of Delta files to Pinot segments.
* Safe to rerun; each execution is independent.
* Supports both Schedule and Execute ad hoc APIs.

**Rerun Recommendation:**

* Check via [Debug API](/api-reference/task/fetch-information-for-the-given-task-name).
* If subtasks show `FAILED` or `TIMED_OUT`, re-trigger.
* Once all are `COMPLETED`, rerun has no effect.

***

## Segment Backfill Task

* Executable only on-demand (cannot be scheduled).
* Does **not** support the `schedule` parameter in task config.
* Avoid re-triggering successful runs — repeated runs will re-ingest the same data.

**Rerun Recommendation:**

* Check via [Debug API](/api-reference/task/fetch-information-for-the-given-task-name).
* If subtasks show `FAILED` or `TIMED_OUT`, re-trigger.
* Once all are `COMPLETED`, rerun has no effect.

***

## Segment Import Task

* Recommended frequency: **every 15 minutes**.
* Should be scheduled via the `schedule` parameter in task config.
* It is **not** recommended to trigger using ad hoc schedule or execute APIs.

***

## Segment Refresh Task / Alter Table Task

* Recommended frequency: **every 15 minutes**.
* Should be scheduled via the `schedule` parameter in task config.
* It is **not** recommended to trigger using ad hoc schedule or execute APIs.
* Use the **[Progress Tracker API](/api-reference/altertable/get-progress-and-estimated-completion-time-for-the-task)** to monitor execution status for Alter Table Task.

Built with [Mintlify](https://mintlify.com).
