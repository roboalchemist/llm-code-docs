# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.eventarc_google_api_source.dataset.md

---
title: Google API Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Google API Source
---

# Google API Source

Google API Source is a Google Cloud resource that connects external APIs or services to Google Cloud's event-driven infrastructure. It allows events from Google or third-party APIs to be delivered to Cloud Run, Cloud Functions, or other event consumers. This enables seamless integration of external systems with Google Cloud applications through standardized event delivery.

```
gcp.eventarc_google_api_source
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Resource annotations.                                                                                                                                                                                                  |
| create_time          | core | timestamp     | Output only. The creation time.                                                                                                                                                                                                  |
| crypto_key_name      | core | string        | Optional. Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`.                                          |
| datadog_display_name | core | string        |
| destination          | core | string        | Required. Destination is the message bus that the GoogleApiSource is delivering to. It must be point to the full resource name of a MessageBus. Format: "projects/{PROJECT_ID}/locations/{region}/messagesBuses/{MESSAGE_BUS_ID) |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on update and delete requests to ensure that the client has an up-to-date value before proceeding.               |
| gcp_display_name     | core | string        | Optional. Resource display name.                                                                                                                                                                                                 |
| labels               | core | array<string> | Optional. Resource labels.                                                                                                                                                                                                       |
| logging_config       | core | json          | Optional. Config to control Platform logging for the GoogleApiSource.                                                                                                                                                            |
| name                 | core | string        | Identifier. Resource name of the form projects/{project}/locations/{location}/googleApiSources/{google_api_source}                                                                                                               |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.                                                                    |
| update_time          | core | timestamp     | Output only. The last-modified time.                                                                                                                                                                                             |
| zone_id              | core | string        |
