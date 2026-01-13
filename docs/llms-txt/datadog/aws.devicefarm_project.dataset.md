# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_project.dataset.md

---
title: Device Farm Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Device Farm Project
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.devicefarm_project.dataset/index.html
---

# Device Farm Project

A Device Farm Project in AWS is a container for running and managing mobile app tests across a wide range of real devices hosted in the cloud. It organizes test runs, results, and device selections, allowing teams to validate app performance and compatibility at scale.

```
aws.devicefarm_project
```

## Fields

| Title                       | ID   | Type      | Data Type                                                                                                                       | Description |
| --------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    |
| arn                         | core | string    | The project's ARN.                                                                                                              |
| created                     | core | timestamp | When the project was created.                                                                                                   |
| default_job_timeout_minutes | core | int64     | The default number of minutes (at the project level) a test run executes before it times out. The default value is 150 minutes. |
| name                        | core | string    | The project's name.                                                                                                             |
| tags                        | core | hstore    |
| vpc_config                  | core | json      | The VPC security groups and subnets that are attached to a project.                                                             |
