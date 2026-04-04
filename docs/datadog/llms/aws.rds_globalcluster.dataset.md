# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_globalcluster.dataset.md

---
title: RDS Global Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Global Cluster
---

# RDS Global Cluster

This table represents the RDS Global Cluster resource from Amazon Web Services.

```
aws.rds_globalcluster
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| database_name              | core | string     | The default database name within the new global database cluster.                                                                                                                                                                                                                                                                  |
| deletion_protection        | core | bool       | The deletion protection setting for the new global database cluster.                                                                                                                                                                                                                                                               |
| endpoint                   | core | string     | The writer endpoint for the new global database cluster. This endpoint always points to the writer DB instance in the current primary cluster.                                                                                                                                                                                     |
| engine                     | core | string     | The Aurora database engine used by the global database cluster.                                                                                                                                                                                                                                                                    |
| engine_lifecycle_support   | core | string     | The life cycle type for the global cluster. For more information, see CreateGlobalCluster.                                                                                                                                                                                                                                         |
| engine_version             | core | string     | Indicates the database engine version.                                                                                                                                                                                                                                                                                             |
| failover_state             | core | json       | A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster (Aurora global database). This object is empty unless the <code>SwitchoverGlobalCluster</code> or <code>FailoverGlobalCluster</code> operation was called on this global cluster. |
| global_cluster_arn         | core | string     | The Amazon Resource Name (ARN) for the global database cluster.                                                                                                                                                                                                                                                                    |
| global_cluster_identifier  | core | string     | Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database cluster.                                                                                                                                                                                          |
| global_cluster_members     | core | json       | The list of primary and secondary clusters within the global database cluster.                                                                                                                                                                                                                                                     |
| global_cluster_resource_id | core | string     | The Amazon Web Services Region-unique, immutable identifier for the global database cluster. This identifier is found in Amazon Web Services CloudTrail log entries whenever the Amazon Web Services KMS key for the DB cluster is accessed.                                                                                       |
| status                     | core | string     | Specifies the current state of this global database cluster.                                                                                                                                                                                                                                                                       |
| storage_encrypted          | core | bool       | The storage encryption setting for the global database cluster.                                                                                                                                                                                                                                                                    |
| tags                       | core | hstore_csv |
