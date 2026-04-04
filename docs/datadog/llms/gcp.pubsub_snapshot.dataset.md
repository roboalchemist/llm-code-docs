# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.pubsub_snapshot.dataset.md

---
title: Pub/Sub Snapshot
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pub/Sub Snapshot
---

# Pub/Sub Snapshot

A Pub/Sub Snapshot in Google Cloud is a point-in-time copy of a subscription's message backlog. It allows you to preserve unacknowledged messages so that you can replay them later by seeking a subscription to the snapshot. This is useful for recovering from errors, testing, or reprocessing data without losing messages.

```
gcp.pubsub_snapshot
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| expire_time          | core | timestamp     | Optional. The snapshot is guaranteed to exist up until this time. A newly-created snapshot expires no later than 7 days from the time of its creation. Its exact lifetime is determined at creation by the existing backlog in the source subscription. Specifically, the lifetime of the snapshot is `7 days - (age of oldest unacked message in the subscription)`. For example, consider a subscription whose oldest unacked message is 3 days old. If a snapshot is created from this subscription, the snapshot -- which will always capture this 3-day-old backlog as long as the snapshot exists -- will expire in 4 days. The service will refuse to create a snapshot that would expire in less than 1 hour after creation. |
| labels               | core | array<string> | Optional. See [Creating and managing labels] (https://cloud.google.com/pubsub/docs/labels).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| name                 | core | string        | Optional. The name of the snapshot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| topic                | core | string        | Optional. The name of the topic from which this snapshot is retaining messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| zone_id              | core | string        |
