# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_farm.dataset.md

---
title: Deadline Cloud Farm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud Farm
---

# Deadline Cloud Farm

Deadline Cloud Farm in AWS represents a managed render farm resource within AWS Deadline Cloud. It provides a centralized environment for managing rendering workloads across compute resources. A farm defines the overall rendering capacity, configuration, and policies for distributing jobs to workers. It enables studios and teams to scale rendering tasks efficiently in the cloud, ensuring flexibility, cost control, and integration with creative pipelines.

```
aws.deadline_farm
```

## Fields

| Title       | ID   | Type       | Data Type                                      | Description |
| ----------- | ---- | ---------- | ---------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| created_at  | core | timestamp  | The date and time the resource was created.    |
| created_by  | core | string     | The user or system that created this resource. |
| farm_id     | core | string     | The farm ID.                                   |
| kms_key_arn | core | string     | The ARN for the KMS key.                       |
| tags        | core | hstore_csv |
| updated_at  | core | timestamp  | The date and time the resource was updated.    |
| updated_by  | core | string     | The user or system that updated this resource. |
