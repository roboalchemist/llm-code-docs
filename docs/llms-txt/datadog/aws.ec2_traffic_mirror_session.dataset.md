# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_traffic_mirror_session.dataset.md

---
title: Traffic Mirror Session
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Traffic Mirror Session
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_traffic_mirror_session.dataset/index.html
---

# Traffic Mirror Session

A Traffic Mirror Session in AWS allows you to capture and mirror network traffic from an Elastic Network Interface (ENI) to a target for monitoring and analysis. It defines the source ENI, the target destination (such as a Network Load Balancer or EC2 instance), and optional filters to control which traffic is mirrored. This helps with deep packet inspection, troubleshooting, and security monitoring without impacting the original traffic flow.

```
aws.ec2_traffic_mirror_session
```

## Fields

| Title                     | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                                                                      | Description |
| ------------------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string |
| account_id                | core | string |
| description               | core | string | The description of the Traffic Mirror session.                                                                                                                                                                                                                                                                                                                 |
| network_interface_id      | core | string | The ID of the Traffic Mirror session's network interface.                                                                                                                                                                                                                                                                                                      |
| owner_id                  | core | string | The ID of the account that owns the Traffic Mirror session.                                                                                                                                                                                                                                                                                                    |
| packet_length             | core | int64  | The number of bytes in each packet to mirror. These are the bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet |
| session_number            | core | int64  | The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets. Valid values are 1-32766.                                                                                                                                |
| tags                      | core | hstore |
| traffic_mirror_filter_id  | core | string | The ID of the Traffic Mirror filter.                                                                                                                                                                                                                                                                                                                           |
| traffic_mirror_session_id | core | string | The ID for the Traffic Mirror session.                                                                                                                                                                                                                                                                                                                         |
| traffic_mirror_target_id  | core | string | The ID of the Traffic Mirror target.                                                                                                                                                                                                                                                                                                                           |
| virtual_network_id        | core | int64  | The virtual network ID associated with the Traffic Mirror session.                                                                                                                                                                                                                                                                                             |
