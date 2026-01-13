# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dynamodb_global_table.dataset.md

---
title: DynamoDB Global Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DynamoDB Global Table
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dynamodb_global_table.dataset/index.html
---

# DynamoDB Global Table

DynamoDB Global Table is a fully managed, multi-region, and multi-active database resource in AWS. It automatically replicates your DynamoDB tables across selected AWS regions, enabling low-latency data access and high availability for globally distributed applications. This resource helps ensure disaster recovery, fault tolerance, and seamless scalability without the need for complex replication setups.

```
aws.dynamodb_global_table
```

## Fields

| Title               | ID   | Type      | Data Type                                                                                                                                                                                                                    | Description |
| ------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string    |
| account_id          | core | string    |
| creation_date_time  | core | timestamp | The creation time of the global table.                                                                                                                                                                                       |
| global_table_arn    | core | string    | The unique identifier of the global table.                                                                                                                                                                                   |
| global_table_name   | core | string    | The global table name.                                                                                                                                                                                                       |
| global_table_status | core | string    | The current state of the global table: CREATING - The global table is being created. UPDATING - The global table is being updated. DELETING - The global table is being deleted. ACTIVE - The global table is ready for use. |
| replication_group   | core | json      | The Regions where the global table has replicas.                                                                                                                                                                             |
| tags                | core | hstore    |
