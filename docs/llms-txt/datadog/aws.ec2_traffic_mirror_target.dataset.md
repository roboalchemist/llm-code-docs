# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_traffic_mirror_target.dataset.md

---
title: Traffic Mirror Target
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Traffic Mirror Target
---

# Traffic Mirror Target

A Traffic Mirror Target in AWS is a destination resource that receives mirrored network traffic from one or more Traffic Mirror Sessions. It can be a network interface, a Network Load Balancer, or a Gateway Load Balancer endpoint. This allows you to send copies of network traffic to monitoring and security appliances for deep packet inspection, threat detection, or troubleshooting without impacting the original traffic flow.

```
aws.ec2_traffic_mirror_target
```

## Fields

| Title                             | ID   | Type       | Data Type                                                    | Description |
| --------------------------------- | ---- | ---------- | ------------------------------------------------------------ | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| description                       | core | string     | Information about the Traffic Mirror target.                 |
| gateway_load_balancer_endpoint_id | core | string     | The ID of the Gateway Load Balancer endpoint.                |
| network_interface_id              | core | string     | The network interface ID that is attached to the target.     |
| network_load_balancer_arn         | core | string     | The Amazon Resource Name (ARN) of the Network Load Balancer. |
| owner_id                          | core | string     | The ID of the account that owns the Traffic Mirror target.   |
| tags                              | core | hstore_csv |
| traffic_mirror_target_id          | core | string     | The ID of the Traffic Mirror target.                         |
| type                              | core | string     | The type of Traffic Mirror target.                           |
