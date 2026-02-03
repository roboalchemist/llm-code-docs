# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.speech_custom_class.dataset.md

---
title: CustomClass
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CustomClass
---

# CustomClass

CustomClass in Google Cloud is a Speech-to-Text resource that defines custom word classes to improve recognition accuracy for specific terms, such as product names or domain-specific vocabulary. It allows users to group related words or phrases and reference them in speech adaptation configurations, helping the model better understand context and pronunciation variations.

```
gcp.speech_custom_class
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations.                                                                                                                                                 |
| create_time          | core | timestamp     | Output only. Creation time.                                                                                                                                                                                                                                                                              |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. The time at which this resource was requested for deletion.                                                                                                                                                                                                                                 |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding.                                                                                       |
| expire_time          | core | timestamp     | Output only. The time at which this resource will be purged.                                                                                                                                                                                                                                             |
| gcp_display_name     | core | string        | Optional. User-settable, human-readable name for the CustomClass. Must be 63 characters or less.                                                                                                                                                                                                         |
| items                | core | json          | A collection of class items.                                                                                                                                                                                                                                                                             |
| kms_key_name         | core | string        | Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the CustomClass is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.                                                        |
| kms_key_version_name | core | string        | Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which the CustomClass is encrypted. The expected format is `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}`. |
| labels               | core | array<string> |
| name                 | core | string        | Output only. Identifier. The resource name of the CustomClass. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`.                                                                                                                                                           |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. Whether or not this CustomClass is in the process of being updated.                                                                                                                                                                                                                         |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The CustomClass lifecycle state.                                                                                                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. System-assigned unique identifier for the CustomClass.                                                                                                                                                                                                                                      |
| update_time          | core | timestamp     | Output only. The most recent time this resource was modified.                                                                                                                                                                                                                                            |
| zone_id              | core | string        |
