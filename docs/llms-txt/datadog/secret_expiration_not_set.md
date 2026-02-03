# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/secret_expiration_not_set.md

---
title: Secret expiration not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Secret expiration not set
---

# Secret expiration not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dfa20ffa-f476-428f-a490-424b41e91c7f`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/key_vault_secret)

### Description{% #description %}

Secrets stored in Azure Key Vault using the `azurerm_key_vault_secret` resource should always have an `expiration_date` set to ensure that sensitive credentials are not usable indefinitely. Failing to set an expiration date may result in forgotten or stale secrets lingering in your environment, increasing the risk of those secrets being misused if an account is compromised or a process changes. For a more secure configuration, explicitly specify the `expiration_date` attribute, as shown below:

```
resource "azurerm_key_vault_secret" "example" {
    name             = "api-key"
    value            = "supersecret"
    key_vault_id     = azurerm_key_vault.example.id

    expiration_date  = "2025-01-01T00:00:00Z"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_key_vault_secret" "negative1" {
    name         = "secret-sauce"
    value        = "szechuan"
    key_vault_id = azurerm_key_vault.example.id

    tags = {
    environment = "Production"
    }
    expiration_date = "2020-12-30T20:00:00Z"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_key_vault_secret" "positive1" {
    name         = "secret-sauce"
    value        = "szechuan"
    key_vault_id = azurerm_key_vault.example.id

    tags = {
    environment = "Production"
    }
}
```
