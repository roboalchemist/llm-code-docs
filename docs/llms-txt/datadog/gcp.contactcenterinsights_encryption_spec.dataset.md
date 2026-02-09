# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.contactcenterinsights_encryption_spec.dataset.md

---
title: EncryptionSpec
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EncryptionSpec
---

# EncryptionSpec

EncryptionSpec in Google Cloud defines the encryption settings used to protect data at rest for a resource. It specifies the type of encryption key, such as a Google-managed key or a customer-managed key from Cloud KMS. This configuration ensures that sensitive data is encrypted according to organizational security and compliance requirements.

```
gcp.contactcenterinsights_encryption_spec
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The resource name of the encryption key specification resource. Format: projects/{project}/locations/{location}/encryptionSpec |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
