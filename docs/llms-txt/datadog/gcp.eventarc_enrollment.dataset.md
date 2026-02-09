# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.eventarc_enrollment.dataset.md

---
title: Eventarc Enrollment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Eventarc Enrollment
---

# Eventarc Enrollment

Eventarc Enrollment in Google Cloud enables services to receive and react to events from various sources across GCP and external systems. It connects event producers and consumers through a standardized eventing framework, allowing event-driven architectures without complex integrations. This resource manages the configuration and registration of event sources and destinations.

```
gcp.eventarc_enrollment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Resource annotations.                                                                                                                                                                                    |
| cel_match            | core | string        | Required. A CEL expression identifying which messages this enrollment applies to.                                                                                                                                  |
| create_time          | core | timestamp     | Output only. The creation time.                                                                                                                                                                                    |
| datadog_display_name | core | string        |
| destination          | core | string        | Required. Destination is the Pipeline that the Enrollment is delivering to. It must point to the full resource name of a Pipeline. Format: "projects/{PROJECT_ID}/locations/{region}/pipelines/{PIPELINE_ID)"      |
| etag                 | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
| gcp_display_name     | core | string        | Optional. Resource display name.                                                                                                                                                                                   |
| labels               | core | array<string> | Optional. Resource labels.                                                                                                                                                                                         |
| message_bus          | core | string        | Required. Immutable. Resource name of the message bus identifying the source of the messages. It matches the form projects/{project}/locations/{location}/messageBuses/{messageBus}.                               |
| name                 | core | string        | Identifier. Resource name of the form projects/{project}/locations/{location}/enrollments/{enrollment}                                                                                                             |
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
