# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_ssl_certificate.dataset.md

---
title: SSL Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SSL Certificate
---

# SSL Certificate

An SSL Certificate in Google Cloud is a managed resource that provides secure communication between clients and services by encrypting data in transit. It can be automatically provisioned and renewed by Google or manually uploaded by the user. These certificates are typically used with load balancers and other HTTPS endpoints to ensure data integrity and confidentiality.

```
gcp.compute_ssl_certificate
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| ancestors                 | core | array<string> |
| certificate               | core | string        | A value read into memory from a certificate file. The certificate file must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert.                                                                                                                                                                                                                                    |
| creation_timestamp        | core | timestamp     | [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                             |
| datadog_display_name      | core | string        |
| description               | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| expire_time               | core | string        | Output only. [Output Only] Expire time of the certificate. RFC3339                                                                                                                                                                                                                                                                                                                                                                                  |
| id                        | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                     |
| kind                      | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#sslCertificate for SSL certificates.                                                                                                                                                                                                                                                                                                                                                 |
| labels                    | core | array<string> |
| managed                   | core | json          | Configuration and status of a managed SSL certificate.                                                                                                                                                                                                                                                                                                                                                                                              |
| name                      | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id           | core | string        |
| parent                    | core | string        |
| project_id                | core | string        |
| project_number            | core | string        |
| region                    | core | string        | Output only. [Output Only] URL of the region where the regional SSL Certificate resides. This field is not applicable to global SSL Certificate.                                                                                                                                                                                                                                                                                                    |
| region_id                 | core | string        |
| resource_name             | core | string        |
| self_link                 | core | string        | [Output only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| self_managed              | core | json          | Configuration and status of a self-managed SSL certificate.                                                                                                                                                                                                                                                                                                                                                                                         |
| subject_alternative_names | core | array<string> | Output only. [Output Only] Domains associated with the certificate via Subject Alternative Name.                                                                                                                                                                                                                                                                                                                                                    |
| tags                      | core | hstore_csv    |
| type                      | core | string        | (Optional) Specifies the type of SSL certificate, either "SELF_MANAGED" or "MANAGED". If not specified, the certificate is self-managed and the fieldscertificate and private_key are used.                                                                                                                                                                                                                                                         |
| zone_id                   | core | string        |
