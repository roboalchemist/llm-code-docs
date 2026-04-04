# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/aws_password_policy_with_unchangeable_passwords.md

---
title: AWS password policy with unchangeable passwords
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > AWS password policy with unchangeable
  passwords
---

# AWS password policy with unchangeable passwords

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9ef7d25d-9764-4224-9968-fa321c56ef76`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_account_password_policy)

### Description{% #description %}

This check evaluates whether the AWS IAM account password policy allows users to change their own passwords by ensuring the attribute `allow_users_to_change_password` is set to `true`. If `allow_users_to_change_password` is set to `false`, users are prevented from updating their passwords, which can lead to stale or compromised credentials remaining in active use. This increases the risk of unauthorized account access, as users are unable to maintain password hygiene or respond quickly to potential credential exposures.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_sqs_queue" "negative1" {
  name = "examplequeue"
}

// comment
resource "aws_iam_account_password_policy" "negative2" {
  minimum_password_length        = 10
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_sqs_queue" "positive1" {
  name = "examplequeue"
}

// comment
resource "aws_iam_account_password_policy" "positive2" {
  minimum_password_length        = 8
  require_lowercase_characters   = true
  require_numbers                = true
  require_uppercase_characters   = true
  require_symbols                = true
  allow_users_to_change_password = false
}
```
