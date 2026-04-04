# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.event_grid_partner_topic.dataset.md

---
title: Event Grid Partner Topic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Grid Partner Topic
---

# Event Grid Partner Topic

This table represents the event_grid_partner_topic resource from Microsoft Azure.

```
azure.event_grid_partner_topic
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                                                                                              | Description |
| ------------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                 | core | string     |
| activation_state                     | core | string     | Activation state of the partner topic.                                                                                                                                                                                                                 |
| event_type_info                      | core | json       | Event Type information from the corresponding event channel.                                                                                                                                                                                           |
| expiration_time_if_not_activated_utc | core | string     | Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,the partner topic and corresponding event channel are deleted.                                                                            |
| id                                   | core | string     | Fully qualified identifier of the resource.                                                                                                                                                                                                            |
| identity                             | core | json       | Identity information for the Partner Topic resource.                                                                                                                                                                                                   |
| location                             | core | string     | Location of the resource.                                                                                                                                                                                                                              |
| message_for_activation               | core | string     | Context or helpful message that can be used during the approval process by the subscriber.                                                                                                                                                             |
| name                                 | core | string     | Name of the resource.                                                                                                                                                                                                                                  |
| partner_registration_immutable_id    | core | string     | The immutableId of the corresponding partner registration.                                                                                                                                                                                             |
| partner_topic_friendly_description   | core | string     | Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer. |
| provisioning_state                   | core | string     | Provisioning state of the partner topic.                                                                                                                                                                                                               |
| resource_group                       | core | string     |
| subscription_id                      | core | string     |
| subscription_name                    | core | string     |
| system_data                          | core | json       | The system metadata relating to Partner Topic resource.                                                                                                                                                                                                |
| tags                                 | core | hstore_csv |
| type                                 | core | string     | Type of the resource.                                                                                                                                                                                                                                  |
