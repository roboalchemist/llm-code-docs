# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.emrserverless_application.dataset.md

---
title: EMR Serverless Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EMR Serverless Application
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.emrserverless_application.dataset/index.html
---

# EMR Serverless Application

An EMR Serverless Application in AWS is a managed resource that lets you run big data frameworks like Apache Spark and Hive without managing clusters. It automatically provisions and scales compute and memory resources based on workload demand, removing the need for manual infrastructure setup. This makes it easier to run analytics and data processing jobs in a cost-efficient and serverless way.

```
aws.emrserverless_application
```

## Fields

| Title                         | ID   | Type      | Data Type                                                                                                                                                                                                                                                                            | Description |
| ----------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string    |
| account_id                    | core | string    |
| application_id                | core | string    | The ID of the application.                                                                                                                                                                                                                                                           |
| architecture                  | core | string    | The CPU architecture of an application.                                                                                                                                                                                                                                              |
| arn                           | core | string    | The ARN of the application.                                                                                                                                                                                                                                                          |
| auto_start_configuration      | core | json      | The configuration for an application to automatically start on job submission.                                                                                                                                                                                                       |
| auto_stop_configuration       | core | json      | The configuration for an application to automatically stop after a certain amount of time being idle.                                                                                                                                                                                |
| created_at                    | core | timestamp | The date and time when the application run was created.                                                                                                                                                                                                                              |
| identity_center_configuration | core | json      | The IAM Identity Center configuration applied to enable trusted identity propagation.                                                                                                                                                                                                |
| image_configuration           | core | json      | The image configuration applied to all worker types.                                                                                                                                                                                                                                 |
| initial_capacity              | core | string    | The initial capacity of the application.                                                                                                                                                                                                                                             |
| interactive_configuration     | core | json      | The interactive configuration object that enables the interactive use cases for an application.                                                                                                                                                                                      |
| maximum_capacity              | core | json      | The maximum capacity of the application. This is cumulative across all workers at any given point in time during the lifespan of the application is created. No new resources will be created once any one of the defined limits is hit.                                             |
| monitoring_configuration      | core | json      | The configuration setting for monitoring.                                                                                                                                                                                                                                            |
| name                          | core | string    | The name of the application.                                                                                                                                                                                                                                                         |
| network_configuration         | core | json      | The network configuration for customer VPC connectivity for the application.                                                                                                                                                                                                         |
| release_label                 | core | string    | The Amazon EMR release associated with the application.                                                                                                                                                                                                                              |
| runtime_configuration         | core | json      | The Configuration specifications of an application. Each configuration consists of a classification and properties. You use this parameter when creating or updating an application. To see the runtimeConfiguration object of an application, run the GetApplication API operation. |
| scheduler_configuration       | core | json      | The scheduler configuration for batch and streaming jobs running on this application. Supported with release labels emr-7.0.0 and above.                                                                                                                                             |
| state                         | core | string    | The state of the application.                                                                                                                                                                                                                                                        |
| state_details                 | core | string    | The state details of the application.                                                                                                                                                                                                                                                |
| tags                          | core | hstore    |
| type                          | core | string    | The type of application, such as Spark or Hive.                                                                                                                                                                                                                                      |
| updated_at                    | core | timestamp | The date and time when the application run was last updated.                                                                                                                                                                                                                         |
| worker_type_specifications    | core | string    | The specification applied to each worker type.                                                                                                                                                                                                                                       |
