# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.m2_application.dataset.md

---
title: Mainframe Modernization Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mainframe Modernization Application
---

# Mainframe Modernization Application

Mainframe Modernization Application in AWS is a managed resource that represents an application running within the AWS Mainframe Modernization service. It allows organizations to migrate, modernize, and run mainframe workloads in a cloud-native environment. This resource provides details about the application, including its configuration, runtime environment, and deployment state, enabling easier management and integration of legacy mainframe systems with modern AWS services.

```
aws.m2_application
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                            | Description |
| ---------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| application_arn        | core | string        | The Amazon Resource Name (ARN) of the application.                                                                                                                                                                                                   |
| application_id         | core | string        | The identifier of the application.                                                                                                                                                                                                                   |
| creation_time          | core | timestamp     | The timestamp when this application was created.                                                                                                                                                                                                     |
| deployed_version       | core | json          | The version of the application that is deployed.                                                                                                                                                                                                     |
| description            | core | string        | The description of the application.                                                                                                                                                                                                                  |
| engine_type            | core | string        | The type of the target platform for the application.                                                                                                                                                                                                 |
| environment_id         | core | string        | The identifier of the runtime environment where you want to deploy the application.                                                                                                                                                                  |
| kms_key_id             | core | string        | The identifier of a customer managed key.                                                                                                                                                                                                            |
| last_start_time        | core | timestamp     | The timestamp when you last started the application. Null until the application runs for the first time.                                                                                                                                             |
| latest_version         | core | json          | The latest version of the application.                                                                                                                                                                                                               |
| listener_arns          | core | array<string> | The Amazon Resource Name (ARN) for the network load balancer listener created in your Amazon Web Services account. Amazon Web Services Mainframe Modernization creates this listener for you the first time you deploy an application.               |
| listener_ports         | core | array<int64>  | The port associated with the network load balancer listener created in your Amazon Web Services account.                                                                                                                                             |
| load_balancer_dns_name | core | string        | The public DNS name of the load balancer created in your Amazon Web Services account.                                                                                                                                                                |
| log_groups             | core | json          | The list of log summaries. Each log summary includes the log type as well as the log group identifier. These are CloudWatch logs. Amazon Web Services Mainframe Modernization pushes the application log to CloudWatch under the customer's account. |
| name                   | core | string        | The unique identifier of the application.                                                                                                                                                                                                            |
| role_arn               | core | string        | The Amazon Resource Name (ARN) of the role associated with the application.                                                                                                                                                                          |
| status                 | core | string        | The status of the application.                                                                                                                                                                                                                       |
| status_reason          | core | string        | The reason for the reported status.                                                                                                                                                                                                                  |
| tags                   | core | hstore_csv    |
| target_group_arns      | core | array<string> | Returns the Amazon Resource Names (ARNs) of the target groups that are attached to the network load balancer.                                                                                                                                        |
