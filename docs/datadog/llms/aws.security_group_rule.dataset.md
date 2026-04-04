# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.security_group_rule.dataset.md

---
title: Security Group Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Group Rule
---

# Security Group Rule

This table represents the Security Group Rule resource from Amazon Web Services.

```
aws.security_group_rule
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                                               | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| cidr_ipv4               | core | string     | The IPv4 CIDR range.                                                                                                                                                                                                                                                    |
| cidr_ipv6               | core | string     | The IPv6 CIDR range.                                                                                                                                                                                                                                                    |
| description             | core | string     | The security group rule description.                                                                                                                                                                                                                                    |
| from_port               | core | int64      | If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).                                                                                                                    |
| group_id                | core | string     | The ID of the security group.                                                                                                                                                                                                                                           |
| group_owner_id          | core | string     | The ID of the Amazon Web Services account that owns the security group.                                                                                                                                                                                                 |
| ip_protocol             | core | string     | The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers</a>). Use <code>-1</code> to specify all protocols. |
| is_egress               | core | bool       | Indicates whether the security group rule is an outbound rule.                                                                                                                                                                                                          |
| prefix_list_id          | core | string     | The ID of the prefix list.                                                                                                                                                                                                                                              |
| referenced_group_info   | core | json       | Describes the security group that is referenced in the rule.                                                                                                                                                                                                            |
| security_group_rule_arn | core | string     |
| security_group_rule_id  | core | string     | The ID of the security group rule.                                                                                                                                                                                                                                      |
| tags                    | core | hstore_csv |
| to_port                 | core | int64      | If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).                             |
