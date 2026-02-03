# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.security_group.dataset.md

---
title: Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Group
---

# Security Group

This table represents the Security Group resource from Amazon Web Services.

```
aws.security_group
```

## Fields

| Title                 | ID   | Type       | Data Type                                                              | Description |
| --------------------- | ---- | ---------- | ---------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| description           | core | string     | A description of the security group.                                   |
| group_id              | core | string     | The ID of the security group.                                          |
| group_name            | core | string     | The name of the security group.                                        |
| ip_permissions        | core | json       | The inbound rules associated with the security group.                  |
| ip_permissions_egress | core | json       | The outbound rules associated with the security group.                 |
| owner_id              | core | string     | The Amazon Web Services account ID of the owner of the security group. |
| security_group_arn    | core | string     |
| tags                  | core | hstore_csv |
| vpc_id                | core | string     | The ID of the VPC for the security group.                              |
