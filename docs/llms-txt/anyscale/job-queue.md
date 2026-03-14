# Source: https://docs.anyscale.com/reference/job-queue.md

# Job Queue API Reference

[View Markdown](/reference/job-queue.md)

# Job Queue API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Job Queue CLI[​](#job-queue-cli "Direct link to Job Queue CLI")

### `anyscale job-queue list`[​](#anyscale-job-queue-list "Direct link to anyscale-job-queue-list")

**Usage**

`anyscale job-queue list [OPTIONS]`

List job queues.

**Options**

* **`--id`**: ID of a job queue.
* **`--name`**: Filter by name.
* **`--cloud`**: Filter by cloud.
* **`--project`**: Filter by project.
* **`--include-all-users/--only-mine`**: Include job queues not created by current user.
* **`--cluster-status`**: Filter by cluster status.
* **`--tag`**: This option can be repeated to filter by multiple tags. Tags with the same key are ORed, whereas tags with different keys are ANDed. Example: --tag team
  <!-- -->
  :mlops
  <!-- -->
  \--tag team
  <!-- -->
  :infra
  <!-- -->
  \--tag env
  <!-- -->
  :prod
  <!-- -->
  . Filters with team: (mlops OR infra) AND env
  <!-- -->
  :prod
  <!-- -->
  .
* **`--view`**: Columns view.
* **`--page-size`**: Items per page (max 50).
* **`--max-items`**: Non-interactive max items.
* **`--sort`**: Sort by FIELD (prefix with '-' for desc). Repeatable.
* **`--interactive/--no-interactive`**: Enable interactive pagination.
* **`-j/--json`**: JSON output.
* **`--include-archived`**: Include archived job queues when searching by name. Ignored when using --id.

#### Examples[​](#examples "Direct link to Examples")

* CLI

```
$ anyscale job-queue list
Output
JOB QUEUES:
             ID                 NAME              CLUSTER ID                      CREATOR ID             MAX CONCURRENCY    IDLE TIMEOUT SEC    CURRENT CLUSTER STATE
jq_h8fcze2qkr8wttuuvapi1hvyuc  queue_3  ses_cjr7uaf1yh2ue5uzvd11p24p4u  usr_we8x7d7u8hq8mj2488ed9x47n6          3                 5000               Terminated
jq_v5bx9z1sd4pbxasxhdms37j4gi  queue_2  ses_k86raeu6k1t6z1bvyejn3vblad  usr_we8x7d7u8hq8mj2488ed9x47n6         10                 5000               Terminated
jq_ni6hk66nt3194msr7hzzj9daun  queue_1  ses_uhb8a9gamtarz68kcurpjh86sa  usr_we8x7d7u8hq8mj2488ed9x47n6         10                 5000               Terminated
```

### `anyscale job-queue update`[​](#anyscale-job-queue-update "Direct link to anyscale-job-queue-update")

**Usage**

`anyscale job-queue update [OPTIONS]`

Update job queue settings.

**Options**

* **`--id`**: ID of the job queue.
* **`--name/-n`**: Name of the job queue.
* **`--project/-p`**: Project name (required when using --name).
* **`--cloud`**: Cloud name (required when using --name).
* **`--max-concurrency`**: Max number of concurrent jobs.
* **`--idle-timeout-s`**: Idle timeout in seconds.
* **`--json`**: JSON output.

#### Examples[​](#examples-1 "Direct link to Examples")

* CLI

```
$ anyscale job-queue update --id jq_h8fcze2qkr8wttuuvapi1hvyuc --max-concurrency 5
Output
ID                            : jq_h8fcze2qkr8wttuuvapi1hvyuc
USER PROVIDED ID              : queue_3
NAME                          : queue_3
CURRENT JOB QUEUE STATE       : ACTIVE
EXECUTION MODE                : PRIORITY
MAX CONCURRENCY               : 5
IDLE TIMEOUT SEC              : 5000
CREATED AT                    : 2025-04-15 20:40:44
CREATOR ID                    : usr_we8x7d7u8hq8mj2488ed9x47n6
CREATOR EMAIL                 : test@anyscale.com
COMPUTE CONFIG ID             : cpt_8hzsv1t4jvb6kwjhfqbfjw5i6b
CURRENT CLUSTER STATE         : Terminated
CLUSTER ID                    : ses_cjr7uaf1yh2ue5uzvd11p24p4u
PROJECT ID                    : prj_7FWKGPGPaD3Q5mvk9zK2viBD
CLOUD ID                      : cld_kvedZWag2qA8i5BjxUevf5i7
TOTAL JOBS                    : 6
SUCCESSFUL JOBS               : 6
FAILED JOBS                   : 0
ACTIVE JOBS                   : 0
```

