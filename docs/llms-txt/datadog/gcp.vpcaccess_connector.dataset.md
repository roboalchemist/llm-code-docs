# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vpcaccess_connector.dataset.md

---
title: Serverless VPC Access Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Serverless VPC Access Connector
---

# Serverless VPC Access Connector

Serverless VPC Access Connector in Google Cloud allows serverless services like Cloud Functions, Cloud Run, and App Engine to connect securely to resources in a Virtual Private Cloud (VPC) network. It provides private IP connectivity, enabling access to databases, virtual machines, and other services within the VPC without exposing traffic to the public internet.

```
gcp.vpcaccess_connector
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| connected_projects   | core | array<string> | Output only. List of projects using the connector.                                                                                                                                                                                                                                                                                                                                                                           |
| datadog_display_name | core | string        |
| ip_cidr_range        | core | string        | Optional. The range of internal addresses that follows RFC 4632 notation. Example: `10.132.0.0/28`.                                                                                                                                                                                                                                                                                                                          |
| labels               | core | array<string> |
| machine_type         | core | string        | Machine type of VM Instance underlying connector. Default is e2-micro                                                                                                                                                                                                                                                                                                                                                        |
| max_instances        | core | int64         | Maximum value of instances in autoscaling group underlying the connector.                                                                                                                                                                                                                                                                                                                                                    |
| max_throughput       | core | int64         | Maximum throughput of the connector in Mbps. Refers to the expected throughput when using an `e2-micro` machine type. Value must be a multiple of 100 from 300 through 1000. Must be higher than the value specified by --min-throughput. If both max-throughput and max-instances are provided, max-instances takes precedence over max-throughput. The use of `max-throughput` is discouraged in favor of `max-instances`. |
| min_instances        | core | int64         | Minimum value of instances in autoscaling group underlying the connector.                                                                                                                                                                                                                                                                                                                                                    |
| min_throughput       | core | int64         | Minimum throughput of the connector in Mbps. Refers to the expected throughput when using an `e2-micro` machine type. Value must be a multiple of 100 from 200 through 900. Must be lower than the value specified by --max-throughput. If both min-throughput and min-instances are provided, min-instances takes precedence over min-throughput. The use of `min-throughput` is discouraged in favor of `min-instances`.   |
| name                 | core | string        | The resource name in the format `projects/*/locations/*/connectors/*`.                                                                                                                                                                                                                                                                                                                                                       |
| network              | core | string        | Optional. Name of a VPC network.                                                                                                                                                                                                                                                                                                                                                                                             |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the VPC access connector.                                                                                                                                                                                                                                                                                                                                                                              |
| subnet               | core | json          | Optional. The subnet in which to house the VPC Access Connector.                                                                                                                                                                                                                                                                                                                                                             |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
