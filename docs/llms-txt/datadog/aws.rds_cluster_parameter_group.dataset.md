# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_cluster_parameter_group.dataset.md

---
title: RDS Cluster Parameter Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Cluster Parameter Group
---

# RDS Cluster Parameter Group

This table represents the RDS Cluster Parameter Group resource from Amazon Web Services.

```
aws.rds_cluster_parameter_group
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                          | Description |
| ------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| db_cluster_parameter_group_arn  | core | string     | The Amazon Resource Name (ARN) for the DB cluster parameter group.                                 |
| db_cluster_parameter_group_name | core | string     | The name of the DB cluster parameter group.                                                        |
| db_parameter_group_family       | core | string     | The name of the DB parameter group family that this DB cluster parameter group is compatible with. |
| description                     | core | string     | Provides the customer-specified description for this DB cluster parameter group.                   |
| tags                            | core | hstore_csv |
