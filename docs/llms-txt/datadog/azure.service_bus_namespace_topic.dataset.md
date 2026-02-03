# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.service_bus_namespace_topic.dataset.md

---
title: Service Bus Namespace Topic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Bus Namespace Topic
---

# Service Bus Namespace Topic

This table represents the service_bus_namespace_topic resource from Microsoft Azure.

```
azure.service_bus_namespace_topic
```

## Fields

| Title                                   | ID   | Type       | Data Type                                                                                                                                                                                                                                    | Description |
| --------------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                    | core | string     |
| accessed_at                             | core | string     | Last time the message was sent, or a request was received, for this topic.                                                                                                                                                                   |
| auto_delete_on_idle                     | core | string     | ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.                                                                                                                           |
| count_details                           | core | json       | Message count details                                                                                                                                                                                                                        |
| created_at                              | core | string     | Exact time the message was created.                                                                                                                                                                                                          |
| default_message_time_to_live            | core | string     | ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |
| duplicate_detection_history_time_window | core | string     | ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.                                                                                                                    |
| enable_batched_operations               | core | bool       | Value that indicates whether server-side batched operations are enabled.                                                                                                                                                                     |
| enable_express                          | core | bool       | Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.                                                                                   |
| enable_partitioning                     | core | bool       | Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.                                                                                                                                         |
| id                                      | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                    |
| location                                | core | string     | The geo-location where the resource lives                                                                                                                                                                                                    |
| max_message_size_in_kilobytes           | core | int64      | Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.                                                                                              |
| max_size_in_megabytes                   | core | int64      | Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.                                                                                                                            |
| name                                    | core | string     | The name of the resource                                                                                                                                                                                                                     |
| requires_duplicate_detection            | core | bool       | Value indicating if this topic requires duplicate detection.                                                                                                                                                                                 |
| resource_group                          | core | string     |
| size_in_bytes                           | core | int64      | Size of the topic, in bytes.                                                                                                                                                                                                                 |
| status                                  | core | string     | Enumerates the possible values for the status of a messaging entity.                                                                                                                                                                         |
| subscription_count                      | core | int64      | Number of subscriptions.                                                                                                                                                                                                                     |
| subscription_id                         | core | string     |
| subscription_name                       | core | string     |
| support_ordering                        | core | bool       | Value that indicates whether the topic supports ordering.                                                                                                                                                                                    |
| system_data                             | core | json       | The system meta data relating to this resource.                                                                                                                                                                                              |
| tags                                    | core | hstore_csv |
| type                                    | core | string     | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"                                                                                                                                  |
| updated_at                              | core | string     | The exact time the message was updated.                                                                                                                                                                                                      |
