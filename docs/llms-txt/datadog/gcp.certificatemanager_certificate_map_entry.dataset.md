# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.certificatemanager_certificate_map_entry.dataset.md

---
title: Certificate Map Entry
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Map Entry
---

# Certificate Map Entry

A Certificate Map Entry in Google Cloud is a configuration element within Certificate Manager that associates a specific hostname or pattern with a managed or self-managed SSL certificate. It enables flexible routing of incoming HTTPS requests to the correct certificate based on domain names, simplifying certificate management for multiple domains or subdomains.

```
gcp.certificatemanager_certificate_map_entry
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| certificates         | core | array<string> | Optional. A set of Certificates defines for the given `hostname`. There can be defined up to four certificates in each Certificate Map Entry. Each certificate must match pattern `projects/*/locations/*/certificates/*`. |
| create_time          | core | timestamp     | Output only. The creation timestamp of a Certificate Map Entry.                                                                                                                                                            |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. One or more paragraphs of text description of a certificate map entry.                                                                                                                                           |
| hostname             | core | string        | A Hostname (FQDN, e.g. `example.com`) or a wildcard hostname expression (`*.example.com`) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate.              |
| labels               | core | array<string> | Optional. Set of labels associated with a Certificate Map Entry.                                                                                                                                                           |
| matcher              | core | string        | A predefined matcher for particular cases, other than SNI selection.                                                                                                                                                       |
| name                 | core | string        | Identifier. A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*/certificateMapEntries/*`.                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. A serving state of this Certificate Map Entry.                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The update timestamp of a Certificate Map Entry.                                                                                                                                                              |
| zone_id              | core | string        |
