# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/service_control_policies_disabled.md

---
title: Service control policies disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Service control policies disabled
---

# Service control policies disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5ba6229c-8057-433e-91d0-21cf13569ca9`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/organizations_policy)

### Description{% #description %}

This check verifies whether the Amazon Organizations configuration has the `feature_set` attribute set to `"ALL"`, which enables all features, including the use of Service Control Policies (SCPs). If `feature_set` is set only to `"CONSOLIDATED_BILLING"`, as in the following example, then organizations cannot use SCPs for centralized governance, making it difficult to enforce security and compliance policies across AWS accounts:

```
resource "aws_organizations_organization" "example" {
  feature_set = "CONSOLIDATED_BILLING"
}
```

This leaves accounts within the organization more vulnerable to misconfigurations and unauthorized access, as critical controls cannot be imposed at the organization level.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_organizations_organization" "negative1" {
  aws_service_access_principals = [
    "cloudtrail.amazonaws.com",
    "config.amazonaws.com",
  ]

  feature_set = "ALL"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_organizations_organization" "positive1" {
  aws_service_access_principals = [
    "cloudtrail.amazonaws.com",
    "config.amazonaws.com",
  ]

  feature_set = "CONSOLIDATED_BILLING"
}
```
