# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ram_account_password_policy_not_required_minimum_length.md

---
title: RAM account password policy does not enforce minimum password length
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RAM account password policy does not enforce
  minimum password length
---

# RAM account password policy does not enforce minimum password length

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a9dfec39-a740-4105-bbd6-721ba163c053`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ram_account_password_policy#minimum_password_length)

### Description{% #description %}

The RAM account password policy must define `minimum_password_length` and set it to `14` or greater. If the attribute is missing, the policy is non-compliant and should include `minimum_password_length = 14`. This rule reports `IncorrectValue` when the attribute is defined but below `14`, and `MissingAttribute` when it is not defined.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ram_account_password_policy" "corporate" {
  minimum_password_length      = 14
  require_lowercase_characters = false
  require_uppercase_characters = false
  require_numbers              = false
  require_symbols              = false
  hard_expiry                  = true
  max_password_age             = 14
  password_reuse_prevention    = 5
  max_login_attempts           = 3
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_ram_account_password_policy" "corporate" {
  require_lowercase_characters = false
  require_uppercase_characters = false
  require_numbers              = false
  require_symbols              = false
  hard_expiry                  = true
  max_password_age             = 12
  password_reuse_prevention    = 5
  max_login_attempts           = 3
}
```

```terraform
resource "alicloud_ram_account_password_policy" "corporate" {
  minimum_password_length      = 9
  require_lowercase_characters = false
  require_uppercase_characters = false
  require_numbers              = false
  require_symbols              = false
  hard_expiry                  = true
  max_password_age             = 12
  password_reuse_prevention    = 5
  max_login_attempts           = 3
}
```
