# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshiftserverless_managed_workgroup.dataset.md

---
title: Redshift Serverless Managed Workgroup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Redshift Serverless Managed
  Workgroup
---

# Redshift Serverless Managed Workgroup

Redshift Serverless Managed Workgroup in AWS is a serverless compute resource for Amazon Redshift that automatically provisions and scales data warehouse capacity. It allows you to run analytics without managing clusters, handling scaling, availability, and performance tuning in the background. Workgroups define compute resources and security settings for running queries and workloads.

```
aws.redshiftserverless_managed_workgroup
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                          | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date          | core | timestamp  | The creation date of the managed workgroup.                                        |
| managed_workgroup_id   | core | string     | The unique identifier of the managed workgroup.                                    |
| managed_workgroup_name | core | string     | The name of the managed workgroup.                                                 |
| source_arn             | core | string     | The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog. |
| status                 | core | string     | The status of the managed workgroup.                                               |
| tags                   | core | hstore_csv |
