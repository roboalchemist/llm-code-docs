# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudkms_crypto_key_version.dataset.md

---
title: Cloud KMS CryptoKeyVersion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud KMS CryptoKeyVersion
---

# Cloud KMS CryptoKeyVersion

A Cloud KMS CryptoKeyVersion in Google Cloud represents a specific version of a cryptographic key within a Cloud KMS key. Each version contains the actual key material used for encryption, decryption, signing, or verification. Key versions allow for key rotation and lifecycle management, enabling secure updates without disrupting applications.

```
gcp.cloudkms_crypto_key_version
```

## Fields

| Title                               | ID   | Type          | Data Type                                                                                                                                                                                                                                         | Description |
| ----------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string        |
| algorithm                           | core | string        | Output only. The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports.                                                                                                                                                                   |
| ancestors                           | core | array<string> |
| attestation                         | core | json          | Output only. Statement that was generated and signed by the HSM at key creation time. Use this statement to verify attributes of the key as stored on the HSM, independently of Google. Only provided for key versions with protection_level HSM. |
| create_time                         | core | timestamp     | Output only. The time at which this CryptoKeyVersion was created.                                                                                                                                                                                 |
| datadog_display_name                | core | string        |
| destroy_event_time                  | core | timestamp     | Output only. The time this CryptoKeyVersion's key material was destroyed. Only present if state is DESTROYED.                                                                                                                                     |
| destroy_time                        | core | timestamp     | Output only. The time this CryptoKeyVersion's key material is scheduled for destruction. Only present if state is DESTROY_SCHEDULED.                                                                                                              |
| external_destruction_failure_reason | core | string        | Output only. The root cause of the most recent external destruction failure. Only present if state is EXTERNAL_DESTRUCTION_FAILED.                                                                                                                |
| external_protection_level_options   | core | json          | ExternalProtectionLevelOptions stores a group of additional fields for configuring a CryptoKeyVersion that are specific to the EXTERNAL protection level and EXTERNAL_VPC protection levels.                                                      |
| generate_time                       | core | timestamp     | Output only. The time this CryptoKeyVersion's key material was generated.                                                                                                                                                                         |
| generation_failure_reason           | core | string        | Output only. The root cause of the most recent generation failure. Only present if state is GENERATION_FAILED.                                                                                                                                    |
| import_failure_reason               | core | string        | Output only. The root cause of the most recent import failure. Only present if state is IMPORT_FAILED.                                                                                                                                            |
| import_job                          | core | string        | Output only. The name of the ImportJob used in the most recent import of this CryptoKeyVersion. Only present if the underlying key material was imported.                                                                                         |
| import_time                         | core | timestamp     | Output only. The time at which this CryptoKeyVersion's key material was most recently imported.                                                                                                                                                   |
| labels                              | core | array<string> |
| name                                | core | string        | Output only. The resource name for this CryptoKeyVersion in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`.                                                                                                      |
| organization_id                     | core | string        |
| parent                              | core | string        |
| project_id                          | core | string        |
| project_number                      | core | string        |
| protection_level                    | core | string        | Output only. The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion.                                                                                                                                       |
| region_id                           | core | string        |
| reimport_eligible                   | core | bool          | Output only. Whether or not this key version is eligible for reimport, by being specified as a target in ImportCryptoKeyVersionRequest.crypto_key_version.                                                                                        |
| resource_name                       | core | string        |
| state                               | core | string        | The current state of the CryptoKeyVersion.                                                                                                                                                                                                        |
| tags                                | core | hstore_csv    |
| zone_id                             | core | string        |
