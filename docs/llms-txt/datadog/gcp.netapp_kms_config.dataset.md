# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_kms_config.dataset.md

---
title: NetApp KmsConfig
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp KmsConfig
---

# NetApp KmsConfig

NetApp KmsConfig in Google Cloud is a configuration resource that defines the Key Management Service (KMS) settings for a NetApp Cloud Volumes instance. It specifies which Cloud KMS key is used to encrypt data at rest, allowing users to manage encryption keys independently for enhanced security and compliance.

```
gcp.netapp_kms_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Create time of the KmsConfig.                                                                                                               |
| crypto_key_name      | core | string        | Required. Customer managed crypto key resource full name. Format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. |
| datadog_display_name | core | string        |
| description          | core | string        | Description of the KmsConfig.                                                                                                                            |
| instructions         | core | string        | Output only. Instructions to provide the access to the customer provided encryption key.                                                                 |
| labels               | core | array<string> | Labels as key value pairs                                                                                                                                |
| name                 | core | string        | Identifier. Name of the KmsConfig.                                                                                                                       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_account      | core | string        | Output only. The Service account which will have access to the customer provided encryption key.                                                         |
| state                | core | string        | Output only. State of the KmsConfig.                                                                                                                     |
| state_details        | core | string        | Output only. State details of the KmsConfig.                                                                                                             |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
