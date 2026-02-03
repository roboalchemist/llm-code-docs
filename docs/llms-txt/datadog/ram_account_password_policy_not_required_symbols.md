# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ram_account_password_policy_not_required_symbols.md

---
title: RAM account password policy does not require symbols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > RAM account password policy does not require
  symbols
---

# RAM account password policy does not require symbols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `41a38329-d81b-4be4-aef4-55b2615d3282`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Low

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/ram_account_password_policy#require_symbols)

### Description{% #description %}

RAM account password security should require at least one symbol. Specifically, the `alicloud_ram_account_password_policy` resource must have the `require_symbols` attribute set to `true`. This rule flags cases where `require_symbols` is `false` as an `IncorrectValue` issue and suggests replacing it with `true`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_ram_account_password_policy" "corporate1" {
  minimum_password_length      = 9
  require_lowercase_characters = false
  require_uppercase_characters = false
  require_numbers              = false
  require_symbols              = true
  hard_expiry                  = true
  max_password_age             = 12
  password_reuse_prevention    = 5
  max_login_attempts           = 3
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_ram_account_password_policy" "corporate2" {
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
