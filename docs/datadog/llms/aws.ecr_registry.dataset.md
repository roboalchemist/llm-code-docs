# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ecr_registry.dataset.md

---
title: ECR Registry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ECR Registry
---

# ECR Registry

ECR Registry in AWS is the private container image storage for Amazon Elastic Container Registry. It provides a central place to manage, store, and retrieve Docker and OCI images securely. The registry integrates with AWS Identity and Access Management for fine-grained access control and supports encryption, lifecycle policies, and cross-region replication.

```
aws.ecr_registry
```

## Fields

| Title                     | ID   | Type       | Data Type                                               | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| policies                  | core | json       |
| policy_text               | core | string     | The JSON text of the permissions policy for a registry. |
| registry_arn              | core | string     |
| registry_id               | core | string     | The registry ID associated with the request.            |
| replication_configuration | core | json       | The replication configuration for the registry.         |
| scanning_configuration    | core | json       | The scanning configuration for the registry.            |
| tags                      | core | hstore_csv |
