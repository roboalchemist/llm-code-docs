# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apprunner_vpc_ingress_connection.dataset.md

---
title: App Runner VPC Ingress Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Runner VPC Ingress Connection
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apprunner_vpc_ingress_connection.dataset/index.html
---

# App Runner VPC Ingress Connection

App Runner VPC Ingress Connection in AWS allows an App Runner service to receive traffic securely from resources inside a VPC instead of the public internet. It establishes a managed network path between the VPC and the App Runner service, enabling private communication, improved security, and compliance with internal networking requirements.

```
aws.apprunner_vpc_ingress_connection
```

## Fields

| Title                       | ID   | Type      | Data Type                                                                                                                                                                                                                                         | Description |
| --------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    | The Account Id you use to create the VPC Ingress Connection resource.                                                                                                                                                                             |
| created_at                  | core | timestamp | The time when the VPC Ingress Connection was created. It's in the Unix time stamp format. Type: Timestamp Required: Yes                                                                                                                           |
| deleted_at                  | core | timestamp | The time when the App Runner service was deleted. It's in the Unix time stamp format. Type: Timestamp Required: No                                                                                                                                |
| domain_name                 | core | string    | The domain name associated with the VPC Ingress Connection resource.                                                                                                                                                                              |
| ingress_vpc_configuration   | core | json      | Specifications for the customer's VPC and related PrivateLink VPC endpoint that are used to associate with the VPC Ingress Connection resource.                                                                                                   |
| service_arn                 | core | string    | The Amazon Resource Name (ARN) of the service associated with the VPC Ingress Connection.                                                                                                                                                         |
| status                      | core | string    | The current status of the VPC Ingress Connection. The VPC Ingress Connection displays one of the following statuses: AVAILABLE, PENDING_CREATION, PENDING_UPDATE, PENDING_DELETION,FAILED_CREATION, FAILED_UPDATE, FAILED_DELETION, and DELETED.. |
| tags                        | core | hstore    |
| vpc_ingress_connection_arn  | core | string    | The Amazon Resource Name (ARN) of the VPC Ingress Connection.                                                                                                                                                                                     |
| vpc_ingress_connection_name | core | string    | The customer-provided VPC Ingress Connection name.                                                                                                                                                                                                |
