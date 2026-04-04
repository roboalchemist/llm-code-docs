# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_rule.dataset.md

---
title: VPC Lattice Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Rule
---

# VPC Lattice Rule

This table represents the VPC Lattice Rule resource from Amazon Web Services.

```
aws.vpc_lattice_rule
```

## Fields

| Title           | ID   | Type       | Data Type                                                                      | Description |
| --------------- | ---- | ---------- | ------------------------------------------------------------------------------ | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| action          | core | json       | The action for the default rule.                                               |
| arn             | core | string     | The Amazon Resource Name (ARN) of the listener.                                |
| created_at      | core | timestamp  | The date and time that the listener rule was created, in ISO-8601 format.      |
| id              | core | string     | The ID of the listener.                                                        |
| is_default      | core | bool       | Indicates whether this is the default rule.                                    |
| last_updated_at | core | timestamp  | The date and time that the listener rule was last updated, in ISO-8601 format. |
| match           | core | json       | The rule match.                                                                |
| name            | core | string     | The name of the listener.                                                      |
| priority        | core | int64      | The priority level for the specified rule.                                     |
| tags            | core | hstore_csv |