### `anyscale job-queue status`[​](#anyscale-job-queue-status "Direct link to anyscale-job-queue-status")

**Usage**

`anyscale job-queue status [OPTIONS]`

Show job queue details.

**Options**

* **`--id`**: ID of the job queue.
* **`--name/-n`**: Name of the job queue.
* **`--project/-p`**: Project name to filter by when using --name.
* **`--cloud`**: Cloud name to filter by when using --name.
* **`--view`**: Columns view.
* **`--json`**: JSON output.
* **`--include-archived`**: Include archived job queues when searching by name. Ignored when using --id.

#### Examples[​](#examples-2 "Direct link to Examples")

* CLI

```
$ anyscale job-queue status --id jq_h8fcze2qkr8wttuuvapi1hvyuc
Output
ID                            : jq_h8fcze2qkr8wttuuvapi1hvyuc
USER PROVIDED ID              : queue_3
NAME                          : queue_3
CURRENT JOB QUEUE STATE       : ACTIVE
EXECUTION MODE                : PRIORITY
MAX CONCURRENCY               : 3
IDLE TIMEOUT SEC              : 5000
CREATED AT                    : 2025-04-15 20:40:44
CREATOR ID                    : usr_we8x7d7u8hq8mj2488ed9x47n6
CREATOR EMAIL                 : test@anyscale.com
COMPUTE CONFIG ID             : cpt_8hzsv1t4jvb6kwjhfqbfjw5i6b
CURRENT CLUSTER STATE         : Terminated
CLUSTER ID                    : ses_cjr7uaf1yh2ue5uzvd11p24p4u
PROJECT ID                    : prj_7FWKGPGPaD3Q5mvk9zK2viBD
CLOUD ID                      : cld_kvedZWag2qA8i5BjxUevf5i7
TOTAL JOBS                    : 6
SUCCESSFUL JOBS               : 6
FAILED JOBS                   : 0
ACTIVE JOBS                   : 0
```

### `anyscale job-queue archive`[​](#anyscale-job-queue-archive "Direct link to anyscale-job-queue-archive")

**Usage**

`anyscale job-queue archive [OPTIONS]`

Archive (seal) a job queue. No new jobs can be submitted.

**Options**

* **`--id`**: ID of the job queue.
* **`--name/-n`**: Name of the job queue.
* **`--project`**: Project name (required with --name).
* **`--cloud`**: Cloud name (required with --name).

#### Examples[​](#examples-3 "Direct link to Examples")

* CLI

```
$ anyscale job-queue archive --id jq_abc123
Archiving job queue 'jq_abc123'...
Job queue 'jq_abc123' has been archived.
Query the status with `anyscale job-queue status --id jq_abc123`.

$ anyscale job-queue archive --name my-queue --project my-project --cloud my-cloud
Archiving job queue 'my-queue'...
Job queue 'my-queue' has been archived.
Query the status with `anyscale job-queue status --id jq_abc123`.
```

### `anyscale job-queue terminate`[​](#anyscale-job-queue-terminate "Direct link to anyscale-job-queue-terminate")

**Usage**

`anyscale job-queue terminate [OPTIONS]`

Terminate a job queue and all its pending/running jobs.

**Options**

* **`--id`**: ID of the job queue.
* **`--name/-n`**: Name of the job queue.
* **`--project`**: Project name (required with --name).
* **`--cloud`**: Cloud name (required with --name).
* **`--include-archived`**: Include archived job queues when searching by name. Ignored when using --id.

#### Examples[​](#examples-4 "Direct link to Examples")

* CLI

