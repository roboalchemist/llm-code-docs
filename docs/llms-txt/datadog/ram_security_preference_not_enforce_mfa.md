# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ram_security_preference_not_enforce_mfa.md

---
title: RAM security preference does not enforce MFA login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RAM security preference does not enforce MFA
  login
---

# RAM security preference does not enforce MFA login

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dcda2d32-e482-43ee-a926-75eaabeaa4e0`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ram_security_preference#enforce_mfa_for_login)

### Description{% #description %}

`alicloud_ram_security_preference` must be defined and configured to enforce MFA login for `alicloud_ram_user` accounts. The rule detects when the `alicloud_ram_security_preference` resource is missing, when `enforce_mfa_for_login` is not defined, or when `enforce_mfa_for_login` is set to false. When any of these conditions occur, the policy reports the affected resource and suggests setting `enforce_mfa_for_login = true`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# Create a new RAM user.
resource "alicloud_ram_user" "user0" {
  name         = "user_test"
  display_name = "user_display_name"
  mobile       = "86-18688888888"
  email        = "hello.uuu@aaa.com"
  comments     = "yoyoyo"
  force        = true
}

resource "alicloud_ram_security_preference" "example0" {
  enable_save_mfa_ticket        = false
  allow_user_to_change_password = true
  enforce_mfa_for_login = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# Create a new RAM user.
resource "alicloud_ram_user" "user2" {
  name         = "user_test"
  display_name = "user_display_name"
  mobile       = "86-18688888888"
  email        = "hello.uuu@aaa.com"
  comments     = "yoyoyo"
  force        = true
}

resource "alicloud_ram_security_preference" "example2" {
  enable_save_mfa_ticket        = false
  allow_user_to_change_password = true
  enforce_mfa_for_login = false
}
```

```terraform
# this file does not return any result because inside the test folder exists at least one resource "alicloud_ram_security_preference" in the samples
#resource "alicloud_ram_user" "user3" {
#  name         = "user_test"
#  display_name = "user_display_name"
#  mobile       = "86-18688888888"
#  email        = "hello.uuu@aaa.com"
#  comments     = "yoyoyo"
#  force        = true
#}
```

```terraform
# Create a new RAM user.
resource "alicloud_ram_user" "user1" {
  name         = "user_test"
  display_name = "user_display_name"
  mobile       = "86-18688888888"
  email        = "hello.uuu@aaa.com"
  comments     = "yoyoyo"
  force        = true
}

resource "alicloud_ram_security_preference" "example1" {
  enable_save_mfa_ticket        = false
  allow_user_to_change_password = true
}
```
