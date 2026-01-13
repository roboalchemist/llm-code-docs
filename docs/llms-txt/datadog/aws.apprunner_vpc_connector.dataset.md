# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apprunner_vpc_connector.dataset.md

---
title: App Runner VPC Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Runner VPC Connector
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apprunner_vpc_connector.dataset/index.html
---

# App Runner VPC Connector

App Runner VPC Connector in AWS allows an App Runner service to securely connect to resources inside a VPC. It provides private networking capabilities so that applications can access databases, caches, or other services that are not publicly accessible. This enables tighter security and controlled communication between App Runner services and internal AWS resources.

```
aws.apprunner_vpc_connector
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                              | Description |
| ---------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| created_at             | core | timestamp     | The time when the VPC connector was created. It's in Unix time stamp format.                                                                                                                                                                                           |
| deleted_at             | core | timestamp     | The time when the VPC connector was deleted. It's in Unix time stamp format.                                                                                                                                                                                           |
| security_groups        | core | array<string> | A list of IDs of security groups that App Runner uses for access to Amazon Web Services resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic. |
| status                 | core | string        | The current state of the VPC connector. If the status of a connector revision is INACTIVE, it was deleted and can't be used. Inactive connector revisions are permanently removed some time after they are deleted.                                                    |
| subnets                | core | array<string> | A list of IDs of subnets that App Runner uses for your service. All IDs are of subnets of a single Amazon VPC.                                                                                                                                                         |
| tags                   | core | hstore        |
| vpc_connector_arn      | core | string        | The Amazon Resource Name (ARN) of this VPC connector.                                                                                                                                                                                                                  |
| vpc_connector_name     | core | string        | The customer-provided VPC connector name.                                                                                                                                                                                                                              |
| vpc_connector_revision | core | int64         | The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name. At this time, App Runner supports only one revision per name.                                                                           |
