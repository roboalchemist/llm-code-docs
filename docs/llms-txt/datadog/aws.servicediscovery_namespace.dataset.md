# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.servicediscovery_namespace.dataset.md

---
title: Cloud Map Namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Map Namespace
---

# Cloud Map Namespace

Cloud Map Namespace in AWS is a logical container for service discovery resources. It defines a naming boundary where services can be registered and discovered by applications. Namespaces can be public or private, allowing services to be resolved either within a VPC or over the internet. This enables dynamic service discovery without hardcoding endpoints.

```
aws.servicediscovery_namespace
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) that Cloud Map assigns to the namespace when you create it.                                                                                                                                                                                                                                                                                                                             |
| create_date        | core | timestamp  | The date that the namespace was created, in Unix date/time format and Coordinated Universal Time (UTC). The value of CreateDate is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.                                                                                                                                                                |
| creator_request_id | core | string     | A unique string that identifies the request and that allows failed requests to be retried without the risk of running an operation twice.                                                                                                                                                                                                                                                                              |
| description        | core | string     | The description that you specify for the namespace when you create it.                                                                                                                                                                                                                                                                                                                                                 |
| id                 | core | string     | The ID of a namespace.                                                                                                                                                                                                                                                                                                                                                                                                 |
| name               | core | string     | The name of the namespace, such as example.com.                                                                                                                                                                                                                                                                                                                                                                        |
| properties         | core | json       | A complex type that contains information that's specific to the type of the namespace.                                                                                                                                                                                                                                                                                                                                 |
| service_count      | core | int64      | The number of services that are associated with the namespace.                                                                                                                                                                                                                                                                                                                                                         |
| tags               | core | hstore_csv |
| type               | core | string     | The type of the namespace. The methods for discovering instances depends on the value that you specify: HTTP Instances can be discovered only programmatically, using the Cloud Map DiscoverInstances API. DNS_PUBLIC Instances can be discovered using public DNS queries and using the DiscoverInstances API. DNS_PRIVATE Instances can be discovered using DNS queries in VPCs and using the DiscoverInstances API. |
