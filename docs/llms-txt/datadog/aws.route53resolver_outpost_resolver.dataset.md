# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53resolver_outpost_resolver.dataset.md

---
title: "Route\_53 Resolver on Outposts Resolver"
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: "Docs > DDSQL Reference > Data Directory > Route\_53 Resolver on Outposts Resolver"
---

# Route 53 Resolver on Outposts Resolver

Route 53 Resolver on Outposts Resolver is an AWS resource that enables DNS query resolution within an Outpost environment. It extends Route 53 Resolver functionality to on-premises Outposts, allowing workloads running locally to resolve domain names without relying on external DNS infrastructure. This helps maintain low-latency, secure, and consistent DNS resolution for hybrid applications.

```
aws.route53resolver_outpost_resolver
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                  | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| arn                     | core | string     | The ARN (Amazon Resource Name) for the Resolver on an Outpost.                                                                                                                             |
| creation_time           | core | string     | The date and time that the Outpost Resolver was created, in Unix time format and Coordinated Universal Time (UTC).                                                                         |
| creator_request_id      | core | string     | A unique string that identifies the request that created the Resolver endpoint. The CreatorRequestId allows failed requests to be retried without the risk of running the operation twice. |
| id                      | core | string     | The ID of the Resolver on Outpost.                                                                                                                                                         |
| instance_count          | core | int64      | Amazon EC2 instance count for the Resolver on the Outpost.                                                                                                                                 |
| modification_time       | core | string     | The date and time that the Outpost Resolver was modified, in Unix time format and Coordinated Universal Time (UTC).                                                                        |
| name                    | core | string     | Name of the Resolver.                                                                                                                                                                      |
| outpost_arn             | core | string     | The ARN (Amazon Resource Name) for the Outpost.                                                                                                                                            |
| preferred_instance_type | core | string     | The Amazon EC2 instance type.                                                                                                                                                              |
| status                  | core | string     | Status of the Resolver.                                                                                                                                                                    |
| status_message          | core | string     | A detailed description of the Resolver.                                                                                                                                                    |
| tags                    | core | hstore_csv |
