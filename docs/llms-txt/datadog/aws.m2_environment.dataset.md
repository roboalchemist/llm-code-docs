# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.m2_environment.dataset.md

---
title: Mainframe Modernization Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mainframe Modernization Environment
---

# Mainframe Modernization Environment

Mainframe Modernization Environment in AWS provides a managed runtime for migrating, modernizing, and running mainframe applications in the cloud. It offers the infrastructure and tools needed to deploy, test, and operate mainframe workloads without maintaining on-premises mainframe hardware. This environment supports different runtime engines, enabling organizations to replatform or refactor legacy applications while integrating with other AWS services for scalability, monitoring, and automation.

```
aws.m2_environment
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                       | Description |
| ---------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| account_id                   | core | string        |
| actual_capacity              | core | int64         | The number of instances included in the runtime environment. A standalone runtime environment has a maximum of one instance. Currently, a high availability runtime environment has a maximum of two instances. |
| creation_time                | core | timestamp     | The timestamp when the runtime environment was created.                                                                                                                                                         |
| description                  | core | string        | The description of the runtime environment.                                                                                                                                                                     |
| engine_type                  | core | string        | The target platform for the runtime environment.                                                                                                                                                                |
| engine_version               | core | string        | The version of the runtime engine.                                                                                                                                                                              |
| environment_arn              | core | string        | The Amazon Resource Name (ARN) of the runtime environment.                                                                                                                                                      |
| environment_id               | core | string        | The unique identifier of the runtime environment.                                                                                                                                                               |
| high_availability_config     | core | json          | The desired capacity of the high availability configuration for the runtime environment.                                                                                                                        |
| instance_type                | core | string        | The type of instance underlying the runtime environment.                                                                                                                                                        |
| kms_key_id                   | core | string        | The identifier of a customer managed key.                                                                                                                                                                       |
| load_balancer_arn            | core | string        | The Amazon Resource Name (ARN) for the load balancer used with the runtime environment.                                                                                                                         |
| name                         | core | string        | The name of the runtime environment. Must be unique within the account.                                                                                                                                         |
| network_type                 | core | string        | The network type supported by the runtime environment.                                                                                                                                                          |
| pending_maintenance          | core | json          | Indicates the pending maintenance scheduled on this environment.                                                                                                                                                |
| preferred_maintenance_window | core | string        | The maintenance window for the runtime environment. If you don't provide a value for the maintenance window, the service assigns a random value.                                                                |
| publicly_accessible          | core | bool          | Whether applications running in this runtime environment are publicly accessible.                                                                                                                               |
| security_group_ids           | core | array<string> | The unique identifiers of the security groups assigned to this runtime environment.                                                                                                                             |
| status                       | core | string        | The status of the runtime environment. If the Amazon Web Services Mainframe Modernization environment is missing a connection to the customer owned dependent resource, the status will be Unhealthy.           |
| status_reason                | core | string        | The reason for the reported status.                                                                                                                                                                             |
| storage_configurations       | core | json          | The storage configurations defined for the runtime environment.                                                                                                                                                 |
| subnet_ids                   | core | array<string> | The unique identifiers of the subnets assigned to this runtime environment.                                                                                                                                     |
| tags                         | core | hstore_csv    |
| vpc_id                       | core | string        | The unique identifier for the VPC used with this runtime environment.                                                                                                                                           |
