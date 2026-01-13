# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_migration_project.dataset.md

---
title: DMS Migration Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Migration Project
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.dms_migration_project.dataset/index.html
---

# DMS Migration Project

An AWS DMS Migration Project is a resource in Database Migration Service that defines and manages the configuration for migrating databases. It organizes migration settings, including source and target endpoints, data mapping, and transformation rules, into a reusable project. This helps streamline and standardize database migrations across different environments.

```
aws.dms_migration_project
```

## Fields

| Title                                    | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                | Description |
| ---------------------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string    |
| account_id                               | core | string    |
| description                              | core | string    | A user-friendly description of the migration project.                                                                                                                                                                                                                                    |
| instance_profile_arn                     | core | string    | The Amazon Resource Name (ARN) of the instance profile for your migration project.                                                                                                                                                                                                       |
| instance_profile_name                    | core | string    | The name of the associated instance profile.                                                                                                                                                                                                                                             |
| migration_project_arn                    | core | string    | The ARN string that uniquely identifies the migration project.                                                                                                                                                                                                                           |
| migration_project_creation_time          | core | timestamp | The time when the migration project was created.                                                                                                                                                                                                                                         |
| migration_project_name                   | core | string    | The name of the migration project.                                                                                                                                                                                                                                                       |
| schema_conversion_application_attributes | core | json      | The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.                                                                                                                                                                                |
| source_data_provider_descriptors         | core | json      | Information about the source data provider, including the name or ARN, and Secrets Manager parameters.                                                                                                                                                                                   |
| tags                                     | core | hstore    |
| target_data_provider_descriptors         | core | json      | Information about the target data provider, including the name or ARN, and Secrets Manager parameters.                                                                                                                                                                                   |
| transformation_rules                     | core | string    | The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects. |
