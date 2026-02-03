# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_snapshot_tenant_database.dataset.md

---
title: RDS Snapshot Tenant Database
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Snapshot Tenant Database
---

# RDS Snapshot Tenant Database

This table represents the RDS Snapshot Tenant Database resource from Amazon Web Services.

```
aws.rds_snapshot_tenant_database
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                               | Description |
| ------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| character_set_name              | core | string     | The name of the character set of a tenant database.                                                                                     |
| db_instance_identifier          | core | string     | The ID for the DB instance that contains the tenant databases.                                                                          |
| db_snapshot_identifier          | core | string     | The identifier for the snapshot of the DB instance.                                                                                     |
| db_snapshot_tenant_database_arn | core | string     | The Amazon Resource Name (ARN) for the snapshot tenant database.                                                                        |
| dbi_resource_id                 | core | string     | The resource identifier of the source CDB instance. This identifier can't be changed and is unique to an Amazon Web Services Region.    |
| engine_name                     | core | string     | The name of the database engine.                                                                                                        |
| master_username                 | core | string     | The master username of the tenant database.                                                                                             |
| nchar_character_set_name        | core | string     | The <code>NCHAR</code> character set name of the tenant database.                                                                       |
| snapshot_type                   | core | string     | The type of DB snapshot.                                                                                                                |
| tags                            | core | hstore_csv |
| tenant_database_create_time     | core | timestamp  | The time the DB snapshot was taken, specified in Coordinated Universal Time (UTC). If you copy the snapshot, the creation time changes. |
| tenant_database_resource_id     | core | string     | The resource ID of the tenant database.                                                                                                 |
| tenant_db_name                  | core | string     | The name of the tenant database.                                                                                                        |
