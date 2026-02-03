# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_client_tls_policy.dataset.md

---
title: ClientTlsPolicy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > ClientTlsPolicy
---

# ClientTlsPolicy

ClientTlsPolicy is a Google Cloud resource that defines how a client secures connections to a server using TLS. It specifies settings such as the trusted certificate authorities, client identity, and validation rules for server certificates. This policy helps ensure encrypted and authenticated communication between services.

```
gcp.networksecurity_client_tls_policy
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| client_certificate   | core | json          | Optional. Defines a mechanism to provision client identity (public and private keys) for peer to peer authentication. The presence of this dictates mTLS.                      |
| create_time          | core | timestamp     | Output only. The timestamp when the resource was created.                                                                                                                      |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Free-text description of the resource.                                                                                                                               |
| labels               | core | array<string> | Optional. Set of label tags associated with the resource.                                                                                                                      |
| name                 | core | string        | Required. Name of the ClientTlsPolicy resource. It matches the pattern `projects/{project}/locations/{location}/clientTlsPolicies/{client_tls_policy}`                         |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| server_validation_ca | core | json          | Optional. Defines the mechanism to obtain the Certificate Authority certificate to validate the server certificate. If empty, client does not validate the server certificate. |
| sni                  | core | string        | Optional. Server Name Indication string to present to the server during TLS handshake. E.g: "secure.example.com".                                                              |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp when the resource was updated.                                                                                                                      |
| zone_id              | core | string        |
