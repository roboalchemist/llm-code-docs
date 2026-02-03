# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_client_vpn_target_network.dataset.md

---
title: Ec2 Client Vpn Target Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Client Vpn Target Network
---

# Ec2 Client Vpn Target Network

This table represents the ec2_client_vpn_target_network resource from Amazon Web Services.

```
aws.ec2_client_vpn_target_network
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                      | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| association_id         | core | string        | The ID of the association.                                                     |
| client_vpn_endpoint_id | core | string        | The ID of the Client VPN endpoint with which the target network is associated. |
| security_groups        | core | array<string> | The IDs of the security groups applied to the target network association.      |
| status                 | core | json          | The current state of the target network association.                           |
| tags                   | core | hstore_csv    |
| target_network_id      | core | string        | The ID of the subnet specified as the target network.                          |
| vpc_id                 | core | string        | The ID of the VPC in which the target network (subnet) is located.             |
