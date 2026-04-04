# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.app_service_plan.dataset.md

---
title: App Service Plan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Service Plan
---

# App Service Plan

This table represents the App Service Plan resource from Microsoft Azure.

```
azure.app_service_plan
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                       | Description |
| ---------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| extended_location            | core | json       |
| free_offer_expiration_time   | core | string     | The time when the server farm free offer expires.                                                                                                                                               |
| geo_region                   | core | string     | Geographical location for the App Service plan.                                                                                                                                                 |
| hosting_environment_profile  | core | json       | Specification for the App Service Environment to use for the App Service plan.                                                                                                                  |
| hyper_v                      | core | bool       | If Hyper-V container app service plan <code>true</code>, <code>false</code> otherwise.                                                                                                          |
| id                           | core | string     | Resource Id.                                                                                                                                                                                    |
| is_spot                      | core | bool       | If <code>true</code>, this App Service Plan owns spot instances.                                                                                                                                |
| is_xenon                     | core | bool       | Obsolete: If Hyper-V container app service plan <code>true</code>, <code>false</code> otherwise.                                                                                                |
| kind                         | core | string     | Kind of resource.                                                                                                                                                                               |
| kube_environment_profile     | core | json       | Specification for the Kubernetes Environment to use for the App Service plan.                                                                                                                   |
| location                     | core | string     | Resource Location.                                                                                                                                                                              |
| maximum_elastic_worker_count | core | int64      | Maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan                                                                                                           |
| maximum_number_of_workers    | core | int64      | Maximum number of instances that can be assigned to this App Service plan.                                                                                                                      |
| name                         | core | string     | Resource Name.                                                                                                                                                                                  |
| number_of_sites              | core | int64      | Number of apps assigned to this App Service plan.                                                                                                                                               |
| per_site_scaling             | core | bool       | If <code>true</code>, apps assigned to this App Service plan can be scaled independently.If <code>false</code>, apps assigned to this App Service plan will scale to all instances of the plan. |
| provisioning_state           | core | string     | Provisioning state of the App Service Plan.                                                                                                                                                     |
| reserved                     | core | bool       | If Linux app service plan <code>true</code>, <code>false</code> otherwise.                                                                                                                      |
| resource_group               | core | string     |
| sku_capacity                 | core | int64      |
| sku_family                   | core | string     |
| sku_name                     | core | string     |
| sku_size                     | core | string     |
| sku_tier                     | core | string     |
| spot_expiration_time         | core | string     | The time when the server farm expires. Valid only if it is a spot server farm.                                                                                                                  |
| status                       | core | string     | App Service plan status.                                                                                                                                                                        |
| subscription                 | core | string     | App Service plan subscription.                                                                                                                                                                  |
| subscription_id              | core | string     |
| subscription_name            | core | string     |
| tags                         | core | hstore_csv |
| target_worker_count          | core | int64      | Scaling worker count.                                                                                                                                                                           |
| target_worker_size_id        | core | int64      | Scaling worker size ID.                                                                                                                                                                         |
| type                         | core | string     | Resource type.                                                                                                                                                                                  |
| worker_tier_name             | core | string     | Target worker tier assigned to the App Service plan.                                                                                                                                            |
