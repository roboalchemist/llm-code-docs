# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.certificatemanager_certificate.dataset.md

---
title: Certificate Manager Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Manager Certificate
---

# Certificate Manager Certificate

Certificate Manager Certificate in Google Cloud is a managed resource that provisions and manages SSL/TLS certificates for your applications and services. It supports both Google-managed and self-managed certificates, automating tasks like renewal and deployment. This helps ensure secure communication over HTTPS without manual certificate handling.

```
gcp.certificatemanager_certificate
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of a Certificate.                                                                                                                                                                                             |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. One or more paragraphs of text description of a certificate.                                                                                                                                                                            |
| expire_time          | core | timestamp     | Output only. The expiry timestamp of a Certificate.                                                                                                                                                                                               |
| labels               | core | array<string> | Optional. Set of labels associated with a Certificate.                                                                                                                                                                                            |
| managed              | core | json          | If set, contains configuration and state of a managed certificate.                                                                                                                                                                                |
| name                 | core | string        | Identifier. A user-defined name of the certificate. Certificate names must be unique globally and match pattern `projects/*/locations/*/certificates/*`.                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| pem_certificate      | core | string        | Output only. The PEM-encoded certificate chain.                                                                                                                                                                                                   |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| san_dnsnames         | core | array<string> | Output only. The list of Subject Alternative Names of dnsName type defined in the certificate (see RFC 5280 4.2.1.6). Managed certificates that haven't been provisioned yet have this field populated with a value of the managed.domains field. |
| scope                | core | string        | Optional. Immutable. The scope of the certificate.                                                                                                                                                                                                |
| self_managed         | core | json          | If set, defines data of a self-managed certificate.                                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update timestamp of a Certificate.                                                                                                                                                                                          |
| used_by              | core | json          | Output only. The list of resources that use this Certificate.                                                                                                                                                                                     |
| zone_id              | core | string        |
