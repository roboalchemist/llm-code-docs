# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshiftserverless_endpoint_access.dataset.md

---
title: Redshift Serverless Endpoint Access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Serverless Endpoint Access
---

# Redshift Serverless Endpoint Access

Redshift Serverless Endpoint Access in AWS provides a managed network endpoint that allows secure connectivity to a Redshift Serverless workgroup. It controls how users and applications connect to the serverless data warehouse, including VPC settings, subnets, and security groups. This resource helps manage access boundaries and ensures that Redshift Serverless can be reached from the desired network environments without requiring manual infrastructure setup.

```
aws.redshiftserverless_endpoint_access
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                            | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| account_id           | core | string        |
| address              | core | string        | The DNS address of the endpoint.                                                                     |
| endpoint_arn         | core | string        | The Amazon Resource Name (ARN) of the VPC endpoint.                                                  |
| endpoint_create_time | core | timestamp     | The time that the endpoint was created.                                                              |
| endpoint_name        | core | string        | The name of the VPC endpoint.                                                                        |
| endpoint_status      | core | string        | The status of the VPC endpoint.                                                                      |
| port                 | core | int64         | The port number on which Amazon Redshift Serverless accepts incoming connections.                    |
| subnet_ids           | core | array<string> | The unique identifier of subnets where Amazon Redshift Serverless choose to deploy the VPC endpoint. |
| tags                 | core | hstore_csv    |
| vpc_endpoint         | core | json          | The connection endpoint for connecting to Amazon Redshift Serverless.                                |
| vpc_security_groups  | core | json          | The security groups associated with the endpoint.                                                    |
| workgroup_name       | core | string        | The name of the workgroup associated with the endpoint.                                              |
