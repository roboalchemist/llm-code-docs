# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.memorydb_acl.dataset.md

---
title: MemoryDB ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MemoryDB ACL
---

# MemoryDB ACL

MemoryDB ACL is an access control list resource in Amazon MemoryDB for Redis. It defines which users can connect to a MemoryDB cluster and what permissions they have. By assigning ACLs to clusters, you can enforce fine-grained access control, ensuring that only authorized users can perform specific operations on the data.

```
aws.memorydb_acl
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                   | Description |
| ---------------------- | ---- | ------------- | --------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| arn                    | core | string        | The Amazon Resource Name (ARN) of the ACL                                   |
| clusters               | core | array<string> | A list of clusters associated with the ACL.                                 |
| minimum_engine_version | core | string        | The minimum engine version supported for the ACL                            |
| name                   | core | string        | The name of the Access Control List                                         |
| pending_changes        | core | json          | A list of updates being applied to the ACL.                                 |
| status                 | core | string        | Indicates ACL status. Can be "creating", "active", "modifying", "deleting". |
| tags                   | core | hstore_csv    |
| user_names             | core | array<string> | The list of user names that belong to the ACL.                              |
