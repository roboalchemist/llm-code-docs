# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/storage_account_not_forcing_https.md

---
title: Storage account not forcing HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Storage account not forcing HTTPS
---

# Storage account not forcing HTTPS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `12944ec4-1fa0-47be-8b17-42a034f937c2`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account#https_traffic_only_enabled-1)

### Description{% #description %}

Storage accounts should enforce the use of HTTPS by setting the `https_traffic_only_enabled` attribute to `true` in the Terraform configuration. Allowing HTTP traffic (`https_traffic_only_enabled = false`) exposes sensitive data to interception and man-in-the-middle attacks during transit. A secure configuration should look like the following:

```
resource "azurerm_storage_account" "secure_example" {
  // ... other configuration ...
  https_traffic_only_enabled = true
}
```

Enforcing HTTPS ensures all connections to the storage account are encrypted, protecting data integrity and confidentiality.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_storage_account" "positive2" {
  name                     = "example2"
  resource_group_name      = data.azurerm_resource_group.example.name
  location                 = data.azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  # will not flag because https_traffic_only_enabled is set to true by default so we do not error
}
```

```terraform
resource "azurerm_storage_account" "negative1" {
  name                       = "example"
  resource_group_name        = data.azurerm_resource_group.example.name
  location                   = data.azurerm_resource_group.example.location
  account_tier               = "Standard"
  account_replication_type   = "GRS"
  https_traffic_only_enabled = true # Set to true as desired
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_storage_account" "positive1" {
  name                       = "example1"
  resource_group_name        = data.azurerm_resource_group.example.name
  location                   = data.azurerm_resource_group.example.location
  account_tier               = "Standard"
  account_replication_type   = "GRS"
  https_traffic_only_enabled = false
}
```
