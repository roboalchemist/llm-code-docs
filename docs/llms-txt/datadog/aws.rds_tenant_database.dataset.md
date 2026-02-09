# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_tenant_database.dataset.md

---
title: RDS Tenant Database
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Tenant Database
---

# RDS Tenant Database

This table represents the RDS Tenant Database resource from Amazon Web Services.

```
aws.rds_tenant_database
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                            | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| character_set_name          | core | string     | The character set of the tenant database.                                            |
| db_instance_identifier      | core | string     | The ID of the DB instance that contains the tenant database.                         |
| dbi_resource_id             | core | string     | The Amazon Web Services Region-unique, immutable identifier for the DB instance.     |
| deletion_protection         | core | bool       | Specifies whether deletion protection is enabled for the DB instance.                |
| master_username             | core | string     | The master username of the tenant database.                                          |
| nchar_character_set_name    | core | string     | The NCHAR character set name of the tenant database.                                 |
| pending_modified_values     | core | json       | Information about pending changes for a tenant database.                             |
| status                      | core | string     | The status of the tenant database.                                                   |
| tags                        | core | hstore_csv |
| tenant_database_arn         | core | string     | The Amazon Resource Name (ARN) for the tenant database.                              |
| tenant_database_create_time | core | timestamp  | The creation time of the tenant database.                                            |
| tenant_database_resource_id | core | string     | The Amazon Web Services Region-unique, immutable identifier for the tenant database. |
| tenant_db_name              | core | string     | The database name of the tenant database.                                            |
