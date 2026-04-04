# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.application_insights_component.dataset.md

---
title: Application Insights Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Application Insights Component
---

# Application Insights Component

This table represents the Application Insights Component resource from Microsoft Azure.

```
azure.application_insights_component
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                                                                                                                                                     | Description |
| ----------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| app_id                              | core | string     | Application Insights Unique ID for your Application.                                                                                                                                                                                          |
| application_id                      | core | string     | The unique ID of your application. This field mirrors the 'Name' field and cannot be changed.                                                                                                                                                 |
| application_type                    | core | string     | Type of application being monitored.                                                                                                                                                                                                          |
| connection_string                   | core | string     | Application Insights component connection string.                                                                                                                                                                                             |
| creation_date                       | core | string     | Creation Date for the Application Insights component, in ISO 8601 format.                                                                                                                                                                     |
| disable_ip_masking                  | core | bool       | Disable IP masking.                                                                                                                                                                                                                           |
| disable_local_auth                  | core | bool       | Disable Non-AAD based Auth.                                                                                                                                                                                                                   |
| etag                                | core | string     | Resource etag                                                                                                                                                                                                                                 |
| flow_type                           | core | string     | Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API.                                                   |
| force_customer_storage_for_profiler | core | bool       | Force users to create their own storage account for profiler and debugger.                                                                                                                                                                    |
| hockey_app_id                       | core | string     | The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp.                                                                                                                       |
| id                                  | core | string     | Azure resource Id                                                                                                                                                                                                                             |
| immediate_purge_data_on30_days      | core | bool       | Purge data immediately after 30 days.                                                                                                                                                                                                         |
| ingestion_mode                      | core | string     | Indicates the flow of the ingestion.                                                                                                                                                                                                          |
| kind                                | core | string     | The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone.                                           |
| la_migration_date                   | core | string     | The date which the component got migrated to LA, in ISO 8601 format.                                                                                                                                                                          |
| location                            | core | string     | Resource location                                                                                                                                                                                                                             |
| name                                | core | string     | Application name.                                                                                                                                                                                                                             |
| private_link_scoped_resources       | core | json       | List of linked private link scope resources.                                                                                                                                                                                                  |
| provisioning_state                  | core | string     | Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed. |
| public_network_access_for_ingestion | core | string     | The network access type for accessing Application Insights ingestion.                                                                                                                                                                         |
| public_network_access_for_query     | core | string     | The network access type for accessing Application Insights query.                                                                                                                                                                             |
| request_source                      | core | string     | Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'.                                                                                                              |
| resource_group                      | core | string     |
| retention_in_days                   | core | int64      | Retention period in days.                                                                                                                                                                                                                     |
| sampling_percentage                 | core | float64    | Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry.                                                                                                                  |
| subscription_id                     | core | string     |
| subscription_name                   | core | string     |
| tags                                | core | hstore_csv |
| tenant_id                           | core | string     | Azure Tenant Id.                                                                                                                                                                                                                              |
| type                                | core | string     | Azure resource type                                                                                                                                                                                                                           |
| workspace_resource_id               | core | string     | Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property.                        |
