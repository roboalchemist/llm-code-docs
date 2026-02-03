# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_application_gateway.dataset.md

---
title: Application Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Application Gateway
---

# Application Gateway

Application Gateway in Azure is a web traffic load balancer that manages and distributes incoming application traffic across multiple servers. It operates at the application layer (OSI layer 7) and provides features such as SSL termination, URL-based routing, session affinity, and Web Application Firewall (WAF) integration. This helps improve application performance, security, and scalability by intelligently routing requests based on content and ensuring high availability of web applications.

```
azure.network_application_gateway
```

## Fields

| Title                             | ID   | Type          | Data Type                                                                                                                                                                                                       | Description |
| --------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string        |
| autoscale_configuration           | core | json          | Application Gateway autoscale configuration.                                                                                                                                                                    |
| backend_address_pools             | core | json          | Backend address pool of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).  |
| custom_error_configurations       | core | json          | Custom error configurations of the application gateway resource.                                                                                                                                                |
| enable_fips                       | core | bool          | Whether FIPS is enabled on the application gateway resource.                                                                                                                                                    |
| enable_http2                      | core | bool          | Whether HTTP2 is enabled on the application gateway resource.                                                                                                                                                   |
| etag                              | core | string        | A unique read-only string that changes whenever the resource is updated.                                                                                                                                        |
| firewall_policy                   | core | json          | Reference to another subresource.                                                                                                                                                                               |
| force_firewall_policy_association | core | bool          | If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config.                                                                                    |
| frontend_ip_configurations        | core | json          | Frontend IP addresses of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits). |
| frontend_ports                    | core | json          | Frontend ports of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).        |
| gateway_ip_configurations         | core | json          | Subnets of the application gateway resource. For default limits, see [Application Gateway limits](https://docs.microsoft.com/azure/azure-subscription-service-limits#application-gateway-limits).               |
| global_configuration              | core | json          | Application Gateway global configuration.                                                                                                                                                                       |
| id                                | core | string        | Resource ID.                                                                                                                                                                                                    |
| identity                          | core | json          | Identity for the resource.                                                                                                                                                                                      |
| location                          | core | string        | Resource location.                                                                                                                                                                                              |
| name                              | core | string        | Resource name.                                                                                                                                                                                                  |
| operational_state                 | core | string        | Operational state of the application gateway resource.                                                                                                                                                          |
| provisioning_state                | core | string        | The current provisioning state.                                                                                                                                                                                 |
| resource_group                    | core | string        |
| resource_guid                     | core | string        | The resource GUID property of the application gateway resource.                                                                                                                                                 |
| sku                               | core | json          | SKU of an application gateway.                                                                                                                                                                                  |
| ssl_policy                        | core | json          | Application Gateway Ssl policy.                                                                                                                                                                                 |
| subscription_id                   | core | string        |
| subscription_name                 | core | string        |
| tags                              | core | hstore_csv    |
| type                              | core | string        | Resource type.                                                                                                                                                                                                  |
| zones                             | core | array<string> | A list of availability zones denoting where the resource needs to come from.                                                                                                                                    |
