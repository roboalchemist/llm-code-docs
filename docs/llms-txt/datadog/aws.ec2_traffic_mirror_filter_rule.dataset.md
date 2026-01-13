# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_traffic_mirror_filter_rule.dataset.md

---
title: Traffic Mirror Filter Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Traffic Mirror Filter Rule
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_traffic_mirror_filter_rule.dataset/index.html
---

# Traffic Mirror Filter Rule

A Traffic Mirror Filter Rule in AWS defines the criteria for capturing and mirroring network traffic in a VPC. It specifies conditions such as source and destination CIDR blocks, protocols, and port ranges to determine which traffic is mirrored. These rules are applied to a Traffic Mirror Filter, allowing fine-grained control over the traffic sent to monitoring and security appliances.

```
aws.ec2_traffic_mirror_filter_rule
```

## Fields

| Title                         | ID   | Type   | Data Type                                                             | Description |
| ----------------------------- | ---- | ------ | --------------------------------------------------------------------- | ----------- |
| _key                          | core | string |
| account_id                    | core | string |
| description                   | core | string | The description of the Traffic Mirror rule.                           |
| destination_cidr_block        | core | string | The destination CIDR block assigned to the Traffic Mirror rule.       |
| destination_port_range        | core | json   | The destination port range assigned to the Traffic Mirror rule.       |
| protocol                      | core | int64  | The protocol assigned to the Traffic Mirror rule.                     |
| rule_action                   | core | string | The action assigned to the Traffic Mirror rule.                       |
| rule_number                   | core | int64  | The rule number of the Traffic Mirror rule.                           |
| source_cidr_block             | core | string | The source CIDR block assigned to the Traffic Mirror rule.            |
| source_port_range             | core | json   | The source port range assigned to the Traffic Mirror rule.            |
| tags                          | core | hstore |
| traffic_direction             | core | string | The traffic direction assigned to the Traffic Mirror rule.            |
| traffic_mirror_filter_id      | core | string | The ID of the Traffic Mirror filter that the rule is associated with. |
| traffic_mirror_filter_rule_id | core | string | The ID of the Traffic Mirror rule.                                    |
