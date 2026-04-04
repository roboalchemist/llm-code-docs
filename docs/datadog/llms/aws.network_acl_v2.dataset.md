# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.network_acl_v2.dataset.md

---
title: Network ACL V2
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network ACL V2
---

# Network ACL V2

This table represents the Network ACL V2 resource from Amazon Web Services.

```
aws.network_acl_v2
```

## Fields

| Title           | ID   | Type       | Data Type | Description |
| --------------- | ---- | ---------- | --------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| entries         | core | json       |
| is_default      | core | bool       |
| network_acl_arn | core | string     |
| network_acl_id  | core | string     |
| owner_id        | core | string     |
| tags            | core | hstore_csv |
| vpc_id          | core | string     |
