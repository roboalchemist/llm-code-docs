# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_cluster_endpoint.dataset.md

---
title: RDS Cluster Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Cluster Endpoint
---

# RDS Cluster Endpoint

This table represents the RDS Cluster Endpoint resource from Amazon Web Services.

```
aws.rds_cluster_endpoint
```

## Fields

| Title                                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                | Description |
| --------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                    | core | string        |
| account_id                              | core | string        |
| custom_endpoint_type                    | core | string        | The type associated with a custom endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>ANY</code>.                                                                                                                                                                                                                                                          |
| db_cluster_endpoint_arn                 | core | string        | The Amazon Resource Name (ARN) for the endpoint.                                                                                                                                                                                                                                                                                                                         |
| db_cluster_endpoint_identifier          | core | string        | The identifier associated with the endpoint. This parameter is stored as a lowercase string.                                                                                                                                                                                                                                                                             |
| db_cluster_endpoint_resource_identifier | core | string        | A unique system-generated identifier for an endpoint. It remains the same for the whole life of the endpoint.                                                                                                                                                                                                                                                            |
| db_cluster_identifier                   | core | string        | The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.                                                                                                                                                                                                                                                |
| endpoint                                | core | string        | The DNS address of the endpoint.                                                                                                                                                                                                                                                                                                                                         |
| endpoint_type                           | core | string        | The type of the endpoint. One of: <code>READER</code>, <code>WRITER</code>, <code>CUSTOM</code>.                                                                                                                                                                                                                                                                         |
| excluded_members                        | core | array<string> | List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.                                                                                                                                                             |
| static_members                          | core | array<string> | List of DB instance identifiers that are part of the custom endpoint group.                                                                                                                                                                                                                                                                                              |
| status                                  | core | string        | The current status of the endpoint. One of: <code>creating</code>, <code>available</code>, <code>deleting</code>, <code>inactive</code>, <code>modifying</code>. The <code>inactive</code> state applies to an endpoint that can't be used for a certain kind of cluster, such as a <code>writer</code> endpoint for a read-only secondary cluster in a global database. |
| tags                                    | core | hstore_csv    |
