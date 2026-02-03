# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_url_list.dataset.md

---
title: URL List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > URL List
---

# URL List

A URL List in Google Cloud is a resource used to define and manage lists of URLs or domains for network security policies. It allows administrators to group multiple URLs into a single object that can be referenced in firewall rules, security policies, or threat protection configurations. This helps simplify policy management and ensures consistent enforcement of access controls across environments.

```
gcp.networksecurity_url_list
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                   | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time when the security policy was created.                                                                                                                                                     |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Free-text description of the resource.                                                                                                                                                            |
| labels               | core | array<string> |
| name                 | core | string        | Required. Name of the resource provided by the user. Name is of the form projects/{project}/locations/{location}/urlLists/{url_list} url_list should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time when the security policy was updated.                                                                                                                                                     |
| values               | core | array<string> | Required. FQDNs and URLs.                                                                                                                                                                                   |
| zone_id              | core | string        |
