# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ram_password_security_policy_not_require_at_least_one_lowercase_character.md

---
title: RAM account password policy not require at least one lowercase character
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RAM account password policy not require at
  least one lowercase character
---

# RAM account password policy not require at least one lowercase character

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `89143358-cec6-49f5-9392-920c591c669c`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ram_account_password_policy#require_lowercase_characters)

### Description{% #description %}

The RAM account password policy (`alicloud_ram_account_password_policy`) must set `require_lowercase_characters` to `true`. This ensures that account passwords include at least one lowercase character to meet complexity requirements. Resources with `require_lowercase_characters` set to `false` are non-compliant and should be updated to `true`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ram_account_password_policy" "corporate" {
  minimum_password_length      = 9
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
  require_lowercase_characters = true
  require_uppercase_characters = false
  require_numbers              = false
  require_symbols              = false
  hard_expiry                  = true
  max_password_age             = 12
  password_reuse_prevention    = 5
  max_login_attempts           = 3
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

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
