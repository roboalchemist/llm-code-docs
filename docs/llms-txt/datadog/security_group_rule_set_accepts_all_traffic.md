# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/security_group_rule_set_accepts_all_traffic.md

---
title: Beta - security group rule set accepts all traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - security group rule set accepts all
  traffic
---

# Beta - security group rule set accepts all traffic

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d135a36e-c474-452f-b891-76db1e6d1cd5`

**Cloud Provider:** TencentCloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/security_group_rule_set#ingress)

### Description{% #description %}

`tencentcloud_security_group_rule_set` `ingress` is configured to accept all traffic.This rule triggers when an `ingress` entry has `action` set to `ACCEPT` and the source is `cidr_block` = `0.0.0.0/0` (IPv4) or `ipv6_cidr_block` = `::/0` (IPv6), with `protocol` = `ALL` and `port` = `ALL`.`tencentcloud_security_group_rule_set` `ingress` should not be set to accept all traffic.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "Testing Rule Set Security"
}

resource "tencentcloud_security_group_rule_set" "base" {
  security_group_id = tencentcloud_security_group.sg.id
}
```

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "Testing Rule Set Security"
}

resource "tencentcloud_security_group_rule_set" "base" {
  security_group_id = tencentcloud_security_group.sg.id

  ingress {
    action      = "ACCEPT"
    cidr_block  = "10.0.0.0/22"
    protocol    = "TCP"
    port        = "80-90"
    description = "A:Allow Ips and 80-90"
  }

  egress {
    action      = "DROP"
    cidr_block  = "10.0.0.0/16"
    protocol    = "ICMP"
    description = "A:Block ping3"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "Testing Rule Set Security"
}

resource "tencentcloud_security_group_rule_set" "base" {
  security_group_id = tencentcloud_security_group.sg.id

  ingress {
    action     = "ACCEPT"
    cidr_block = "0.0.0.0/0"
  }
}
```

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "Testing Rule Set Security"
}

resource "tencentcloud_security_group_rule_set" "base" {
  security_group_id = tencentcloud_security_group.sg.id

  ingress {
    action          = "ACCEPT"
    ipv6_cidr_block = "::/0"
    protocol        = "ALL"
    port            = "ALL"
  }
}
```

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "Testing Rule Set Security"
}

resource "tencentcloud_security_group_rule_set" "base" {
  security_group_id = tencentcloud_security_group.sg.id

  ingress {
    action          = "ACCEPT"
    ipv6_cidr_block = "::/0"
  }
}
```
