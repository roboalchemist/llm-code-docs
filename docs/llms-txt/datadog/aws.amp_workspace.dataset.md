# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.amp_workspace.dataset.md

---
title: Managed Service for Prometheus Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Managed Service for Prometheus
  Workspace
---

# Managed Service for Prometheus Workspace

Managed Service for Prometheus Workspace in AWS is a fully managed, scalable, and secure environment for monitoring and alerting based on Prometheus. It allows you to collect, store, and query metrics from containerized or cloud-native applications without managing the underlying infrastructure. This service integrates with AWS security, scalability, and availability features, making it easier to run Prometheus workloads in production.

```
aws.amp_workspace
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                    | Description |
| ------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| alias               | core | string     | The alias that is assigned to this workspace to help identify it. It does not need to be unique.                                                                             |
| arn                 | core | string     | The ARN of the workspace. For example, arn:aws:aps:<region>:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234.                                                  |
| created_at          | core | timestamp  | The date and time that the workspace was created.                                                                                                                            |
| kms_key_arn         | core | string     | (optional) If the workspace was created with a customer managed KMS key, the ARN for the key used.                                                                           |
| prometheus_endpoint | core | string     | The Prometheus endpoint available for this workspace. For example, https://aps-workspaces.<region>.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/. |
| status              | core | json       | The current status of the workspace.                                                                                                                                         |
| tags                | core | hstore_csv |
| workspace_id        | core | string     | The unique ID for the workspace. For example, ws-example1-1234-abcd-5678-ef90abcd1234.                                                                                       |
