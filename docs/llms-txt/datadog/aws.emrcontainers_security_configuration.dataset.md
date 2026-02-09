# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.emrcontainers_security_configuration.dataset.md

---
title: EMR on EKS Security Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EMR on EKS Security Configuration
---

# EMR on EKS Security Configuration

This table represents the EMR on EKS Security Configuration resource from Amazon Web Services.

```
aws.emrcontainers_security_configuration
```

## Fields

| Title                       | ID   | Type       | Data Type                                                     | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| arn                         | core | string     | The ARN (Amazon Resource Name) of the security configuration. |
| created_at                  | core | timestamp  | The date and time that the job run was created.               |
| created_by                  | core | string     | The user who created the job run.                             |
| id                          | core | string     | The ID of the security configuration.                         |
| name                        | core | string     | The name of the security configuration.                       |
| security_configuration_data | core | json       | Security configuration inputs for the request.                |
| tags                        | core | hstore_csv |
