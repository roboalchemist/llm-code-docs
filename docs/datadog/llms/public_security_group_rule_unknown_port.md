# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/public_security_group_rule_unknown_port.md

---
title: Public security group rule unknown port
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Public security group rule unknown port
---

# Public security group rule unknown port

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dd706080-b7a8-47dc-81fb-3e8184430ec0`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/security_group_rule#port_range)

### Description{% #description %}

An unknown port, such as `24` or `111`, is open to the public on the `tcp`, `udp`, or `all` protocol. This occurs when `port_range` includes ports not present in the known ports map and `cidr_ip` is set to `0.0.0.0/0`. Such security group rules expose services to the entire Internet and should be avoided.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "icmp"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "-1/-1"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "10.159.6.18/12"
}
```

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "1/65535"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "10.159.6.18/12"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "all"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "-1/-1"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
```

```terraform
resource "alicloud_security_group" "default" {
  name = "default"
}

resource "alicloud_security_group_rule" "allow_all_tcp" {
  type              = "ingress"
  ip_protocol       = "tcp"
  nic_type          = "internet"
  policy            = "accept"
  port_range        = "54/60"
  priority          = 1
  security_group_id = alicloud_security_group.default.id
  cidr_ip           = "0.0.0.0/0"
}
```
