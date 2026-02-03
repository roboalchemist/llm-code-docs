# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.network_acl.dataset.md

---
title: Network ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network ACL
---

# Network ACL

This table represents the Network ACL resource from Amazon Web Services.

```
aws.network_acl
```

## Fields

| Title           | ID   | Type       | Data Type                                                            | Description |
| --------------- | ---- | ---------- | -------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| associations    | core | json       | Any associations between the network ACL and your subnets            |
| entries         | core | json       | The entries (rules) in the network ACL.                              |
| is_default      | core | bool       | Indicates whether this is the default network ACL for the VPC.       |
| network_acl_arn | core | string     |
| network_acl_id  | core | string     | The ID of the network ACL.                                           |
| owner_id        | core | string     | The ID of the Amazon Web Services account that owns the network ACL. |
| tags            | core | hstore_csv |
| vpc_id          | core | string     | The ID of the VPC for the network ACL.                               |
