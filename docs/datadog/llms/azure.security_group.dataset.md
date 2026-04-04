# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.security_group.dataset.md

---
title: Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Group
---

# Security Group

This table represents the Security Group resource from Microsoft Azure.

```
azure.security_group
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| default_security_rules | core | json       | The default security rules of network security group.                    |
| etag                   | core | string     | A unique read-only string that changes whenever the resource is updated. |
| id                     | core | string     | Resource ID.                                                             |
| location               | core | string     | Resource location.                                                       |
| name                   | core | string     | Resource name.                                                           |
| provisioning_state     | core | string     | The provisioning state of the network security group resource.           |
| resource_group         | core | string     |
| resource_guid          | core | string     | The resource GUID property of the network security group resource.       |
| security_rules         | core | json       | A collection of security rules of the network security group.            |
| subscription_id        | core | string     |
| subscription_name      | core | string     |
| tags                   | core | hstore_csv |
| type                   | core | string     | Resource type.                                                           |
