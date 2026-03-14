# Source: https://docs.anyscale.com/jobs.md

# What are Anyscale jobs?

[View Markdown](/jobs.md)

# What are Anyscale jobs?

Anyscale jobs run offline workloads in production with automatic retries, resource management, and comprehensive monitoring. Use jobs for batch processing tasks such as model training, batch inference, and data processing pipelines.

For continuously running applications such as model serving endpoints, see [What are Anyscale services?](/services.md).

## Common use cases[​](#use-cases "Direct link to Common use cases")

The following are examples of workloads suited for Anyscale jobs:

| Use case              | Description                                                             |
| --------------------- | ----------------------------------------------------------------------- |
| Batch inference       | Process large datasets through ML models for predictions at scale.      |
| Model training        | Distribute training workloads across multiple GPUs or nodes.            |
| Model fine-tuning     | Fine-tune large language models on custom datasets.                     |
| Data processing       | Transform, clean, and prepare large datasets using Ray Data.            |
| Hyperparameter tuning | Run parallel experiments to find optimal model configurations.          |
| ETL pipelines         | Extract, transform, and load data between systems.                      |
| Recurring workloads   | Schedule periodic data updates, model retraining, or report generation. |

## Key features[​](#features "Direct link to Key features")

Anyscale jobs provide the following features for production batch workloads:

| Feature                  | Description                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automatic retries        | Configure retry policies with `max_retries` to automatically restart failed jobs. Jobs restart from the beginning with the same configuration.                                  |
| Job queues               | Run multiple jobs on the same cluster to reduce startup times. Supports FIFO, LIFO, and priority-based scheduling. See [Submit jobs to persistent job queues](/jobs/queues.md). |
| Job schedules            | Schedule recurring workloads using cron expressions with timezone support. Automatically run jobs at specified intervals. See [Job schedules](/jobs/schedules.md).              |
| Cluster management       | Anyscale provisions clusters automatically when jobs start and terminates them when jobs complete. Configure custom compute resources or use existing clusters.                 |
| Comprehensive monitoring | Access job metrics, logs, Ray Dashboard, and custom Grafana dashboards. Set up alerts for job failures or performance issues. See [Monitor a job](/jobs/monitor.md).            |
| Multi-cloud support      | Run jobs with consistent APIs and configurations on AWS, Azure, Google Cloud, neoclouds, or Anyscale-hosted infrastructure.                                                     |

## Getting started[​](#getting-started "Direct link to Getting started")

To run your first job, see [Get started with jobs](/jobs/tutorial.md).

For detailed information on creating and managing jobs, see [Create and manage jobs](/jobs/manage.md).

## Best practices[​](#best-practices "Direct link to Best practices")

* Configure appropriate retry policies for fault tolerance. See [Create and manage jobs](/jobs/manage.md).
* Avoid scheduling Ray tasks on the head node for compute-intensive workloads. See [Control head node scheduling](/configuration/compute/advanced.md#head-node).
* Monitor job execution with metrics and logs for effective debugging. See [Monitor a job](/jobs/monitor.md).

## Pricing[​](#pricing "Direct link to Pricing")

Jobs use standard Anyscale pricing based on the type of machines used. See the [Anyscale pricing page](https://www.anyscale.com/pricing-detail).
