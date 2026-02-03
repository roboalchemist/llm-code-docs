# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dns_response_policy.dataset.md

---
title: DNS Response Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DNS Response Policy
---

# DNS Response Policy

A DNS Response Policy in Google Cloud lets you control how DNS queries are resolved within your network. It allows you to define custom rules to override standard DNS responses, block or redirect specific domains, and enforce security or compliance requirements. This helps manage internal name resolution and protect against unwanted or malicious domains.

```
gcp.dns_response_policy
```

## Fields

| Title                | ID   | Type          | Data Type                                                                               | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| description          | core | string        | User-provided description for this Response Policy.                                     |
| gke_clusters         | core | json          | The list of Google Kubernetes Engine clusters to which this response policy is applied. |
| id                   | core | string        | Unique identifier for the resource; defined by the server (output only).                |
| kind                 | core | string        |
| labels               | core | array<string> | User labels.                                                                            |
| networks             | core | json          | List of network names specifying networks to which this policy is applied.              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| response_policy_name | core | string        | User assigned name for this Response Policy.                                            |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
