# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_address_group.dataset.md

---
title: Address Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Address Group
---

# Address Group

An Address Group in Google Cloud is a network security resource that lets you group multiple IP addresses, IP ranges, or other address groups into a single entity. It simplifies the management of firewall rules and security policies by allowing you to reference the group instead of individual addresses. This helps maintain consistency and reduces configuration complexity across network security setups.

```
gcp.networksecurity_address_group
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                         | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| capacity             | core | int64         | Required. Capacity of the Address Group                                                                           |
| create_time          | core | timestamp     | Output only. The timestamp when the resource was created.                                                         |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Free-text description of the resource.                                                                  |
| items                | core | array<string> | Optional. List of items.                                                                                          |
| labels               | core | array<string> | Optional. Set of label tags associated with the AddressGroup resource.                                            |
| name                 | core | string        | Required. Name of the AddressGroup resource. It matches pattern `projects/*/locations/{location}/addressGroups/`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| purpose              | core | array<string> | Optional. List of supported purposes of the Address Group.                                                        |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. Server-defined fully-qualified URL for this resource.                                                |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Required. The type of the Address Group. Possible values are "IPv4" or "IPV6".                                    |
| update_time          | core | timestamp     | Output only. The timestamp when the resource was updated.                                                         |
| zone_id              | core | string        |
