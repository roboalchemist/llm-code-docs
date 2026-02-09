# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.eventarc_channel_connection.dataset.md

---
title: Eventarc Channel Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Eventarc Channel Connection
---

# Eventarc Channel Connection

Eventarc Channel Connection in Google Cloud is a resource that establishes a link between an event producer and an Eventarc channel. It allows external or internal event sources to send events into Eventarc for routing to supported destinations such as Cloud Run, Workflows, or Cloud Functions. This connection ensures secure and reliable event delivery across services.

```
gcp.eventarc_channel_connection
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| activation_token     | core | string        | Input only. Activation token for the channel. The token will be used during the creation of ChannelConnection to bind the channel with the provider project. This field will not be stored in the provider resource.          |
| ancestors            | core | array<string> |
| channel              | core | string        | Required. The name of the connected subscriber Channel. This is a weak reference to avoid cross project and cross accounts references. This must be in `projects/{project}/location/{location}/channels/{channel_id}` format. |
| create_time          | core | timestamp     | Output only. The creation time.                                                                                                                                                                                               |
| datadog_display_name | core | string        |
| labels               | core | array<string> | Optional. Resource labels.                                                                                                                                                                                                    |
| name                 | core | string        | Required. The name of the connection.                                                                                                                                                                                         |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Server assigned ID of the resource. The server guarantees uniqueness and immutability until deleted.                                                                                                             |
| update_time          | core | timestamp     | Output only. The last-modified time.                                                                                                                                                                                          |
| zone_id              | core | string        |
