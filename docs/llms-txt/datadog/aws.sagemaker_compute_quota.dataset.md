# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_compute_quota.dataset.md

---
title: SageMaker Compute Quota
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Compute Quota
---

# SageMaker Compute Quota

SageMaker Compute Quota in AWS defines the limits on compute resources that can be used for SageMaker workloads, such as training jobs, endpoints, and notebook instances. It helps manage and control the maximum capacity available to ensure fair usage and prevent overconsumption of resources.

```
aws.sagemaker_compute_quota
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                     | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| activation_state      | core | string     | The state of the compute allocation being described. Use to enable or disable compute allocation. Default is Enabled.                         |
| cluster_arn           | core | string     | ARN of the cluster.                                                                                                                           |
| compute_quota_arn     | core | string     | ARN of the compute allocation definition.                                                                                                     |
| compute_quota_config  | core | json       | Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks. |
| compute_quota_id      | core | string     | ID of the compute allocation definition.                                                                                                      |
| compute_quota_target  | core | json       | The target entity to allocate compute resources to.                                                                                           |
| compute_quota_version | core | int64      | Version of the compute allocation definition.                                                                                                 |
| created_by            | core | json       | Information about the user who created or modified a SageMaker resource.                                                                      |
| creation_time         | core | timestamp  | Creation time of the compute allocation configuration.                                                                                        |
| description           | core | string     | Description of the compute allocation definition.                                                                                             |
| failure_reason        | core | string     | Failure reason of the compute allocation definition.                                                                                          |
| last_modified_by      | core | json       | Information about the user who created or modified a SageMaker resource.                                                                      |
| last_modified_time    | core | timestamp  | Last modified time of the compute allocation configuration.                                                                                   |
| name                  | core | string     | Name of the compute allocation definition.                                                                                                    |
| status                | core | string     | Status of the compute allocation definition.                                                                                                  |
| tags                  | core | hstore_csv |
