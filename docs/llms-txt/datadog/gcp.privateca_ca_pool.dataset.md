# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.privateca_ca_pool.dataset.md

---
title: Certificate Authority Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Authority Pool
---

# Certificate Authority Pool

A Certificate Authority Pool in Google Cloud is a container for managing multiple certificate authorities within Certificate Authority Service. It allows you to group and organize CAs that share similar trust and policy requirements, simplifying certificate issuance and lifecycle management. Each pool can contain one or more CAs, and clients can request certificates from any CA in the pool based on defined policies.

```
gcp.privateca_ca_pool
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                         | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| issuance_policy      | core | json          | Optional. The IssuancePolicy to control how Certificates will be issued from this CaPool.                         |
| labels               | core | array<string> | Optional. Labels with user-defined metadata.                                                                      |
| name                 | core | string        | Identifier. The resource name for this CaPool in the format `projects/*/locations/*/caPools/*`.                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| publishing_options   | core | json          | Optional. The PublishingOptions to follow when issuing Certificates from any CertificateAuthority in this CaPool. |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| tier                 | core | string        | Required. Immutable. The Tier of this CaPool.                                                                     |
| zone_id              | core | string        |
