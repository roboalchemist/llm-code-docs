# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_testgrid_project.dataset.md

---
title: Devicefarm Testgrid Project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Testgrid Project
---

# Devicefarm Testgrid Project

This table represents the devicefarm_testgrid_project resource from Amazon Web Services.

```
aws.devicefarm_testgrid_project
```

## Fields

| Title       | ID   | Type       | Data Type                                                           | Description |
| ----------- | ---- | ---------- | ------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The ARN for the project.                                            |
| created     | core | timestamp  | When the project was created.                                       |
| description | core | string     | A human-readable description for the project.                       |
| name        | core | string     | A human-readable name for the project.                              |
| tags        | core | hstore_csv |
| vpc_config  | core | json       | The VPC security groups and subnets that are attached to a project. |
