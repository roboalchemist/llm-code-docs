# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_cluster.dataset.md

---
title: SageMaker Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Cluster
---

# SageMaker Cluster

SageMaker Cluster in AWS is a managed resource that provides a group of compute instances for running machine learning workloads. It allows you to scale training and inference jobs across multiple nodes, offering high performance and flexibility for distributed ML tasks. This resource is designed to simplify cluster management, enabling users to focus on model development and deployment without handling infrastructure complexity.

```
aws.sagemaker_cluster
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                               | Description |
| --------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| cluster_arn     | core | string     | The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.                                                                                                                                                                                                                       |
| cluster_name    | core | string     | The name of the SageMaker HyperPod cluster.                                                                                                                                                                                                                                             |
| cluster_status  | core | string     | The status of the SageMaker HyperPod cluster.                                                                                                                                                                                                                                           |
| creation_time   | core | timestamp  | The time when the SageMaker Cluster is created.                                                                                                                                                                                                                                         |
| failure_message | core | string     | The failure message of the SageMaker HyperPod cluster.                                                                                                                                                                                                                                  |
| instance_groups | core | json       | The instance groups of the SageMaker HyperPod cluster.                                                                                                                                                                                                                                  |
| node_recovery   | core | string     | The node recovery mode configured for the SageMaker HyperPod cluster.                                                                                                                                                                                                                   |
| orchestrator    | core | json       | The type of orchestrator used for the SageMaker HyperPod cluster.                                                                                                                                                                                                                       |
| tags            | core | hstore_csv |
| vpc_config      | core | json       | Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see Give SageMaker Access to Resources in your Amazon VPC. |
