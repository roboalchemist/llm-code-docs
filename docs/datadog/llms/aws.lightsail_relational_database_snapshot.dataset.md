# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_relational_database_snapshot.dataset.md

---
title: Lightsail Relational Database Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Lightsail Relational Database
  Snapshot
---

# Lightsail Relational Database Snapshot

A Lightsail Relational Database Snapshot is a point-in-time backup of a managed database in Amazon Lightsail. It captures the entire database state, including data and settings, allowing you to restore the database to the exact moment the snapshot was taken. This helps with disaster recovery, data migration, and creating test environments without affecting the production database.

```
aws.lightsail_relational_database_snapshot
```

## Fields

| Title                                 | ID   | Type       | Data Type                                                                                                                                                                                                                                    | Description |
| ------------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string     |
| account_id                            | core | string     |
| arn                                   | core | string     | The Amazon Resource Name (ARN) of the database snapshot.                                                                                                                                                                                     |
| created_at                            | core | timestamp  | The timestamp when the database snapshot was created.                                                                                                                                                                                        |
| engine                                | core | string     | The software of the database snapshot (for example, MySQL)                                                                                                                                                                                   |
| engine_version                        | core | string     | The database engine version for the database snapshot (for example, 5.7.23).                                                                                                                                                                 |
| from_relational_database_arn          | core | string     | The Amazon Resource Name (ARN) of the database from which the database snapshot was created.                                                                                                                                                 |
| from_relational_database_blueprint_id | core | string     | The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.                                                                                                 |
| from_relational_database_bundle_id    | core | string     | The bundle ID of the database from which the database snapshot was created.                                                                                                                                                                  |
| from_relational_database_name         | core | string     | The name of the source database from which the database snapshot was created.                                                                                                                                                                |
| location                              | core | json       | The Region name and Availability Zone where the database snapshot is located.                                                                                                                                                                |
| name                                  | core | string     | The name of the database snapshot.                                                                                                                                                                                                           |
| resource_type                         | core | string     | The Lightsail resource type.                                                                                                                                                                                                                 |
| size_in_gb                            | core | int64      | The size of the disk in GB (for example, 32) for the database snapshot.                                                                                                                                                                      |
| state                                 | core | string     | The state of the database snapshot.                                                                                                                                                                                                          |
| support_code                          | core | string     | The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily. |
| tags                                  | core | hstore_csv |
