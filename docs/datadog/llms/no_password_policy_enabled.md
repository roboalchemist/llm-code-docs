# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/no_password_policy_enabled.md

---
title: No password policy enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > No password policy enabled
---

# No password policy enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b592ffd4-0577-44b6-bd35-8c5ee81b5918`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user_login_profile)

### Description{% #description %}

Ensuring strong AWS IAM password security involves configuring both the `password_length` and `password_reset_required` attributes in the `aws_iam_user_login_profile` resource. Failing to set a sufficient `password_length` or omitting the `password_reset_required = true` option, as shown below, can lead to accounts being protected by weak or reused passwords, which increases the risk of unauthorized access.

```
resource "aws_iam_user_login_profile" "example" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"
  password_length = 13
  password_reset_required = false
}
```

By requiring users to reset passwords on first use and enforcing adequate password length, as in the following example, organizations can better defend against brute-force attacks and reduce credential compromise risk.

```
resource "aws_iam_user_login_profile" "example" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"
  password_length = 15
  password_reset_required = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_user_login_profile" "negative1" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"

  password_reset_required = true

  password_length = 15
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_user_login_profile" "positive2" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"

  password_reset_required = false

  password_length = 15
}

resource "aws_iam_user_login_profile" "positive3" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"

  password_reset_required = true

  password_length = 13
}

resource "aws_iam_user_login_profile" "positive6" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"

  password_length = 13
}

resource "aws_iam_user_login_profile" "positive7" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"

  password_reset_required = false
  password_length = 13
}
```
