# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/resource_not_using_tags.md

---
title: Resource not using tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Resource not using tags
---

# Resource not using tags

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e38a8e0a-b88b-4902-b3fe-b0fcb17d5c10`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/resource-tagging)

### Description{% #description %}

AWS resource tagging is an essential best practice that supports resource management, cost tracking, automation, and security enforcement. If only the default `Name` tag is applied and no additional metadata tags (such as `Environment`, `Owner`, or `Project`) are defined, resources may become difficult to identify, audit, and manage at scale, increasing the risk of misconfiguration or unintended resource exposure. For example, a secure configuration should use a `tags` block with descriptive tags:

```
tags = {
  Name        = "example-cert"
  Environment = "production"
  Owner       = "devops-team"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_acm_certificate" "cert" {
  domain_name       = "example.com"
  validation_method = "DNS"

  tags = {
    Environment = "test"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_acm_certificate_validation" "example" {
  certificate_arn         = aws_acm_certificate.example.arn
  validation_record_fqdns = [for record in aws_route53_record.example : record.fqdn]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_acm_certificate" "cert" {
  domain_name       = "example.com"
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_acm_certificate" "cert_2" {
  domain_name       = "example.com"
  validation_method = "DNS"

  tags = {
    Name = "test"
  }

  lifecycle {
    create_before_destroy = true
  }
}
```
