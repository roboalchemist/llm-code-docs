# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.signalr_service_signalr.dataset.md

---
title: Signalr Service Signalr
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Signalr Service Signalr
---

# Signalr Service Signalr

This table represents the signalr_service_signalr resource from Microsoft Azure.

```gdscript3
azure.signalr_service_signalr
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ----------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| cors                          | core | json       |
| disable_aad_auth              | core | bool       | DisableLocalAuthEnable or disable aad authWhen set as true, connection with AuthType=aad won't work.                                                                                                                                                                                                                                                                                          |
| disable_local_auth            | core | bool       | DisableLocalAuthEnable or disable local auth with AccessKeyWhen set as true, connection with AccessKey=xxx won't work.                                                                                                                                                                                                                                                                        |
| external_ip                   | core | string     | The publicly accessible IP of the resource.                                                                                                                                                                                                                                                                                                                                                   |
| features                      | core | json       | List of the featureFlags.FeatureFlags that are not included in the parameters for the update operation will not be modified.And the response will only include featureFlags that are explicitly set. When a featureFlag is not explicitly set, its globally default value will be usedBut keep in mind, the default value doesn't mean "false". It varies in terms of different FeatureFlags. |
| host_name                     | core | string     | FQDN of the service instance.                                                                                                                                                                                                                                                                                                                                                                 |
| host_name_prefix              | core | string     | Deprecated.                                                                                                                                                                                                                                                                                                                                                                                   |
| id                            | core | string     | Fully qualified resource Id for the resource.                                                                                                                                                                                                                                                                                                                                                 |
| identity                      | core | json       |
| kind                          | core | string     |
| live_trace_configuration      | core | json       |
| location                      | core | string     | The GEO location of the resource. e.g. West US | East US | North Central US | South Central US.                                                                                                                                                                                                                                                                                               |
| name                          | core | string     | The name of the resource.                                                                                                                                                                                                                                                                                                                                                                     |
| network_ac_ls                 | core | json       |
| private_endpoint_connections  | core | json       | Private endpoint connections to the resource.                                                                                                                                                                                                                                                                                                                                                 |
| provisioning_state            | core | string     |
| public_network_access         | core | string     | Enable or disable public network access. Default to "Enabled".When it's Enabled, network ACLs still apply.When it's Disabled, public network access is always disabled no matter what you set in network ACLs.                                                                                                                                                                                |
| public_port                   | core | int64      | The publicly accessible port of the resource which is designed for browser/client side usage.                                                                                                                                                                                                                                                                                                 |
| resource_group                | core | string     |
| resource_log_configuration    | core | json       |
| server_port                   | core | int64      | The publicly accessible port of the resource which is designed for customer server side usage.                                                                                                                                                                                                                                                                                                |
| serverless                    | core | json       |
| shared_private_link_resources | core | json       | The list of shared private link resources.                                                                                                                                                                                                                                                                                                                                                    |
| sku                           | core | json       |
| subscription_id               | core | string     |
| subscription_name             | core | string     |
| system_data                   | core | json       |
| tags                          | core | hstore_csv |
| tls                           | core | json       |
| type                          | core | string     | The type of the resource - e.g. "Microsoft.SignalRService/SignalR"                                                                                                                                                                                                                                                                                                                            |
| upstream                      | core | json       |
| version                       | core | string     | Version of the resource. Probably you need the same or higher version of client SDKs.                                                                                                                                                                                                                                                                                                         |
