# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudfunctions_function.dataset.md

---
title: Cloud Functions Function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Functions Function
---

# Cloud Functions Function

Cloud Functions Function in GCP is a serverless compute resource that lets you run event-driven code without managing servers. It automatically scales based on incoming requests or events, supports multiple runtimes, and integrates with other Google Cloud services. This resource is ideal for lightweight applications, APIs, and background processing tasks.

```
gcp.cloudfunctions_function
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| build_config         | core | json          | Describes the Build step of the function that builds a container from the given source.                                                                                                                              |
| create_time          | core | timestamp     | Output only. The create timestamp of a Cloud Function. This is only applicable to 2nd Gen functions.                                                                                                                 |
| datadog_display_name | core | string        |
| description          | core | string        | User-provided description of a function.                                                                                                                                                                             |
| environment          | core | string        | Describe whether the function is 1st Gen or 2nd Gen.                                                                                                                                                                 |
| event_trigger        | core | json          | An Eventarc trigger managed by Google Cloud Functions that fires events in response to a condition in another service.                                                                                               |
| kms_key_name         | core | string        | Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources. It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. |
| labels               | core | array<string> | Labels associated with this Cloud Function.                                                                                                                                                                          |
| name                 | core | string        | A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*`                                                                                   |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                |
| service_config       | core | json          | Describes the Service being deployed. Currently deploys services to Cloud Run (fully managed).                                                                                                                       |
| state                | core | string        | Output only. State of the function.                                                                                                                                                                                  |
| state_messages       | core | json          | Output only. State Messages for this Cloud Function.                                                                                                                                                                 |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update timestamp of a Cloud Function.                                                                                                                                                          |
| upgrade_info         | core | json          | Output only. UpgradeInfo for this Cloud Function                                                                                                                                                                     |
| url                  | core | string        | Output only. The deployed url for the function.                                                                                                                                                                      |
| zone_id              | core | string        |
