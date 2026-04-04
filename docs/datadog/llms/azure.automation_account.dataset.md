# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.automation_account.dataset.md

---
title: Automation Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Automation Account
---

# Automation Account

An Azure Automation Account is a cloud resource that provides a central place to manage automation tasks such as process automation, configuration management, and update management. It allows you to create and run runbooks, manage resources across Azure and hybrid environments, and reduce manual effort by automating repetitive tasks.

```
azure.automation_account
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                             | Description |
| ----------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| automation_hybrid_service_url | core | string     | URL of automation hybrid service which is used for hybrid worker on-boarding.                         |
| creation_time                 | core | string     | Gets the creation time.                                                                               |
| description                   | core | string     | Gets or sets the description.                                                                         |
| disable_local_auth            | core | bool       | Indicates whether requests using non-AAD authentication are blocked                                   |
| etag                          | core | string     | Gets or sets the etag of the resource.                                                                |
| id                            | core | string     | Fully qualified resource Id for the resource                                                          |
| identity                      | core | json       | Identity for the resource.                                                                            |
| last_modified_by              | core | string     | Gets or sets the last modified by.                                                                    |
| last_modified_time            | core | string     | Gets the last modified time.                                                                          |
| location                      | core | string     | The Azure Region where the resource lives                                                             |
| name                          | core | string     | The name of the resource                                                                              |
| private_endpoint_connections  | core | json       | List of Automation operations supported by the Automation resource provider.                          |
| public_network_access         | core | bool       | Indicates whether traffic on the non-ARM endpoint (Webhook/Agent) is allowed from the public internet |
| resource_group                | core | string     |
| sku                           | core | json       | The account SKU.                                                                                      |
| state                         | core | string     | Gets status of account.                                                                               |
| subscription_id               | core | string     |
| subscription_name             | core | string     |
| system_data                   | core | json       | Metadata pertaining to creation and last modification of the resource.                                |
| tags                          | core | hstore_csv |
| type                          | core | string     | The type of the resource.                                                                             |
