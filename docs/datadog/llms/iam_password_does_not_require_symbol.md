# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_password_does_not_require_symbol.md

---
title: IAM password policy does not require symbol
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM password policy does not require symbol
---

# IAM password policy does not require symbol

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `bts2c3d4-e5f6-7890-ab12-cd34ef567890`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_account_password_policy#require_symbols)

### Description{% #description %}

This check ensures that the AWS IAM account password policy enforces the use of at least one symbol in user passwords by setting `require_symbols = true`. If `require_symbols` is set to `false`, as shown below it weakens password complexity, making user accounts more susceptible to brute-force or password guessing attacks. Failing to enforce symbol usage increases the risk of unauthorized access to AWS resources.

```
resource "aws_iam_account_password_policy" "bad_example" {
  minimum_password_length      = 14
  require_symbols              = false
  require_numbers              = true
  require_lowercase_characters = true
  require_uppercase_characters = true
}
```

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
  require_symbols              = false
  require_numbers              = true
  require_lowercase_characters = true
  require_uppercase_characters = true
}
```
