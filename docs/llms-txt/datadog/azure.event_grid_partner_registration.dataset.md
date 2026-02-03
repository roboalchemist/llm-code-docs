# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.event_grid_partner_registration.dataset.md

---
title: Event Grid Partner Registration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Event Grid Partner Registration
---

# Event Grid Partner Registration

This table represents the event_grid_partner_registration resource from Microsoft Azure.

```
azure.event_grid_partner_registration
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                 | Description |
| --------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| id                                | core | string     | Fully qualified identifier of the resource.                                                                                                               |
| location                          | core | string     | Location of the resource.                                                                                                                                 |
| name                              | core | string     | Name of the resource.                                                                                                                                     |
| partner_registration_immutable_id | core | string     | The immutableId of the corresponding partner registration.Note: This property is marked for deprecation and is not supported in any future GA API version |
| provisioning_state                | core | string     | Provisioning state of the partner registration.                                                                                                           |
| resource_group                    | core | string     |
| subscription_id                   | core | string     |
| subscription_name                 | core | string     |
| system_data                       | core | json       | The system metadata relating to Partner Registration resource.                                                                                            |
| tags                              | core | hstore_csv |
| type                              | core | string     | Type of the resource.                                                                                                                                     |
