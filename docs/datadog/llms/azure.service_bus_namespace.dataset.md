# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.service_bus_namespace.dataset.md

---
title: Service Bus Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Bus Namespace
---

# Service Bus Namespace

This table represents the service_bus_namespace resource from Microsoft Azure.

```
azure.service_bus_namespace
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                               | Description |
| ---------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| alternate_name               | core | string     | Alternate name for namespace                                                                            |
| created_at                   | core | string     | The time the namespace was created                                                                      |
| disable_local_auth           | core | bool       | This property disables SAS authentication for the Service Bus namespace.                                |
| encryption                   | core | json       | Properties of BYOK Encryption description                                                               |
| id                           | core | string     | Resource Id                                                                                             |
| identity                     | core | json       | Properties of BYOK Identity description                                                                 |
| location                     | core | string     | The Geo-location where the resource lives                                                               |
| metric_id                    | core | string     | Identifier for Azure Insights metrics                                                                   |
| name                         | core | string     | Resource name                                                                                           |
| private_endpoint_connections | core | json       | List of private endpoint connections.                                                                   |
| provisioning_state           | core | string     | Provisioning state of the namespace.                                                                    |
| resource_group               | core | string     |
| service_bus_endpoint         | core | string     | Endpoint you can use to perform Service Bus operations.                                                 |
| sku                          | core | json       | Properties of SKU                                                                                       |
| status                       | core | string     | Status of the namespace.                                                                                |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| system_data                  | core | json       | The system meta data relating to this resource.                                                         |
| tags                         | core | hstore_csv |
| type                         | core | string     | Resource type                                                                                           |
| updated_at                   | core | string     | The time the namespace was updated.                                                                     |
| zone_redundant               | core | bool       | Enabling this property creates a Premium Service Bus Namespace in regions supported availability zones. |
