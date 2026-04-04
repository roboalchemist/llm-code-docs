# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_cluster_scheduler_config.dataset.md

---
title: SageMaker Cluster Scheduler Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Cluster Scheduler Config
---

# SageMaker Cluster Scheduler Config

SageMaker Cluster Scheduler Config in AWS provides details about the scheduling configuration for a SageMaker cluster. It defines how compute resources are allocated and managed within the cluster, including policies for scaling, job placement, and workload distribution. This helps optimize performance and cost efficiency when running machine learning training or inference workloads across multiple nodes.

```
aws.sagemaker_cluster_scheduler_config
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                                                                                                                   | Description |
| -------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| cluster_arn                      | core | string     | ARN of the cluster where the cluster policy is applied.                                                                                                                                     |
| cluster_scheduler_config_arn     | core | string     | ARN of the cluster policy.                                                                                                                                                                  |
| cluster_scheduler_config_id      | core | string     | ID of the cluster policy.                                                                                                                                                                   |
| cluster_scheduler_config_version | core | int64      | Version of the cluster policy.                                                                                                                                                              |
| created_by                       | core | json       | Information about the user who created or modified a SageMaker resource.                                                                                                                    |
| creation_time                    | core | timestamp  | Creation time of the cluster policy.                                                                                                                                                        |
| description                      | core | string     | Description of the cluster policy.                                                                                                                                                          |
| failure_reason                   | core | string     | Failure reason of the cluster policy.                                                                                                                                                       |
| last_modified_by                 | core | json       | Information about the user who created or modified a SageMaker resource.                                                                                                                    |
| last_modified_time               | core | timestamp  | Last modified time of the cluster policy.                                                                                                                                                   |
| name                             | core | string     | Name of the cluster policy.                                                                                                                                                                 |
| scheduler_config                 | core | json       | Cluster policy configuration. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities. |
| status                           | core | string     | Status of the cluster policy.                                                                                                                                                               |
| tags                             | core | hstore_csv |
