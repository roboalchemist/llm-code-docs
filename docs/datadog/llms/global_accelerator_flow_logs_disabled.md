# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/global_accelerator_flow_logs_disabled.md

---
title: Global Accelerator flow logs disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Global Accelerator flow logs disabled
---

# Global Accelerator flow logs disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `96e8183b-e985-457b-90cd-61c0503a3369`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/globalaccelerator_accelerator#flow_logs_enabled)

### Description{% #description %}

Enabling flow logs for AWS Global Accelerator allows visibility into all traffic that traverses the accelerator, providing critical data for monitoring, security auditing, and detecting anomalous activity. If the Terraform attribute `flow_logs_enabled` is not set to `true` and related fields such as `flow_logs_s3_bucket` are not specified, administrators lose valuable insight into network events, significantly hindering threat detection and incident response. Without flow logs enabled, malicious or unauthorized activity could go undetected, increasing the risk of security breaches and data exfiltration.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_globalaccelerator_accelerator" "negative1" {
  name            = "Example"
  ip_address_type = "IPV4"
  enabled         = true

  attributes {
    flow_logs_enabled   = true
    flow_logs_s3_bucket = "example-bucket"
    flow_logs_s3_prefix = "flow-logs/"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_globalaccelerator_accelerator" "positive2" {
  name            = "Example"
  ip_address_type = "IPV4"
  enabled         = true

  attributes {
    flow_logs_s3_bucket = "example-bucket"
    flow_logs_s3_prefix = "flow-logs/"
  }
}
```

```terraform
resource "aws_globalaccelerator_accelerator" "positive3" {
  name            = "Example"
  ip_address_type = "IPV4"
  enabled         = true

  attributes {
    flow_logs_enabled   = false
  }
}
```

```terraform
resource "aws_globalaccelerator_accelerator" "positive1" {
  name            = "Example"
  ip_address_type = "IPV4"
  enabled         = true
}
```
