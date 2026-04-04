# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_password_does_not_require_uppercase.md

---
title: IAM password policy does not require uppercase letter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM password policy does not require uppercase
  letter
---

# IAM password policy does not require uppercase letter

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2c3d4ghwt-e5f6-7890-ab12-cd34ef567890`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_account_password_policy#require_uppercase_characters)

### Description{% #description %}

This check ensures that the AWS IAM password policy requires users to include at least one uppercase letter in their passwords. Without enforcing uppercase characters, passwords become more susceptible to brute-force or dictionary attacks, as the possible character space is significantly reduced. This weakens account security and increases the risk of unauthorized access to critical resources. Enforcing a strong password policy, including uppercase letter requirements, helps protect sensitive AWS environments from compromise due to easily guessed or weak passwords.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_account_password_policy" "good_example" {
  minimum_password_length      = 14
  require_symbols              = true
  require_numbers              = true
  require_lowercase_characters = true
  require_uppercase_characters = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_account_password_policy" "bad_example" {
  minimum_password_length      = 14
  require_symbols              = true
  require_numbers              = true
  require_lowercase_characters = true
  require_uppercase_characters = false
}
```
