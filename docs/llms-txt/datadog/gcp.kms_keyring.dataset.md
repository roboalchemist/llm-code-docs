# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.kms_keyring.dataset.md

---
title: KMS Keyring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > KMS Keyring
---

# KMS Keyring

This table represents the KMS Keyring resource from Google Cloud Platform.

```
gcp.kms_keyring
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                         | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time at which this KeyRing was created.                                          |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The resource name for the KeyRing in the format `projects/*/locations/*/keyRings/*`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
