# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudkms_import_job.dataset.md

---
title: Cloud KMS Import Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud KMS Import Job
---

# Cloud KMS Import Job

A Cloud KMS Import Job in Google Cloud is a temporary resource used to securely import cryptographic key material into Cloud Key Management Service. It defines the parameters and wrapping keys required for the import process, ensuring that key material is encrypted and protected during transfer. Once the import is complete, the job expires and cannot be reused.

```
gcp.cloudkms_import_job
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| attestation          | core | json          | Output only. Statement that was generated and signed by the key creator (for example, an HSM) at key creation time. Use this statement to verify attributes of the key as stored on the HSM, independently of Google. Only present if the chosen ImportMethod is one with a protection level of HSM. |
| create_time          | core | timestamp     | Output only. The time at which this ImportJob was created.                                                                                                                                                                                                                                           |
| datadog_display_name | core | string        |
| expire_event_time    | core | timestamp     | Output only. The time this ImportJob expired. Only present if state is EXPIRED.                                                                                                                                                                                                                      |
| expire_time          | core | timestamp     | Output only. The time at which this ImportJob is scheduled for expiration and can no longer be used to import key material.                                                                                                                                                                          |
| generate_time        | core | timestamp     | Output only. The time this ImportJob's key material was generated.                                                                                                                                                                                                                                   |
| import_method        | core | string        | Required. Immutable. The wrapping method to be used for incoming key material.                                                                                                                                                                                                                       |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The resource name for this ImportJob in the format `projects/*/locations/*/keyRings/*/importJobs/*`.                                                                                                                                                                                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| protection_level     | core | string        | Required. Immutable. The protection level of the ImportJob. This must match the protection_level of the version_template on the CryptoKey you attempt to import into.                                                                                                                                |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of the ImportJob, indicating if it can be used.                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
