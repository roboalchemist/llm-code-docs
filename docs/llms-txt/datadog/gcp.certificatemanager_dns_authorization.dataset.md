# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.certificatemanager_dns_authorization.dataset.md

---
title: Certificate Manager DNS Authorization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Certificate Manager DNS
  Authorization
---

# Certificate Manager DNS Authorization

Certificate Manager DNS Authorization in Google Cloud is a resource used to verify domain ownership through DNS records. It creates and manages DNS authorizations that allow Certificate Manager to issue and manage SSL/TLS certificates for specific domains. This ensures secure communication and automated certificate lifecycle management.

```
gcp.certificatemanager_dns_authorization
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of a DnsAuthorization.                                                                                                                                                                                 |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. One or more paragraphs of text description of a DnsAuthorization.                                                                                                                                                                |
| dns_resource_record  | core | json          | Output only. DNS Resource Record that needs to be added to DNS configuration.                                                                                                                                                              |
| domain               | core | string        | Required. Immutable. A domain that is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for `example.com` can be used to issue certificates for `example.com` and `*.example.com`. |
| labels               | core | array<string> | Optional. Set of labels associated with a DnsAuthorization.                                                                                                                                                                                |
| name                 | core | string        | Identifier. A user-defined name of the dns authorization. DnsAuthorization names must be unique globally and match pattern `projects/*/locations/*/dnsAuthorizations/*`.                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Optional. Immutable. Type of DnsAuthorization. If unset during resource creation the following default will be used: - in location `global`: FIXED_RECORD, - in other locations: PER_PROJECT_RECORD.                                       |
| update_time          | core | timestamp     | Output only. The last update timestamp of a DnsAuthorization.                                                                                                                                                                              |
| zone_id              | core | string        |
