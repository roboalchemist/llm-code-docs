# Source: https://docs.anyscale.com/jobs/queues.md

# Submit jobs to persistent job queues

[View Markdown](/jobs/queues.md)

# Submit jobs to persistent job queues

This page provides an overview of Anyscale job queues.

important

Anyscale has deprecated the `max_concurrency` setting for job queues. See [Concurrent jobs in job queues](#concurrency).

## What are job queues?[​](#what-are-job-queues "Direct link to What are job queues?")

Job queues use a persistent Anyscale cluster for running jobs sequentially. A job queue consists of two components:

* An Anyscale cluster. By default, the same compute config applies across all jobs submitted to a job queue. Jobs submitted to a job queue use the same compute and storage resources.
* A queue of jobs waiting to run. You configure the priority and execution mode to control how Anyscale orders newly submitted jobs.

Use job queues to reduce cluster startup times while running related workloads that have similar runtime and compute requirements. You must use the same Ray version and Python version across all jobs in a job queue, but can use different images to control other dependencies.

warning

Anyscale doesn't provide full isolation guarantees for workloads that reuses persistent compute resources using job queues.

### Job queue semantics[​](#job-queue-semantics "Direct link to Job queue semantics")

The following describes the lifecycle of a job queue:

1. Anyscale creates a job queue the first time you submit a job with a new job queue name.

2. You submit additional jobs to the job queue using the queue name as the identifier.

3. Anyscale always schedules the next job in the queue based on the following:

   <!-- -->

   * **Available capacity**: The total number of worker nodes available in compute config. Job queues auto-scale based on the capacity requirements of scheduled jobs. Anyscale doesn't schedule jobs to the persistent cluster until required capacity is available.
   * **Prioritization**: Jobs enter the queue based on the configured priority and execution mode. See [How do job queues prioritize jobs?](#priority).

4. Once scheduled, a job runs until completion. This includes retries up to the specified number of `max_retries`.

5. The job queue cluster terminates once all jobs in the queue have run and the configured timeout threshold passes.

6. When you submit a job to run on an existing job queue with a terminated cluster, the cluster restarts.

### Scheduling and job queues[​](#scheduling-and-job-queues "Direct link to Scheduling and job queues")

*Scheduling* a job is the process of assigning a job to nodes in the cluster and running the job.

Anyscale doesn't intend job queues to serve as a *job scheduler*. Anyscale doesn't have built-in support for running jobs using conditional logic or dependencies such as completion of other jobs.

Anyscale supports cron scheduling, which uses cron expressions to run jobs on a specified cadence. See [Job schedules](/jobs/schedules.md).

You can use job queues in combination with cron schedules or external scheduling tools.

## How do job queues prioritize jobs?[​](#priority "Direct link to How do job queues prioritize jobs?")

Use the `execution_mode` setting to configure the algorithm used to prioritize jobs.

The following table describes the possible execution modes:

| Execution mode | Description                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `PRIORITY`     | **Default**. Uses the integer `priority` value assigned to each job in the `job_queue_config`. `0` is the highest priority. Jobs of equal priority run in arrival order. |
| `FIFO`         | First-in, first-out. Jobs run in the order they arrive in the job queue.                                                                                                 |
| `LIFO`         | Last-in, first-out. When a job completes and the cluster is available, the job most recently added to the queue runs next.                                               |

## Create a job queue[​](#create "Direct link to Create a job queue")

You create a job queue by adding a job queue configuration to a job configuration then submitting that job.

Anytime you submit an Anyscale job with a job queue spec that includes a new job queue name, Anyscale creates a new job queue.

note

You can reuse the same job queue spec across multiple jobs or job runs if you don't change any of the configurations.

Anyscale recommends using the `target_job_queue_name` parameter for all workloads other than workload that creates the job queue. See [Add jobs to an existing queue](#submit).

* CLI
* SDK

Use the following syntax to create a job config YAML file that includes a job queue config:

```
entrypoint: python main.py

name: <job-name>

# Specify a compute_config for the cluster.
# compute_config must be the same for all jobs in a given queue.
# Each job can use a different image_uri but all images must use the same Ray and Python versions.
compute_config: <compute-config-name>:<version>
image_uri: <image-uri>:<version>

job_queue_config:
  priority: 100 # Valid when `execution_mode: PRIORITY`; 0 is highest priority, 2^64 is lowest. Jobs of equal priority execute in arrival order.

  job_queue_spec:
    name: <job-queue-name>
    execution_mode: PRIORITY # Scheduling algorithm; can also be FIFO (first-in, first-out) or LIFO (last-in, first-out).
    idle_timeout_s: 3600 # Set to 0 to disable idle termination.
```

Submit your job using the following CLI command:

```
anyscale job submit --config-file /path/to/job-config.yaml
```

Use the following syntax to define a submit a job config with a job queue config using the SDK:

```

import anyscale
from anyscale.job.models import JobConfig, JobQueueConfig, JobQueueSpec, JobQueueExecutionMode

config = JobConfig(
  name="<job-name>",
  entrypoint="python main.py",
  compute_config="<compute-config-name>:<version>",
  image_uri="<image-uri>:<version>",
  job_queue_config=JobQueueConfig(
    # Valid when `execution_mode: PRIORITY`; 0 is highest priority, 2^64 is lowest.
    # Jobs of equal priority execute in arrival order.
    priority=100,
    job_queue_spec=JobQueueSpec(
      name="<job-queue-name>",
      # Scheduling algorithm; can also be FIFO (first-in, first-out) or LIFO (last-in, first-out).
      execution_mode=JobQueueExecutionMode.PRIORITY,
      # Set to 0 to disable idle termination
      idle_timeout_s=3600,
    ),
  ),
)

anyscale.job.submit(config)
```

Replace the following:

* `<job-name>`: (Optional) Name for the job.
* `<compute-config-name>:<version>`: Name of an existing registered compute config with a version number. The default is the latest version.
* `<image-uri>:<version>`: URI of an existing image with a version number. The default is the latest version.
* `<job-queue-name>`: Name of the job queue, which serves as the unique identifier for the job queue.

See the API reference for [`JobQueueConfig`](/reference/job-api.md#jobqueueconfig) and [`JobQueueSpec`](/reference/job-api.md#jobqueuespec).

important

If this is the first job for a job queue, Anyscale creates a new cluster based on `job_queue_spec`, `compute_config`, and `image_uri`.

The Ray and Python versions from the container image in your first job define the version requirements for your job queue. Job queues only support container images that use the same Ray and Python versions.

The submission fails if you submit a job with the same job queue `name` but a different `job_queue_spec` or `compute_config`.

If you don't specify `compute_config` or `image_uri`, Anyscale uses the defaults for the current workspace or cloud.

## Add jobs to an existing queue[​](#submit "Direct link to Add jobs to an existing queue")

If you have an existing job queue, you can add new jobs by specifying the `target_job_queue_name` in the job config.

You can deploy each job in your job queue with a different `image_uri`.

note

If you specify an `image_uri` that differs from the container image used by the job that created the job queue, you can't specify other runtime environment settings such as `working_dir`, `env_vars`, and `requirements` when submitting multiple jobs to a job queue. You must package all code dependencies into your container image when scheduling jobs with job queues. See [Refactor development patterns to define custom images](/development/containers.md#define-image).

If all jobs in a job queue use the same container image, you can use other runtime environment settings.

The following example syntax demonstrates this pattern and omits the compute config, Ray version, and most job queue config options. If you include these configuration options, they must match the configurations used by the job that created your job queue cluster.

* CLI
* SDK

Use the following syntax to create a job config YAML file to add to an existing job queue:

```
name: <new-job-name>
entrypoint: python hello_world.py
image_uri: <new-image-uri>:<version>

job_queue_config:
  priority: 100
  target_job_queue_name: <job-queue-name>
```

Submit your job using the following CLI command:

```
anyscale job submit --config-file /path/to/job-config.yaml
```

```

import anyscale
from anyscale.job.models import JobConfig, JobQueueConfig, JobQueueSpec, JobQueueExecutionMode

config = JobConfig(
  name=<new-job-name>,
  entrypoint="python hello_world.py",
  image_uri="<new-image-uri>:<version>",
  job_queue_config=JobQueueConfig(
    priority=100,
    target_job_queue_name=<job-queue-name>,
  ),
)

anyscale.job.submit(config)
```

## View jobs in a queue[​](#view "Direct link to View jobs in a queue")

View jobs in a queue and their status in the Anyscale console, CLI, or SDK.

* Anyscale console
* CLI
* SDK

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click **Jobs**.
3. Click **Job queues**.
4. Click the name of the job queue. The job queue **Overview** appears.

Use the **Jobs** section to search for information about individual jobs in the queue.

To view job queue details and job counts, run the following:

```
anyscale job-queue status --name <job-queue-name> --project <project-name>
```

To list jobs, use `anyscale job list` with filters. See [Job API Reference](/reference/job-api.md) and [Job Queue API Reference](/reference/job-queue.md).

To get job queue status and details, run the following:

```
import anyscale

status = anyscale.job_queue.status(name="<job-queue-name>", project="<project-name>")
print(status)
```

To list jobs, use `anyscale.job.list()`. See [Job API Reference](/reference/job-api.md) and [Job Queue API Reference](/reference/job-queue.md).

## Terminate a job queue[​](#terminate-a-job-queue "Direct link to Terminate a job queue")

Terminating a job queue terminates all running and pending jobs and the underlying cluster. To restart the queue, submit a new job to the queue.

You can also terminate individual running or pending jobs in a queue. See [Terminate a job](/jobs/manage.md#terminate).

* Anyscale console
* CLI
* SDK

From the job queue overview page in the console, click **Terminate job queue**.

Run the following command to terminate a job queue:

```
anyscale job-queue terminate --name <job-queue-name> --project <project-name>
```

Run the following command to terminate a job queue:

```
import anyscale

anyscale.job_queue.terminate(name="<job-queue-name>", project="<project-name>")
```

## Delete a job queue[​](#delete "Direct link to Delete a job queue")

Delete a job queue to permanently remove the job queue cluster. You can't delete a job queue with running or pending jobs.

Deleting a job queue doesn't remove job run information from the Anyscale console.

* CLI
* SDK

Run the following command to delete a job queue:

```
anyscale job-queue delete --name <job-queue-name> --project <project-name>
```

Run the following command to delete a job queue:

```
import anyscale

anyscale.job_queue.delete(name="<job-queue-name>", project="<project-name>")
```

## Concurrent jobs in job queues[​](#concurrency "Direct link to Concurrent jobs in job queues")

Anyscale has deprecated support for running concurrent jobs on job queues. Anyscale has turned off this feature by default in new clouds and existing clouds that don't have job queues configured with a `max_concurrency` setting greater than one. Existing clouds that use job queues to run concurrent jobs retain this feature.

Ray provides limited guarantees around resource isolation and fair sharing, which can lead to unpredictable performance with concurrent job runs on job queues. Anyscale recommends migrating production workloads away from running concurrently on job queues.

Contact [Anyscale support](mailto:support@anyscale.com) to request enablement for this feature in your cloud.
