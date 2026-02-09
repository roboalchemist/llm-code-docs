# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appsync_function.dataset.md

---
title: AppSync Function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppSync Function
---

# AppSync Function

An AppSync Function in AWS is a reusable unit of business logic within an AppSync pipeline resolver. It allows you to define operations such as data fetching, transformation, or validation that can be composed together in sequence. Functions can interact with data sources like DynamoDB, Lambda, or HTTP endpoints, and are executed in the order defined by the pipeline. This helps modularize resolver logic, making it easier to maintain, reuse, and scale GraphQL APIs.

```
aws.appsync_function
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                     | Description |
| ------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| code                      | core | string     | The function code that contains the request and response functions. When code is used, the runtime is required. The runtime value must be APPSYNC_JS.                                                                                         |
| data_source_name          | core | string     | The name of the DataSource.                                                                                                                                                                                                                   |
| description               | core | string     | The Function description.                                                                                                                                                                                                                     |
| function_arn              | core | string     | The Amazon Resource Name (ARN) of the Function object.                                                                                                                                                                                        |
| function_id               | core | string     | A unique ID representing the Function object.                                                                                                                                                                                                 |
| function_version          | core | string     | The version of the request mapping template. Currently, only the 2018-05-29 version of the template is supported.                                                                                                                             |
| max_batch_size            | core | int64      | The maximum batching size for a resolver.                                                                                                                                                                                                     |
| name                      | core | string     | The name of the Function object.                                                                                                                                                                                                              |
| request_mapping_template  | core | string     | The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.                                                                                                                         |
| response_mapping_template | core | string     | The Function response mapping template.                                                                                                                                                                                                       |
| runtime                   | core | json       | Describes a runtime used by an Amazon Web Services AppSync pipeline resolver or Amazon Web Services AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified. |
| sync_config               | core | json       | Describes a Sync configuration for a resolver. Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.                                                                                       |
| tags                      | core | hstore_csv |
