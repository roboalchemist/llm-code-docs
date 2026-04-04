# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/nifcloud/elb_has_common_private.md

---
title: Beta - Nifcloud ELB has common private network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - Nifcloud ELB has common private network
---

# Beta - Nifcloud ELB has common private network

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5061f84c-ab66-4660-90b9-680c9df346c0`

**Cloud Provider:** Nifcloud

**Platform:** Terraform

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/nifcloud/nifcloud/latest/docs/resources/elb#network_id)

### Description{% #description %}

The `nifcloud_elb` is configured to use the shared private network `net-COMMON_PRIVATE`. This exposes the private side to the shared network and should instead use a dedicated private LAN to maintain isolation. The rule flags any `nifcloud_elb` where `network_interface.network_id` equals `net-COMMON_PRIVATE`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "nifcloud_elb" "negative" {
  availability_zone = "east-11"
  instance_port     = 80
  protocol          = "HTTP"
  lb_port           = 80
  network_interface {
    network_id = nifcloud_private_lan.main.id
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "nifcloud_elb" "positive" {
  availability_zone = "east-11"
  instance_port     = 80
  protocol          = "HTTP"
  lb_port           = 80
  network_interface {
    network_id = "net-COMMON_GLOBAL"
  }
  network_interface {
    network_id = "net-COMMON_PRIVATE"
  }
}
```

```terraform
resource "nifcloud_elb" "positive" {
  availability_zone = "east-11"
  instance_port     = 80
  protocol          = "HTTP"
  lb_port           = 80
  network_interface {
    network_id = "net-COMMON_PRIVATE"
  }
}
```
