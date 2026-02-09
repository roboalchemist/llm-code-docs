# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.servicediscovery_service.dataset.md

---
title: Cloud Map Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Map Service
---

# Cloud Map Service

Cloud Map Service in AWS Service Discovery lets you create and manage custom names for your application resources. It provides a registry where services can be discovered dynamically by other applications using DNS or API calls. This helps with service-to-service communication, automatic discovery, and health-aware routing without hardcoding endpoints.

```
aws.servicediscovery_service
```

## Fields

| Title                      | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                    | Description |
| -------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string     |
| account_id                 | core | string     |
| arn                        | core | string     | The Amazon Resource Name (ARN) that Cloud Map assigns to the service when you create it.                                                                                                                                                                                                                                     |
| create_date                | core | timestamp  | The date and time that the service was created, in Unix format and Coordinated Universal Time (UTC). The value of CreateDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.                                                                         |
| creator_request_id         | core | string     | A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. CreatorRequestId can be any unique string (for example, a date/timestamp).                                                                                                        |
| description                | core | string     | The description of the service.                                                                                                                                                                                                                                                                                              |
| dns_config                 | core | json       | A complex type that contains information about the Route 53 DNS records that you want Cloud Map to create when you register an instance. The record types of a service can only be changed by deleting the service and recreating it with a new Dnsconfig.                                                                   |
| health_check_config        | core | json       | Public DNS and HTTP namespaces only. A complex type that contains settings for an optional health check. If you specify settings for a health check, Cloud Map associates the health check with the records that you specify in DnsConfig. For information about the charges for health checks, see Amazon Route 53 Pricing. |
| health_check_custom_config | core | json       | A complex type that contains information about an optional custom health check. If you specify a health check configuration, you can specify either HealthCheckCustomConfig or HealthCheckConfig but not both.                                                                                                               |
| id                         | core | string     | The ID that Cloud Map assigned to the service when you created it.                                                                                                                                                                                                                                                           |
| instance_count             | core | int64      | The number of instances that are currently associated with the service. Instances that were previously associated with the service but that are deleted aren't included in the count. The count might not reflect pending registrations and deregistrations.                                                                 |
| name                       | core | string     | The name of the service.                                                                                                                                                                                                                                                                                                     |
| namespace_id               | core | string     | The ID of the namespace that was used to create the service.                                                                                                                                                                                                                                                                 |
| tags                       | core | hstore_csv |
| type                       | core | string     | Describes the systems that can be used to discover the service instances. DNS_HTTP The service instances can be discovered using either DNS queries or the DiscoverInstances API operation. HTTP The service instances can only be discovered using the DiscoverInstances API operation. DNS Reserved.                       |