```
$ anyscale job-queue terminate --id jq_abc123
Terminating job queue 'jq_abc123'...
Job queue 'jq_abc123' has been marked for termination.
Query the status with `anyscale job-queue status --id jq_abc123`.

$ anyscale job-queue terminate --name my-queue --project my-project --cloud my-cloud
Terminating job queue 'my-queue'...
Job queue 'my-queue' has been marked for termination.
Query the status with `anyscale job-queue status --id jq_abc123`.
```

### `anyscale job-queue delete`[​](#anyscale-job-queue-delete "Direct link to anyscale-job-queue-delete")

**Usage**

`anyscale job-queue delete [OPTIONS]`

Delete a job queue. Jobs previously submitted remain accessible.

**Options**

* **`--id`**: ID of the job queue.
* **`--name/-n`**: Name of the job queue.
* **`--project`**: Project name (required with --name).
* **`--cloud`**: Cloud name (required with --name).
* **`--include-archived`**: Include archived job queues when searching by name. Ignored when using --id.

#### Examples[​](#examples-5 "Direct link to Examples")

* CLI

```
$ anyscale job-queue delete --id jq_abc123
Deleting job queue 'jq_abc123'...
Job queue 'jq_abc123' has been deleted.

$ anyscale job-queue delete --name my-queue --project my-project --cloud my-cloud
Deleting job queue 'my-queue'...
Job queue 'my-queue' has been deleted.
```

### `anyscale job-queue tags add`[​](#anyscale-job-queue-tags-add "Direct link to anyscale-job-queue-tags-add")

**Usage**

`anyscale job-queue tags add [OPTIONS]`

Add or update tags on a job queue.

**Options**

* **`--id`**: ID of a job queue.
* **`--name/-n`**: Name of a job queue.
* **`--tag`**: Tag in key=value (or key
  <!-- -->
  :value
  <!-- -->
  ) format. Repeat to add multiple.

#### Examples[​](#examples-6 "Direct link to Examples")

* CLI

```
$ anyscale job-queue tags add --name my-queue --tag team=data --tag priority=high
```

### `anyscale job-queue tags remove`[​](#anyscale-job-queue-tags-remove "Direct link to anyscale-job-queue-tags-remove")

**Usage**

`anyscale job-queue tags remove [OPTIONS]`

Remove tags by key from a job queue.

**Options**

* **`--id`**: ID of a job queue.
* **`--name/-n`**: Name of a job queue.
* **`--key`**: Tag key to remove. Repeatable.

#### Examples[​](#examples-7 "Direct link to Examples")

* CLI

```
$ anyscale job-queue tags remove --name my-queue --key team --key priority
```

### `anyscale job-queue tags list`[​](#anyscale-job-queue-tags-list "Direct link to anyscale-job-queue-tags-list")

**Usage**

`anyscale job-queue tags list [OPTIONS]`

List tags for a job queue.

**Options**

* **`--id`**: ID of a job queue.
* **`--name/-n`**: Name of a job queue.
* **`--json`**: JSON output.

#### Examples[​](#examples-8 "Direct link to Examples")

* CLI

```
$ anyscale job-queue tags list --name my-queue --json
```

## Job Queue SDK[​](#job-queue-sdk "Direct link to Job Queue SDK")

### `anyscale.job_queue.list`[​](#anyscalejob_queuelist "Direct link to anyscalejob_queuelist")

List job queues or fetch a single job queue by ID.

**Arguments**

