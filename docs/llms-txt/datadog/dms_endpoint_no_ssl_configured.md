# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/dms_endpoint_no_ssl_configured.md

---
title: DMS endpoints without SSL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DMS endpoints without SSL
---

# DMS endpoints without SSL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e6f7g8h9-i0j1-4klm-56no-7890pqrstu12`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dms_endpoint#ssl_mode)

### Description{% #description %}

AWS Database Migration Service (DMS) endpoints without SSL encryption leave sensitive data exposed during transmission between source and target databases. When SSL mode is set to `none`, database credentials and data are transmitted in plaintext, potentially allowing attackers to intercept and capture confidential information. To secure your endpoints, ensure the `ssl_mode` parameter is set to `require` rather than `none`, as shown below:

```
resource "aws_dms_endpoint" "example" {
  endpoint_id   = "example-endpoint"
  endpoint_type = "source"
  engine_name   = "mysql"
  ssl_mode      = "require"  // Secure configuration
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_dms_endpoint" "good_example_exempt_source" {
  endpoint_id   = "example-source-s3"
  endpoint_type = "source"
  engine_name   = "s3"
  ssl_mode      = "none" # â S3 source is exempt
}

resource "aws_dms_endpoint" "good_example_exempt_target" {
  endpoint_id   = "example-target-kinesis"
  endpoint_type = "target"
  engine_name   = "kinesis"
  ssl_mode      = "none" # â Kinesis target is exempt
}
```

```terraform
resource "aws_dms_endpoint" "good_example_source" {
  endpoint_id   = "example-source"
  endpoint_type = "source"
  engine_name   = "mysql"
  ssl_mode      = "require" # â SSL is enabled
}

resource "aws_dms_endpoint" "good_example_target" {
  endpoint_id   = "example-target"
  endpoint_type = "target"
  engine_name   = "postgres"
  ssl_mode      = "require" # â SSL is enabled
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_dms_endpoint" "bad_example_source" {
  endpoint_id   = "example-source"
  endpoint_type = "source"
  engine_name   = "mysql"
  ssl_mode      = "none" # â SSL is disabled for a non-exempt source endpoint
}

resource "aws_dms_endpoint" "bad_example_target" {
  endpoint_id   = "example-target"
  endpoint_type = "target"
  engine_name   = "postgres"
  ssl_mode      = "none" # â SSL is disabled for a non-exempt target endpoint
}
```
