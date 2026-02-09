# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.network_firewall_vpc_endpoint_association.dataset.md

---
title: Network Firewall VPC Endpoint Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Network Firewall VPC Endpoint
  Association
---

# Network Firewall VPC Endpoint Association

This table represents the Network Firewall VPC Endpoint Association resource from Amazon Web Services.

```
aws.network_firewall_vpc_endpoint_association
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                                                                | Description |
| ------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| tags                            | core | hstore_csv |
| vpc_endpoint_association        | core | json       | The configuration settings for the VPC endpoint association. These settings include the firewall and the VPC and subnet to use for the firewall endpoint.                                                |
| vpc_endpoint_association_status | core | json       | Detailed information about the current status of a <a>VpcEndpointAssociation</a>. You can retrieve this by calling <a>DescribeVpcEndpointAssociation</a> and providing the VPC endpoint association ARN. |
