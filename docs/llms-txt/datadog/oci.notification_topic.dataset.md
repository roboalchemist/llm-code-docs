# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.notification_topic.dataset.md

---
title: Notification Topic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Notification Topic
---

# Notification Topic

A Notification Topic in Oracle Cloud Infrastructure (OCI) is a communication channel used to broadcast messages to multiple subscribers. It enables event-driven messaging by allowing services or applications to publish messages that are then delivered to subscribed endpoints such as email, functions, or HTTPS endpoints. This helps decouple components and ensures reliable, scalable message distribution.

```
oci.notification_topic
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                 | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| api_endpoint       | core | string     | The value to assign to the api_endpoint property of this NotificationTopicSummary.                                                                                                                                                                                        |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                     |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                         |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                           |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this NotificationTopicSummary.                                                                                                                                                                                      |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                  |
| description        | core | string     | The value to assign to the description property of this NotificationTopicSummary.                                                                                                                                                                                         |
| etag               | core | string     | The value to assign to the etag property of this NotificationTopicSummary.                                                                                                                                                                                                |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this NotificationTopicSummary.                                                                                                                                                                                       |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this NotificationTopicSummary. Allowed values for this property are: "ACTIVE", "DELETING", "CREATING", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The value to assign to the name property of this NotificationTopicSummary.                                                                                                                                                                                                |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                  |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                            |
| short_topic_id     | core | string     | The value to assign to the short_topic_id property of this NotificationTopicSummary.                                                                                                                                                                                      |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this NotificationTopicSummary.                                                                                                                                                                                        |
| topic_id           | core | string     | The value to assign to the topic_id property of this NotificationTopicSummary.                                                                                                                                                                                            |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                    |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                    |
