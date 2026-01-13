# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.directconnect_gateway.dataset.md

---
title: Direct Connect Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Direct Connect Gateway
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.directconnect_gateway.dataset/index.html
---

# Direct Connect Gateway

Direct Connect Gateway in AWS allows you to connect your Amazon Direct Connect connections to one or more Virtual Private Clouds (VPCs) across different AWS Regions. It provides a way to extend private connectivity beyond a single region without requiring multiple physical connections, simplifying network management and reducing costs.

```
aws.directconnect_gateway
```

## Fields

| Title                               | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                                                                  | Description |
| ----------------------------------- | ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string |
| account_id                          | core | string |
| amazon_side_asn                     | core | int64  | The autonomous system number (ASN) for the Amazon side of the connection.                                                                                                                                                                                                                                                                                  |
| direct_connect_gateway_associations | core | json   | Information about the associations.                                                                                                                                                                                                                                                                                                                        |
| direct_connect_gateway_id           | core | string | The ID of the Direct Connect gateway.                                                                                                                                                                                                                                                                                                                      |
| direct_connect_gateway_name         | core | string | The name of the Direct Connect gateway.                                                                                                                                                                                                                                                                                                                    |
| direct_connect_gateway_state        | core | string | The state of the Direct Connect gateway. The following are the possible values: pending: The initial state after calling CreateDirectConnectGateway. available: The Direct Connect gateway is ready for use. deleting: The initial state after calling DeleteDirectConnectGateway. deleted: The Direct Connect gateway is deleted and cannot pass traffic. |
| directconnect_gateway_arn           | core | string |
| next_token                          | core | string | The token to retrieve the next page.                                                                                                                                                                                                                                                                                                                       |
| owner_account                       | core | string | The ID of the Amazon Web Services account that owns the Direct Connect gateway.                                                                                                                                                                                                                                                                            |
| state_change_error                  | core | string | The error message if the state of an object failed to advance.                                                                                                                                                                                                                                                                                             |
| tags                                | core | hstore |
