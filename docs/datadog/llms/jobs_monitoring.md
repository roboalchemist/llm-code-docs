# Source: https://docs.datadoghq.com/data_observability/jobs_monitoring.md

---
title: 'Data Observability: Jobs Monitoring'
description: >-
  Monitor performance, reliability, and cost efficiency of data processing jobs
  across platforms like EMR, Databricks, Dataproc, and Kubernetes.
breadcrumbs: 'Docs > Data Observability Overview > Data Observability: Jobs Monitoring'
---

# Data Observability: Jobs Monitoring

{% image
   source="https://datadog-docs.imgix.net/images/data_jobs/overview_062024.b8fd03bff95a8b967ee2f580ec451e29.png?auto=format"
   alt="Datadog Data Observability: Jobs Monitoring overview page" /%}

Data Observability: Jobs Monitoring provides visibility into the performance, reliability, and cost efficiency of your data processing jobs, along with the underlying infrastructure. Data Observability: Jobs Monitoring enables you to:

- Track the health and performance of data processing jobs across your accounts and workspaces. See which take up the most compute resources or have inefficiencies.
- Receive an alert when a job failsâor when a job is taking too long to complete.
- Analyze job execution details and stack traces.
- Correlate infrastructure metrics, Spark metrics from the Spark UI, logs, and cluster configuration.
- Compare multiple runs to facilitate troubleshooting, and to optimize provisioning and configuration during deployment.

## Setup{% #setup %}

Data Observability: Jobs Monitoring supports multiple job technologies. To get started, select your technology and follow the installation instructions:

- [Databricks](https://docs.datadoghq.com/data_jobs/databricks/)
- [Airflow](https://docs.datadoghq.com/data_jobs/airflow/)
- [dbt cloud](https://docs.datadoghq.com/data_observability/jobs_monitoring/dbt)

Data Observability: Jobs Monitoring also supports Apache Spark jobs on the following platforms:

- [Kubernetes](https://docs.datadoghq.com/data_jobs/kubernetes/)
- [Amazon EMR](https://docs.datadoghq.com/data_jobs/emr)
- [GCP Dataproc](https://docs.datadoghq.com/data_jobs/dataproc/)

## Explore Data Observability: Jobs Monitoring{% #explore-data-observability-jobs-monitoring %}

### Easily identify unreliable and inefficient jobs{% #easily-identify-unreliable-and-inefficient-jobs %}

View all jobs across cloud accounts and workspaces. Identify failing jobs to take action on, or find jobs with high idle CPU that are using a lot of compute and should be optimized.

### Receive alerts on problematic jobs{% #receive-alerts-on-problematic-jobs %}

Datadog monitors send alerts when a job fails, or is running beyond its completion time. Browse [monitor templates](https://app.datadoghq.com/monitors/templates) to monitor data jobs specific to your installed integrations.

### Analyze and troubleshoot individual jobs{% #analyze-and-troubleshoot-individual-jobs %}

Click on a job to see how it performed across multiple runs, as well as error messages for failed runs.

{% image
   source="https://datadog-docs.imgix.net/images/data_jobs/djm_job_062024.fd215e0f626c9539cc833f8bb18b8a49.png?auto=format"
   alt="Job Overview page for 'product-insights' Spark Application job" /%}

### Analyze an individual run{% #analyze-an-individual-run %}

Clicking on a run opens a side panel with details of how much time was spent on each Spark job and stage, along with a breakdown of resource consumption and Spark metrics, such as idle executor CPU, input/output data volume, shuffling, and disk spill. From this panel, you can correlate the execution with executor and driver node resource utilization, logs, and the job and cluster configuration.

On the **Infrastructure** tab, you can correlate the execution to infrastructure metrics.

{% image
   source="https://datadog-docs.imgix.net/images/data_jobs/djm_run_infra_062024.4300d723b05903b874fc331eeb329db9.png?auto=format"
   alt="Data Observability: Jobs Monitoring > Run panel, Infrastructure tab" /%}

For a failed run, look at the **Errors** tab to see the stack trace, which can help you determine where and how this failure occurred.

To determine why a stage is taking a long time to complete, you can use the **Spark Task Metrics** tab to view task-level metrics for a specific Spark stage, so that you can identify data skew. See the distribution of time spent and data consumed by different tasks.

{% image
   source="https://datadog-docs.imgix.net/images/data_jobs/djm_task_metrics.f04230a5d8a5452ac7a47fa5c82026e4.png?auto=format"
   alt="Data Observability: Jobs Monitoring > Run panel, Spark Task Metrics tab" /%}

## Further Reading{% #further-reading %}

- [Data Streams Monitoring](https://docs.datadoghq.com/data_streams)
- [Ensure trust across the entire data life cycle with Datadog Data Observability](https://www.datadoghq.com/blog/data-observability/)
