# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_target_group.dataset.md

---
title: VPC Lattice Target Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Target Group
---

# VPC Lattice Target Group

This table represents the VPC Lattice Target Group resource from Amazon Web Services.

```
aws.vpc_lattice_target_group
```

## Fields

| Title           | ID   | Type          | Data Type                                                                     | Description |
| --------------- | ---- | ------------- | ----------------------------------------------------------------------------- | ----------- |
| _key            | core | string        |
| account_id      | core | string        |
| arn             | core | string        | The Amazon Resource Name (ARN) of the target group.                           |
| config          | core | json          | The target group configuration.                                               |
| created_at      | core | timestamp     | The date and time that the target group was created, in ISO-8601 format.      |
| failure_code    | core | string        | The failure code.                                                             |
| failure_message | core | string        | The failure message.                                                          |
| id              | core | string        | The ID of the target group.                                                   |
| last_updated_at | core | timestamp     | The date and time that the target group was last updated, in ISO-8601 format. |
| name            | core | string        | The name of the target group.                                                 |
| service_arns    | core | array<string> | The Amazon Resource Names (ARNs) of the service.                              |
| status          | core | string        | The status.                                                                   |
| tags            | core | hstore_csv    |
| type            | core | string        | The target group type.                                                        |
