# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/password_without_reuse_prevention.md

---
title: Password without reuse prevention
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Password without reuse prevention
---

# Password without reuse prevention

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `89806cdc-9c2e-4bd1-a0dc-53f339bcfb2a`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_account_password_policy#password_reuse_prevention)

### Description{% #description %}

This check ensures that the IAM account password policy's `password_reuse_prevention` attribute is set to at least 24, preventing users from reusing any of their last 24 passwords. Without this configuration, as seen when `password_reuse_prevention = 20` or when the attribute is omitted, users may repeatedly cycle through a small set of previously used passwords, increasing the risk of password-related attacks. Configuring a secure password policy, as in the following example, helps to enforce strong password hygiene and mitigates the likelihood of compromised credentials being reused:

```
resource "aws_iam_account_password_policy" "secure" {
  minimum_password_length        = 8
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
  password_reuse_prevention      = 24
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_account_password_policy" "negative1" {
  minimum_password_length        = 8
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
  password_reuse_prevention = 24
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_account_password_policy" "positive1" {
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
  password_reuse_prevention = 20
}

resource "aws_iam_account_password_policy" "positive2" {
  minimum_password_length        = 3
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
}
```
