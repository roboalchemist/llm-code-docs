# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.certificatemanager_trust_config.dataset.md

---
title: Certificate Manager TrustConfig
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Manager TrustConfig
---

# Certificate Manager TrustConfig

Certificate Manager TrustConfig in Google Cloud is a resource that defines trust stores and trust anchors used for certificate validation. It allows you to configure how certificates are trusted within your environment, including specifying custom certificate authorities or system roots. This helps manage secure communication and authentication for services that rely on TLS or mTLS connections.

```
gcp.certificatemanager_trust_config
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                                                               | Description |
| ------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| allowlisted_certificates | core | json          | Optional. A certificate matching an allowlisted certificate is always considered valid as long as the certificate is parseable, proof of private key possession is established, and constraints on the certificate's SAN field are met.                 |
| ancestors                | core | array<string> |
| create_time              | core | timestamp     | Output only. The creation timestamp of a TrustConfig.                                                                                                                                                                                                   |
| datadog_display_name     | core | string        |
| description              | core | string        | Optional. One or more paragraphs of text description of a TrustConfig.                                                                                                                                                                                  |
| etag                     | core | string        | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                                                               |
| labels                   | core | array<string> | Optional. Set of labels associated with a TrustConfig.                                                                                                                                                                                                  |
| name                     | core | string        | Identifier. A user-defined name of the trust config. TrustConfig names must be unique globally and match pattern `projects/*/locations/*/trustConfigs/*`.                                                                                               |
| organization_id          | core | string        |
| parent                   | core | string        |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| resource_name            | core | string        |
| tags                     | core | hstore_csv    |
| trust_stores             | core | json          | Optional. Set of trust stores to perform validation against. This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation. Only one TrustStore specified is currently allowed. |
| update_time              | core | timestamp     | Output only. The last update timestamp of a TrustConfig.                                                                                                                                                                                                |
| zone_id                  | core | string        |
