# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.run_domain_mapping.dataset.md

---
title: Cloud Run Domain Mapping
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Run Domain Mapping
---

# Cloud Run Domain Mapping

Cloud Run Domain Mapping in Google Cloud allows you to associate a custom domain with a Cloud Run service. It manages the necessary DNS records and SSL/TLS certificates automatically, enabling secure HTTPS access to your service through your own domain name. This simplifies custom domain configuration and certificate management for Cloud Run applications.

```
gcp.run_domain_mapping
```

## Fields

| Title                | ID   | Type          | Data Type                                                        | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| api_version          | core | string        | The API version for this call such as "domains.cloudrun.com/v1". |
| datadog_display_name | core | string        |
| gcp_status           | core | json          | The current status of the DomainMapping.                         |
| kind                 | core | string        | The kind of resource, in this case "DomainMapping".              |
| labels               | core | array<string> |
| metadata             | core | json          | Metadata associated with this BuildTemplate.                     |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| spec                 | core | json          | The spec for this DomainMapping.                                 |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
