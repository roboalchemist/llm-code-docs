# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_data_provider.dataset.md

---
title: DMS Data Provider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Data Provider
---

# DMS Data Provider

DMS Data Provider in AWS Database Migration Service represents a connection profile that defines how DMS connects to a specific data source or target. It stores connection details such as engine type, authentication, and network settings, allowing migrations to be managed more easily and reused across multiple tasks.

```
aws.dms_data_provider
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                              | Description |
| --------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| data_provider_arn           | core | string     | The Amazon Resource Name (ARN) string that uniquely identifies the data provider.                                                                                                                                                                                                      |
| data_provider_creation_time | core | timestamp  | The time the data provider was created.                                                                                                                                                                                                                                                |
| data_provider_name          | core | string     | The name of the data provider.                                                                                                                                                                                                                                                         |
| description                 | core | string     | A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.                         |
| engine                      | core | string     | The type of database engine for the data provider. Valid values include "aurora", "aurora-postgresql", "mysql", "oracle", "postgres", "sqlserver", redshift, mariadb, mongodb, db2, db2-zos, docdb, and sybase. A value of "aurora" represents Amazon Aurora MySQL-Compatible Edition. |
| settings                    | core | json       | The settings in JSON format for a data provider.                                                                                                                                                                                                                                       |
| tags                        | core | hstore_csv |
