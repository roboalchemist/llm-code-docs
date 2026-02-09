# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_cluster_parameter_group.dataset.md

---
title: Redshift Cluster Parameter Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Cluster Parameter Group
---

# Redshift Cluster Parameter Group

An Amazon Redshift Cluster Parameter Group is a collection of configuration settings that manage the behavior of Redshift clusters. It acts as a container for engine configuration values, such as query performance tuning, logging, and workload management. By creating and applying a custom parameter group, you can override default settings to optimize cluster performance and tailor it to specific workloads.

```
aws.redshift_cluster_parameter_group
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                            | Description |
| ------------------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| account_id                           | core | string     |
| description                          | core | string     | The description of the parameter group.                                                              |
| parameter_group_family               | core | string     | The name of the cluster parameter group family that this cluster parameter group is compatible with. |
| parameter_group_name                 | core | string     | The name of the cluster parameter group.                                                             |
| redshift_cluster_parameter_group_arn | core | string     |
| tags                                 | core | hstore_csv |
