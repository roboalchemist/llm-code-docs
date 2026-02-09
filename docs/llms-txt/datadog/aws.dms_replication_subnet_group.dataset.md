# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_replication_subnet_group.dataset.md

---
title: DMS Replication Subnet Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Replication Subnet Group
---

# DMS Replication Subnet Group

An AWS DMS Replication Subnet Group is a collection of subnets that you specify for a Database Migration Service replication instance. It defines the network boundaries and availability zones where the replication instance can run, ensuring secure and reliable connectivity to source and target databases during migration.

```
aws.dms_replication_subnet_group
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                                                                                                                                                                 | Description |
| ------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string        |
| account_id                           | core | string        |
| replication_subnet_group_description | core | string        | A description for the replication subnet group.                                                                                                                                                                           |
| replication_subnet_group_identifier  | core | string        | The identifier of the replication instance subnet group.                                                                                                                                                                  |
| subnet_group_status                  | core | string        | The status of the subnet group.                                                                                                                                                                                           |
| subnets                              | core | json          | The subnets that are in the subnet group.                                                                                                                                                                                 |
| supported_network_types              | core | array<string> | The IP addressing protocol supported by the subnet group. This is used by a replication instance with values such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported. |
| tags                                 | core | hstore_csv    |
| vpc_id                               | core | string        | The ID of the VPC.                                                                                                                                                                                                        |
