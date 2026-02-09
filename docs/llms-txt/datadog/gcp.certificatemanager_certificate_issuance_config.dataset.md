# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.certificatemanager_certificate_issuance_config.dataset.md

---
title: Certificate Issuance Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Issuance Configuration
---

# Certificate Issuance Configuration

Certificate Issuance Configuration in Google Cloud is a resource that defines how SSL/TLS certificates are issued and managed for your domains. It specifies the certificate authority, lifetime, and key parameters used when creating certificates. This configuration helps automate and standardize certificate provisioning for services like load balancers or managed domains, ensuring secure communication and compliance with organizational policies.

```
gcp.certificatemanager_certificate_issuance_config
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                            | Description |
| ---------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| certificate_authority_config | core | json          | Required. The CA that issues the workload certificate. It includes the CA address, type, authentication to CA service, etc.                                                                          |
| create_time                  | core | timestamp     | Output only. The creation timestamp of a CertificateIssuanceConfig.                                                                                                                                  |
| datadog_display_name         | core | string        |
| description                  | core | string        | Optional. One or more paragraphs of text description of a CertificateIssuanceConfig.                                                                                                                 |
| key_algorithm                | core | string        | Required. The key algorithm to use when generating the private key.                                                                                                                                  |
| labels                       | core | array<string> | Optional. Set of labels associated with a CertificateIssuanceConfig.                                                                                                                                 |
| lifetime                     | core | string        | Required. Workload certificate lifetime requested.                                                                                                                                                   |
| name                         | core | string        | Identifier. A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern `projects/*/locations/*/certificateIssuanceConfigs/*`. |
| organization_id              | core | string        |
| parent                       | core | string        |
| project_id                   | core | string        |
| project_number               | core | string        |
| region_id                    | core | string        |
| resource_name                | core | string        |
| rotation_window_percentage   | core | int64         | Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive.                                    |
| tags                         | core | hstore_csv    |
| update_time                  | core | timestamp     | Output only. The last update timestamp of a CertificateIssuanceConfig.                                                                                                                               |
| zone_id                      | core | string        |
