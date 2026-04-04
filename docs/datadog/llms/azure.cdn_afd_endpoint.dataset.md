# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.cdn_afd_endpoint.dataset.md

---
title: Azure Front Door Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Front Door Endpoint
---

# Azure Front Door Endpoint

Azure Front Door Endpoint is a globally distributed entry point for delivering web applications with high availability and performance. It provides intelligent traffic routing, SSL termination, and application acceleration by leveraging Microsoft's global edge network. This resource enables secure, fast, and scalable delivery of web content to users worldwide.

```
azure.cdn_afd_endpoint
```

## Fields

| Title                                  | ID   | Type       | Data Type                                                                                        | Description |
| -------------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key                                   | core | string     |
| auto_generated_domain_name_label_scope | core | string     | Indicates the endpoint name reuse scope. The default value is TenantReuse.                       |
| deployment_status                      | core | string     |
| enabled_state                          | core | string     | Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'                 |
| host_name                              | core | string     | The host name of the endpoint structured as {endpointName}.{DNSZone}, e.g. contoso.azureedge.net |
| id                                     | core | string     | Resource ID.                                                                                     |
| location                               | core | string     | Resource location.                                                                               |
| name                                   | core | string     | Resource name.                                                                                   |
| profile_name                           | core | string     | The name of the profile which holds the endpoint.                                                |
| provisioning_state                     | core | string     | Provisioning status                                                                              |
| resource_group                         | core | string     |
| subscription_id                        | core | string     |
| subscription_name                      | core | string     |
| system_data                            | core | json       | Read only system data                                                                            |
| tags                                   | core | hstore_csv |
| type                                   | core | string     | Resource type.                                                                                   |
