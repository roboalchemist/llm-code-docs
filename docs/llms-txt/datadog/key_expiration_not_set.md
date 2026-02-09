# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/key_expiration_not_set.md

---
title: Key expiration not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Key expiration not set
---

# Key expiration not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4d080822-5ee2-49a4-8984-68f3d4c890fc`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault_key)

### Description{% #description %}

To ensure cryptographic hygiene and limit risk exposure, all keys managed by Azure Key Vault should have an explicit expiration date set using the `expiration_date` attribute. Without an expiration, keys may remain valid indefinitely, increasing the likelihood of unauthorized access or misuse if the key is ever compromised. For example, a secure configuration includes `expiration_date`, as shown below:

```
resource "azurerm_key_vault_key" "example" {
  name             = "generated-certificate"
  key_vault_id     = azurerm_key_vault.example.id
  key_type         = "RSA"
  key_size         = 2048
  key_opts         = ["decrypt", "encrypt", "sign", "unwrapKey", "verify", "wrapKey"]
  expiration_date  = "2020-12-30T20:00:00Z"
}
```

Failure to set this attribute can result in persistent, potentially stale keys that remain active past their intended lifecycle, increasing the attack surface.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_key_vault_key" "negative1" {
    name         = "generated-certificate"
    key_vault_id = azurerm_key_vault.example.id
    key_type     = "RSA"
    key_size     = 2048

    key_opts = [
    "decrypt",
    "encrypt",
    "sign",
    "unwrapKey",
    "verify",
    "wrapKey",
    ]
  expiration_date = "2020-12-30T20:00:00Z"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_key_vault_key" "positive1" {
    name         = "generated-certificate"
    key_vault_id = azurerm_key_vault.example.id
    key_type     = "RSA"
    key_size     = 2048

    key_opts = [
    "decrypt",
    "encrypt",
    "sign",
    "unwrapKey",
    "verify",
    "wrapKey",
    ]
}
```
