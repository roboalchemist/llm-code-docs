# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.eventarc_channel.dataset.md

---
title: Eventarc Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Eventarc Channel
---

# Eventarc Channel

Eventarc Channel in Google Cloud is a resource that connects event providers and event consumers. It acts as a communication path through which events are delivered from sources to destinations such as Cloud Run, Workflows, or Cloud Functions. Channels can be private or public, allowing secure and controlled event routing across projects or organizations.

```
gcp.eventarc_channel
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| activation_token     | core | string        | Output only. The activation token for the channel. The token must be used by the provider to register the channel for publishing.                                                                                                               |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation time.                                                                                                                                                                                                                 |
| crypto_key_name      | core | string        | Optional. Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt their event data. It must match the pattern `projects/*/locations/*/keyRings/*/cryptoKeys/*`.                                                         |
| datadog_display_name | core | string        |
| labels               | core | array<string> | Optional. Resource labels.                                                                                                                                                                                                                      |
| name                 | core | string        | Required. The resource name of the channel. Must be unique within the location on the project and must be in `projects/{project}/locations/{location}/channels/{channel_id}` format.                                                            |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| provider             | core | string        | The name of the event provider (e.g. Eventarc SaaS partner) associated with the channel. This provider will be granted permissions to publish events to the channel. Format: `projects/{project}/locations/{location}/providers/{provider_id}`. |
| pubsub_topic         | core | string        | Output only. The name of the Pub/Sub topic created and managed by Eventarc system as a transport for the event delivery. Format: `projects/{project}/topics/{topic_id}`.                                                                        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzs        | core | bool          | Output only. Whether or not this Channel satisfies the requirements of physical zone separation                                                                                                                                                 |
| state                | core | string        | Output only. The state of a Channel.                                                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. Server assigned unique identifier for the channel. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.                                                                                   |
| update_time          | core | timestamp     | Output only. The last-modified time.                                                                                                                                                                                                            |
| zone_id              | core | string        |
