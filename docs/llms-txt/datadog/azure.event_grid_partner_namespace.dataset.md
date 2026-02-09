# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.event_grid_partner_namespace.dataset.md

---
title: Event Grid Partner Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Grid Partner Namespace
---

# Event Grid Partner Namespace

This table represents the event_grid_partner_namespace resource from Microsoft Azure.

```
azure.event_grid_partner_namespace
```

## Fields

| Title                                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                      | Description |
| --------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                    | core | string     |
| activation_state                        | core | string     | Activation state of the partner topic.                                                                                                                                                                                                                                                         |
| disable_local_auth                      | core | bool       | This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace.                                                                            |
| endpoint                                | core | string     | Endpoint for the partner namespace.                                                                                                                                                                                                                                                            |
| event_type_info                         | core | json       | Event Type information from the corresponding event channel.                                                                                                                                                                                                                                   |
| expiration_time_if_not_activated_utc    | core | string     | Expiration time of the partner topic. If this timer expires while the partner topic is still never activated,the partner topic and corresponding event channel are deleted.                                                                                                                    |
| id                                      | core | string     | Fully qualified identifier of the resource.                                                                                                                                                                                                                                                    |
| identity                                | core | json       | Identity information for the Partner Topic resource.                                                                                                                                                                                                                                           |
| inbound_ip_rules                        | core | json       | This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.                                                                                                                                                  |
| location                                | core | string     | Location of the resource.                                                                                                                                                                                                                                                                      |
| message_for_activation                  | core | string     | Context or helpful message that can be used during the approval process by the subscriber.                                                                                                                                                                                                     |
| name                                    | core | string     | Name of the resource.                                                                                                                                                                                                                                                                          |
| partner_registration_fully_qualified_id | core | string     | The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}. |
| partner_registration_immutable_id       | core | string     | The immutableId of the corresponding partner registration.                                                                                                                                                                                                                                     |
| partner_topic_friendly_description      | core | string     | Friendly description about the topic. This can be set by the publisher/partner to show custom description for the customer partner topic.This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.                                         |
| partner_topic_routing_mode              | core | string     | This determines if events published to this partner namespace should use the source attribute in the event payloador use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic.            |
| private_endpoint_connections            | core | json       |
| provisioning_state                      | core | string     | Provisioning state of the partner topic.                                                                                                                                                                                                                                                       |
| public_network_access                   | core | string     | This determines if traffic is allowed over public network. By default it is enabled.You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" />                            |
| resource_group                          | core | string     |
| subscription_id                         | core | string     |
| subscription_name                       | core | string     |
| system_data                             | core | json       | The system metadata relating to Partner Topic resource.                                                                                                                                                                                                                                        |
| tags                                    | core | hstore_csv |
| type                                    | core | string     | Type of the resource.                                                                                                                                                                                                                                                                          |
