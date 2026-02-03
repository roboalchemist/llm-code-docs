# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.integrations_certificate.dataset.md

---
title: Certificate Manager Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Manager Certificate
---

# Certificate Manager Certificate

Certificate Manager Certificate in Google Cloud is a managed resource that provisions and manages SSL/TLS certificates for securing applications and services. It supports both Google-managed and self-managed certificates, automating tasks like renewal and deployment. This helps ensure secure communication for domains and load-balanced endpoints without manual certificate handling.

```
gcp.integrations_certificate
```

## Fields

| Title                | ID   | Type          | Data Type                                                                 | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| certificate_status   | core | string        | Status of the certificate                                                 |
| credential_id        | core | string        | Immutable. Credential id that will be used to register with trawler       |
| datadog_display_name | core | string        |
| description          | core | string        | Description of the certificate                                            |
| gcp_display_name     | core | string        | Required. Name of the certificate                                         |
| labels               | core | array<string> |
| name                 | core | string        | Output only. Auto generated primary key                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| raw_certificate      | core | json          | Input only. Raw client certificate which would be registered with trawler |
| region_id            | core | string        |
| requestor_id         | core | string        | Immutable. Requestor ID to be used to register certificate with trawler   |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| valid_end_time       | core | timestamp     | Output only. The timestamp after which certificate will expire            |
| valid_start_time     | core | timestamp     | Output only. The timestamp after which certificate will be valid          |
| zone_id              | core | string        |
