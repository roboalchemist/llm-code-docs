# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/general/generic_git_module_without_revision.md

---
title: Generic Git module without revision
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Generic Git module without revision
---

# Generic Git module without revision

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3a81fc06-566f-492a-91dd-7448e409e2cd`

**Cloud Provider:** Common

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://www.terraform.io/docs/language/modules/sources.html#selecting-a-revision)

### Description{% #description %}

All generic Git module sources should include a revision reference. Module sources that begin with `git::` must include a `?ref=` parameter to pin the source to a specific commit, tag, or branch. This ensures reproducible and predictable builds. This rule flags modules where `module.source` starts with `git::` and does not contain `?ref=`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
variable "cluster_name" {
  default     = "example"
  description = "cluster name"
  type        = string
}

module "acm" {
  source      = "terraform-aws-modules/acm/aws"
  version     = "~> v2.0"
  domain_name = var.site_domain
  zone_id     = data.aws_route53_zone.this.zone_id
  tags        = var.tags

  providers = {
    aws = aws.us_east_1 # cloudfront needs acm certificate to be from "us-east-1" region
  }
}

resource "aws_eks_cluster" "negative1" {
  depends_on                = [aws_cloudwatch_log_group.example]

  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
  name                      = var.cluster_name
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
variable "cluster_name" {
  default     = "example"
  description = "cluster name"
  type        = string
}

module "acm" {
  source      = "git::https://example.com/vpc.git"
  version     = "~> v2.0"
  domain_name = var.site_domain
  zone_id     = data.aws_route53_zone.this.zone_id
  tags        = var.tags

  providers = {
    aws = aws.us_east_1 # cloudfront needs acm certificate to be from "us-east-1" region
  }
}

resource "aws_eks_cluster" "negative1" {
  depends_on                = [aws_cloudwatch_log_group.example]

  enabled_cluster_log_types = ["api", "audit", "authenticator", "controllerManager", "scheduler"]
  name                      = var.cluster_name
}
```
