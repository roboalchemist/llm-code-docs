# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.event_grid_topic.dataset.md

---
title: Event Grid Topic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Grid Topic
---

# Event Grid Topic

This table represents the event_grid_topic resource from Microsoft Azure.

```
azure.event_grid_topic
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                                                 | Description |
| ---------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| data_residency_boundary      | core | string     | Data Residency Boundary of the resource.                                                                                                                                                                                                                  |
| disable_local_auth           | core | bool       | This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the topic.                                                   |
| endpoint                     | core | string     | Endpoint for the topic.                                                                                                                                                                                                                                   |
| id                           | core | string     | Fully qualified identifier of the resource.                                                                                                                                                                                                               |
| identity                     | core | json       | Identity information for the resource.                                                                                                                                                                                                                    |
| inbound_ip_rules             | core | json       | This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.                                                                                                             |
| input_schema                 | core | string     | This determines the format that Event Grid should expect for incoming events published to the topic.                                                                                                                                                      |
| input_schema_mapping         | core | json       | This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.                                                      |
| location                     | core | string     | Location of the resource.                                                                                                                                                                                                                                 |
| metric_resource_id           | core | string     | Metric resource id for the topic.                                                                                                                                                                                                                         |
| name                         | core | string     | Name of the resource.                                                                                                                                                                                                                                     |
| private_endpoint_connections | core | json       |
| provisioning_state           | core | string     | Provisioning state of the topic.                                                                                                                                                                                                                          |
| public_network_access        | core | string     | This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" /> |
| resource_group               | core | string     |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| system_data                  | core | json       | The system metadata relating to Topic resource.                                                                                                                                                                                                           |
| tags                         | core | hstore_csv |
| type                         | core | string     | Type of the resource.                                                                                                                                                                                                                                     |
