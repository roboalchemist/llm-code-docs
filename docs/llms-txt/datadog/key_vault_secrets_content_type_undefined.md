# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/key_vault_secrets_content_type_undefined.md

---
title: Key Vault secrets content type undefined
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Key Vault secrets content type undefined
---

# Key Vault secrets content type undefined

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f8e08a38-fc6e-4915-abbe-a7aadf1d59ef`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault_secret#content_type)

### Description{% #description %}

Key Vault secrets in Azure should explicitly set the `content_type` attribute to define the type and intended usage of the stored secret. Omitting `content_type` can lead to poor secret management practices, making it more difficult to identify and handle secrets correctly, which increases the risk of accidental misuse or disclosure. A secure Terraform configuration includes the `content_type` attribute, as shown below:

```
resource "azurerm_key_vault_secret" "example" {
  name         = "db-password"
  value        = "MySecurePassword123"
  key_vault_id = azurerm_key_vault.example.id
  content_type = "password"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_key_vault_secret" "negative" {
  name         = "secret-sauce"
  value        = "szechuan"
  key_vault_id = azurerm_key_vault.example.id
  content_type = "password"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_key_vault_secret" "positive" {
  name         = "secret-sauce"
  value        = "szechuan"
  key_vault_id = azurerm_key_vault.example.id
}
```
