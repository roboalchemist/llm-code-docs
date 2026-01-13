# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.emrcontainers_virtual_cluster.dataset.md

---
title: EMR on EKS Virtual Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EMR on EKS Virtual Cluster
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.emrcontainers_virtual_cluster.dataset/index.html
---

# EMR on EKS Virtual Cluster

EMR on EKS Virtual Cluster is a managed resource in AWS that lets you run Amazon EMR workloads on Amazon Elastic Kubernetes Service. It acts as a logical abstraction that maps EMR jobs to a specific Kubernetes namespace within an EKS cluster, enabling you to run big data frameworks like Spark without managing separate EMR clusters.

```
aws.emrcontainers_virtual_cluster
```

## Fields

| Title                     | ID   | Type      | Data Type                                              | Description |
| ------------------------- | ---- | --------- | ------------------------------------------------------ | ----------- |
| _key                      | core | string    |
| account_id                | core | string    |
| arn                       | core | string    | The ARN of the virtual cluster.                        |
| container_provider        | core | json      | The container provider of the virtual cluster.         |
| created_at                | core | timestamp | The date and time when the virtual cluster is created. |
| id                        | core | string    | The ID of the virtual cluster.                         |
| name                      | core | string    | The name of the virtual cluster.                       |
| security_configuration_id | core | string    | The ID of the security configuration.                  |
| state                     | core | string    | The state of the virtual cluster.                      |
| tags                      | core | hstore    |
