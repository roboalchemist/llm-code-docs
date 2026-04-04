# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.service_bus_namespace_queue.dataset.md

---
title: Service Bus Namespace Queue
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Bus Namespace Queue
---

# Service Bus Namespace Queue

This table represents the service_bus_namespace_queue resource from Microsoft Azure.

```
azure.service_bus_namespace_queue
```

## Fields

| Title                                   | ID   | Type       | Data Type                                                                                                                                                                                                                                    | Description |
| --------------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                    | core | string     |
| accessed_at                             | core | string     | Last time a message was sent, or the last time there was a receive request to this queue.                                                                                                                                                    |
| auto_delete_on_idle                     | core | string     | ISO 8061 timeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.                                                                                                                           |
| count_details                           | core | json       | Message Count Details.                                                                                                                                                                                                                       |
| created_at                              | core | string     | The exact time the message was created.                                                                                                                                                                                                      |
| dead_lettering_on_message_expiration    | core | bool       | A value that indicates whether this queue has dead letter support when a message expires.                                                                                                                                                    |
| default_message_time_to_live            | core | string     | ISO 8601 default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |
| duplicate_detection_history_time_window | core | string     | ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.                                                                                                                   |
| enable_batched_operations               | core | bool       | Value that indicates whether server-side batched operations are enabled.                                                                                                                                                                     |
| enable_express                          | core | bool       | A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.                                                                                 |
| enable_partitioning                     | core | bool       | A value that indicates whether the queue is to be partitioned across multiple message brokers.                                                                                                                                               |
| forward_dead_lettered_messages_to       | core | string     | Queue/Topic name to forward the Dead Letter message                                                                                                                                                                                          |
| forward_to                              | core | string     | Queue/Topic name to forward the messages                                                                                                                                                                                                     |
| id                                      | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                    |
| location                                | core | string     | The geo-location where the resource lives                                                                                                                                                                                                    |
| lock_duration                           | core | string     | ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.                                       |
| max_delivery_count                      | core | int64      | The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.                                                                                                                    |
| max_message_size_in_kilobytes           | core | int64      | Maximum size (in KB) of the message payload that can be accepted by the queue. This property is only used in Premium today and default is 1024.                                                                                              |
| max_size_in_megabytes                   | core | int64      | The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. Default is 1024.                                                                                                                            |
| message_count                           | core | int64      | The number of messages in the queue.                                                                                                                                                                                                         |
| name                                    | core | string     | The name of the resource                                                                                                                                                                                                                     |
| requires_duplicate_detection            | core | bool       | A value indicating if this queue requires duplicate detection.                                                                                                                                                                               |
| requires_session                        | core | bool       | A value that indicates whether the queue supports the concept of sessions.                                                                                                                                                                   |
| resource_group                          | core | string     |
| size_in_bytes                           | core | int64      | The size of the queue, in bytes.                                                                                                                                                                                                             |
| status                                  | core | string     | Enumerates the possible values for the status of a messaging entity.                                                                                                                                                                         |
| subscription_id                         | core | string     |
| subscription_name                       | core | string     |
| system_data                             | core | json       | The system meta data relating to this resource.                                                                                                                                                                                              |
| tags                                    | core | hstore_csv |
| type                                    | core | string     | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"                                                                                                                                  |
| updated_at                              | core | string     | The exact time the message was updated.                                                                                                                                                                                                      |
