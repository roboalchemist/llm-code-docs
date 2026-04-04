# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_listener.dataset.md

---
title: VPC Lattice Listener
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Listener
---

# VPC Lattice Listener

This table represents the VPC Lattice Listener resource from Amazon Web Services.

```
aws.vpc_lattice_listener
```

## Fields

| Title           | ID   | Type       | Data Type                                                                 | Description |
| --------------- | ---- | ---------- | ------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| arn             | core | string     | The Amazon Resource Name (ARN) of the listener.                           |
| created_at      | core | timestamp  | The date and time that the listener was created, in ISO-8601 format.      |
| default_action  | core | json       | The actions for the default listener rule.                                |
| id              | core | string     | The ID of the listener.                                                   |
| last_updated_at | core | timestamp  | The date and time that the listener was last updated, in ISO-8601 format. |
| name            | core | string     | The name of the listener.                                                 |
| port            | core | int64      | The listener port.                                                        |
| protocol        | core | string     | The listener protocol.                                                    |
| service_arn     | core | string     | The Amazon Resource Name (ARN) of the service.                            |
| service_id      | core | string     | The ID of the service.                                                    |
| tags            | core | hstore_csv |