* **`job_queue_id` (str | None) = None**: If provided, fetches only the job queue with this ID.
* **`name` (str | None) = None**: Filter by job queue name.
* **`creator_id` (str | None) = None**: Filter by the user ID of the creator.
* **`cloud` (str | None) = None**: Filter by cloud name.
* **`project` (str | None) = None**: Filter by project name.
* **`cluster_status` (str | None) = None**: Filter by the state of the associated cluster.
* **`tags_filter` (Dict\[str, List\[str]] | None) = None**: Filter by tags. Accepts dict\[key] -> List\[values] or list\['key
  <!-- -->
  :value
  <!-- -->
  '] entries.
* **`page_size` (int | None) = None**: Number of items per API request page.
* **`max_items` (int | None) = None**: Maximum total number of items to return.
* **`sorting_directives` (List\[str] | None) = None**: List of directives to sort the results.
* **`include_archived` (bool) = False**: If True, include archived job queues in the search. Ignored when using job\_queue\_id.

**Returns**: ResultIterator\[[JobQueueStatus](/reference/job-queue.md#jobqueuestatus)]

#### Examples[​](#examples-9 "Direct link to Examples")

* Python

```
import anyscale

# Example: List the first 50 job queues
for jq in anyscale.job_queue.list(max_items=50):
    print(jq.id, jq.name, jq.state)
```

### `anyscale.job_queue.status`[​](#anyscalejob_queuestatus "Direct link to anyscalejob_queuestatus")

Get the status and details for a specific job queue.

**Arguments**

* **`job_queue_id` (str | None) = None**: The unique ID of the job queue.
* **`name` (str | None) = None**: The name of the job queue (alternative to job\_queue\_id).
* **`project` (str | None) = None**: The project name to filter by when using name.
* **`cloud` (str | None) = None**: The cloud name to filter by when using name.
* **`include_archived` (bool) = False**: If True, include archived job queues when searching by name. Ignored when using job\_queue\_id.

**Returns**: [JobQueueStatus](/reference/job-queue.md#jobqueuestatus)

#### Examples[​](#examples-10 "Direct link to Examples")

* Python

```
import anyscale

# Get status by ID
status = anyscale.job_queue.status(job_queue_id="jobq_abc123")
print(status)

# Get status by name
status = anyscale.job_queue.status(name="my-queue")
print(status)
```

### `anyscale.job_queue.update`[​](#anyscalejob_queueupdate "Direct link to anyscalejob_queueupdate")

Update a job queue.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to update.
* **`job_queue_name` (str | None) = None**: Name of the job queue to update (alternative to ID).
* **`project` (str | None) = None**: Project name (required when using job\_queue\_name).
* **`cloud` (str | None) = None**: Cloud name (required when using job\_queue\_name).
* **`max_concurrency` (int | None) = None**: New maximum concurrency value.
* **`idle_timeout_s` (int | None) = None**: New idle timeout in seconds.

**Returns**: [JobQueueStatus](/reference/job-queue.md#jobqueuestatus)

#### Examples[​](#examples-11 "Direct link to Examples")

* Python

```
import anyscale

updated_jq = anyscale.job_queue.update(job_queue_id="jobq_abc123", max_concurrency=5)
print(updated_jq)
```

### `anyscale.job_queue.archive`[​](#anyscalejob_queuearchive "Direct link to anyscalejob_queuearchive")

Archive (seal) a job queue. No new jobs can be submitted.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to archive (alternative to name).
* **`name` (str | None) = None**: Name of the job queue to archive (alternative to ID).
* **`project` (str | None) = None**: Project name (required when using name).
* **`cloud` (str | None) = None**: Cloud name (required when using name).

**Returns**: str

#### Examples[​](#examples-12 "Direct link to Examples")

* Python

```
import anyscale

# Archive by ID
anyscale.job_queue.archive(job_queue_id="jq_abc123")

# Archive by name (requires project and cloud)
anyscale.job_queue.archive(name="my-queue", project="my-project", cloud="my-cloud")
```

### `anyscale.job_queue.terminate`[​](#anyscalejob_queueterminate "Direct link to anyscalejob_queueterminate")

Terminate a job queue and all its pending/running jobs.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to terminate (alternative to name).
* **`name` (str | None) = None**: Name of the job queue to terminate (alternative to ID).
* **`project` (str | None) = None**: Project name (required when using name).
* **`cloud` (str | None) = None**: Cloud name (required when using name).
* **`include_archived` (bool) = False**: If True, include archived job queues when searching by name. Ignored when using job\_queue\_id.

**Returns**: str

#### Examples[​](#examples-13 "Direct link to Examples")

* Python

```
import anyscale

# Terminate by ID
anyscale.job_queue.terminate(job_queue_id="jq_abc123")

# Terminate by name (requires project and cloud)
anyscale.job_queue.terminate(name="my-queue", project="my-project", cloud="my-cloud")
```

### `anyscale.job_queue.delete`[​](#anyscalejob_queuedelete "Direct link to anyscalejob_queuedelete")

Delete a job queue.

Jobs previously submitted to the queue remain accessible. The job queue must have all jobs in terminal state and no running clusters. This action cannot be undone.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to delete (alternative to name).
* **`name` (str | None) = None**: Name of the job queue to delete (alternative to ID).
* **`project` (str | None) = None**: Project name (required when using name).
* **`cloud` (str | None) = None**: Cloud name (required when using name).
* **`include_archived` (bool) = False**: If True, include archived job queues when searching by name. Ignored when using job\_queue\_id.

**Returns**: str

#### Examples[​](#examples-14 "Direct link to Examples")

* Python

```
import anyscale

# Delete by ID
anyscale.job_queue.delete(job_queue_id="jq_abc123")

# Delete by name (requires project and cloud)
anyscale.job_queue.delete(name="my-queue", project="my-project", cloud="my-cloud")
```

### `anyscale.job_queue.add_tags`[​](#anyscalejob_queueadd_tags "Direct link to anyscalejob_queueadd_tags")

Upsert tags for a job queue.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to tag (alternative to name).
* **`name` (str | None) = None**: Name of the job queue to tag (alternative to ID).
* **`tags` (Dict\[str, str])**: Key/value tags to upsert as a map {key: value}.

#### Examples[​](#examples-15 "Direct link to Examples")

* Python

```
import anyscale

anyscale.job_queue.add_tags(job_queue_id="jobq_abc123", tags={"team": "mlops"})
```

### `anyscale.job_queue.remove_tags`[​](#anyscalejob_queueremove_tags "Direct link to anyscalejob_queueremove_tags")

Remove tags by key from a job queue.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to modify (alternative to name).
* **`name` (str | None) = None**: Name of the job queue to modify (alternative to ID).
* **`keys` (List\[str])**: List of tag keys to remove.

#### Examples[​](#examples-16 "Direct link to Examples")

* Python

```
import anyscale

anyscale.job_queue.remove_tags(job_queue_id="jobq_abc123", keys=["team"])
```

### `anyscale.job_queue.list_tags`[​](#anyscalejob_queuelist_tags "Direct link to anyscalejob_queuelist_tags")

List tags for a job queue as a key/value mapping.

**Arguments**

* **`job_queue_id` (str | None) = None**: ID of the job queue to read tags (alternative to name).
* **`name` (str | None) = None**: Name of the job queue to read tags (alternative to ID).

**Returns**: Dict\[str, str]

#### Examples[​](#examples-17 "Direct link to Examples")

* Python

```
import anyscale

tags: dict[str, str] = anyscale.job_queue.list_tags(name="my-queue")
```

## Job Queue Models[​](#job-queue-models "Direct link to Job Queue Models")

### `JobQueueStatus`[​](#jobqueuestatus "Direct link to jobqueuestatus")

Represents the status and details of a Job Queue.

#### Fields[​](#fields "Direct link to Fields")

* **`id` (str)**: Unique ID of the job queue.
* **`state` (str)**: Current state of the job queue.
* **`name` (str | None)**: Name of the job queue.
* **`creator_email` (str | None)**: Email of the user who created the job queue.
* **`project_id` (str | None)**: ID of the project this job queue belongs to.
* **`created_at` (datetime | None)**: Timestamp when the job queue was created.
* **`max_concurrency` (int | None)**: Maximum number of jobs allowed to run concurrently.
* **`idle_timeout_s` (int | None)**: Idle timeout in seconds before the queue's cluster may shut down.
* **`user_provided_id` (str | None)**: User provided identifier of the job queue.
* **`execution_mode` (str | None)**: The execution mode of the job queue.
* **`creator_id` (str | None)**: Identifier of user who created the job queue.
* **`cloud_id` (str | None)**: The cloud ID associated with the job queue.
* **`total_jobs` (int | None)**: Total number of jobs in the job queue.
* **`successful_jobs` (int | None)**: Number of successful jobs in the job queue.
* **`failed_jobs` (int | None)**: Number of failed jobs in the job queue.
* **`active_jobs` (int | None)**: Number of active jobs in the job queue.

#### Python Methods[​](#python-methods "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-18 "Direct link to Examples")

* Python

```
from anyscale.job_queue.models import JobQueueStatus

status = JobQueueStatus(
    id="jq_123",
    state="ACTIVE",
    name="my-queue",
    max_concurrency=5,
    idle_timeout_s=300,
)
```

### `JobQueueState`[​](#jobqueuestate "Direct link to jobqueuestate")

Current state of a job queue.

#### Values[​](#values "Direct link to Values")

* **`ACTIVE`**: The job queue is active and accepting jobs.
* **`SEALED`**: The job queue is sealed and not accepting new jobs. It may still be processing existing jobs.
* **`UNKNOWN`**: The state of the job queue is unknown or could not be determined.

### `ExecutionMode`[​](#executionmode "Direct link to executionmode")

Execution mode of a job queue.

#### Values[​](#values-1 "Direct link to Values")

* **`FIFO`**: FIFO execution mode.
* **`LIFO`**: LIFO execution mode.
* **`PRIORITY`**: Priority-based execution mode.
* **`UNKNOWN`**: Unknown execution mode.

### `ClusterState`[​](#clusterstate "Direct link to clusterstate")

Possible states for a cluster.

#### Values[​](#values-2 "Direct link to Values")

* **`RUNNING`**: The cluster is running.
* **`TERMINATED`**: The cluster is terminated.
* **`PENDING`**: The cluster is pending creation.
* **`UNKNOWN`**: The state of the cluster is unknown.

### `JobQueueSortField`[​](#jobqueuesortfield "Direct link to jobqueuesortfield")

Fields available for sorting job queues.

#### Values[​](#values-3 "Direct link to Values")

* **`ID`**: Sort by Job Queue ID.
* **`NAME`**: Sort by Job Queue name.
* **`CREATED_AT`**: Sort by creation timestamp.
* **`CREATOR_ID`**: Sort by the ID of the creator.
* **`CREATOR_EMAIL`**: Sort by the email of the creator.
* **`PROJECT_ID`**: Sort by the Project ID.
* **`CLOUD_ID`**: Sort by the Cloud ID.
* **`QUEUE_STATE`**: Sort by the Job Queue's state (ACTIVE, SEALED).
* **`CLUSTER_STATE`**: Sort by the state of the associated cluster.

### `JobQueueSortDirective`[​](#jobqueuesortdirective "Direct link to jobqueuesortdirective")

Directive for sorting job queue results.

#### Fields[​](#fields-1 "Direct link to Fields")

* **`sort_field` ([JobQueueSortField](/reference/job-queue.md#jobqueuesortfield) | str)**: The field to sort by.
* **`sort_order` ([SortOrder](/reference/job-queue.md#sortorder) | str)**: The sort order (ASC or DESC).

#### Python Methods[​](#python-methods-1 "Direct link to Python Methods")

```
def to_dict(self) -> Dict[str, Any]
    """Return a dictionary representation of the model."""
```

#### Examples[​](#examples-19 "Direct link to Examples")

* Python

```
from anyscale.job_queue.models import JobQueueSortDirective, JobQueueSortField, SortOrder

# Create a sort directive
sort_directive = JobQueueSortDirective(
    sort_field=JobQueueSortField.CREATED_AT,
    sort_order=SortOrder.DESC
)
```

### `SortOrder`[​](#sortorder "Direct link to sortorder")

Sort order for queries.

#### Values[​](#values-4 "Direct link to Values")

* **`ASC`**: Ascending order.
* **`DESC`**: Descending order.

### `SessionState`[​](#sessionstate "Direct link to sessionstate")

State of a cluster/session.

#### Values[​](#values-5 "Direct link to Values")

* **`Stopped`**: The cluster is stopped.
* **`Terminated`**: The cluster is terminated.
* **`StartingUp`**: The cluster is starting up.
* **`StartupErrored`**: The cluster encountered an error during startup.
* **`Running`**: The cluster is running.
* **`Updating`**: The cluster is being updated.
* **`UpdatingErrored`**: The cluster encountered an error during update.
* **`Stopping`**: The cluster is stopping.
* **`Terminating`**: The cluster is terminating.
* **`AwaitingStartup`**: The cluster is awaiting startup.
* **`AwaitingFileMounts`**: The cluster is awaiting file mounts.
* **`TerminatingErrored`**: The cluster encountered an error during termination.
* **`StoppingErrored`**: The cluster encountered an error while stopping.
