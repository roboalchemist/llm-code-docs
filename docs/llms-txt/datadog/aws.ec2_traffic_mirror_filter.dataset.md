# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_traffic_mirror_filter.dataset.md

---
title: EC2 Traffic Mirror Filter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Traffic Mirror Filter
---

# EC2 Traffic Mirror Filter

An EC2 Traffic Mirror Filter in AWS defines the rules that control the network traffic captured by a Traffic Mirror session. It specifies which inbound and outbound packets are mirrored based on protocol, port, and CIDR ranges. Filters allow you to include or exclude specific traffic, giving fine-grained control over what is sent to monitoring and security tools.

```
aws.ec2_traffic_mirror_filter
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                               | Description |
| ------------------------ | ---- | ------------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| account_id               | core | string        |
| description              | core | string        | The description of the Traffic Mirror filter.                                           |
| egress_filter_rules      | core | json          | Information about the egress rules that are associated with the Traffic Mirror filter.  |
| ingress_filter_rules     | core | json          | Information about the ingress rules that are associated with the Traffic Mirror filter. |
| network_services         | core | array<string> | The network service traffic that is associated with the Traffic Mirror filter.          |
| tags                     | core | hstore_csv    |
| traffic_mirror_filter_id | core | string        | The ID of the Traffic Mirror filter.                                                    |
