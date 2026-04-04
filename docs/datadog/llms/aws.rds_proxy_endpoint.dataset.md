# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_proxy_endpoint.dataset.md

---
title: RDS Proxy Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Proxy Endpoint
---

# RDS Proxy Endpoint

This table represents the RDS Proxy Endpoint resource from Amazon Web Services.

```
aws.rds_proxy_endpoint
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                        | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| created_date           | core | timestamp     | The date and time when the DB proxy endpoint was first created.                                                                                                                                                                                  |
| db_proxy_endpoint_arn  | core | string        | The Amazon Resource Name (ARN) for the DB proxy endpoint.                                                                                                                                                                                        |
| db_proxy_endpoint_name | core | string        | The name for the DB proxy endpoint. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.                                              |
| db_proxy_name          | core | string        | The identifier for the DB proxy that is associated with this DB proxy endpoint.                                                                                                                                                                  |
| endpoint               | core | string        | The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.                                                                                             |
| is_default             | core | bool          | Indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.   |
| status                 | core | string        | The current status of this DB proxy endpoint. A status of <code>available</code> means the endpoint is ready to handle requests. Other values indicate that you must wait for the endpoint to be ready, or take some action to resolve an issue. |
| tags                   | core | hstore_csv    |
| target_role            | core | string        | A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.                                                                                                                                         |
| vpc_id                 | core | string        | Provides the VPC ID of the DB proxy endpoint.                                                                                                                                                                                                    |
| vpc_security_group_ids | core | array<string> | Provides a list of VPC security groups that the DB proxy endpoint belongs to.                                                                                                                                                                    |
| vpc_subnet_ids         | core | array<string> | The EC2 subnet IDs for the DB proxy endpoint.                                                                                                                                                                                                    |
