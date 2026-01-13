# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_update.dataset.md

---
title: EKS Update
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS Update
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eks_update.dataset/index.html
---

# EKS Update

EKS Update in AWS refers to the operation that updates an Amazon Elastic Kubernetes Service (EKS) cluster. It allows you to modify cluster settings such as Kubernetes version, logging configuration, or other cluster-level parameters. This operation helps keep your cluster secure, up to date, and aligned with the latest EKS features without needing to recreate the cluster.

```
aws.eks_update
```

## Fields

| Title      | ID   | Type      | Data Type                                                                | Description |
| ---------- | ---- | --------- | ------------------------------------------------------------------------ | ----------- |
| _key       | core | string    |
| account_id | core | string    |
| created_at | core | timestamp | The Unix epoch timestamp at object creation.                             |
| errors     | core | json      | Any errors associated with a Failed update.                              |
| id         | core | string    | A UUID that is used to track the update.                                 |
| params     | core | json      | A key-value map that contains the parameters associated with the update. |
| status     | core | string    | The current status of the update.                                        |
| tags       | core | hstore    |
| type       | core | string    | The type of the update.                                                  |
