# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.eventarc_message_bus.dataset.md

---
title: Eventarc Message Bus
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Eventarc Message Bus
---

# Eventarc Message Bus

Eventarc Message Bus is a Google Cloud service that enables event-driven communication between applications and services. It routes events from various sources, such as Cloud Storage, Pub/Sub, or custom sources, to targets like Cloud Run or Workflows. This allows developers to build loosely coupled, scalable systems that react to changes in real time without managing complex integrations.

```
gcp.eventarc_message_bus
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Resource annotations.                                                                                                                                                                                    |
| create_time          | core | timestamp     | Output only. The creation time.                                                                                                                                                                                    |
| crypto_key_name      | core | string        | Optional. Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`.                            |
| datadog_display_name | core | string        |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
| gcp_display_name     | core | string        | Optional. Resource display name.                                                                                                                                                                                   |
| labels               | core | array<string> | Optional. Resource labels.                                                                                                                                                                                         |
| logging_config       | core | json          | Optional. Config to control Platform logging for the Message Bus. This log configuration is applied to the Message Bus itself, and all the Enrollments attached to it.                                             |
| name                 | core | string        | Identifier. Resource name of the form projects/{project}/locations/{location}/messageBuses/{message_bus}                                                                                                           |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.                                                      |
| update_time          | core | timestamp     | Output only. The last-modified time.                                                                                                                                                                               |
| zone_id              | core | string        |
