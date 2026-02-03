# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/azure_cognitive_search_public_network_access_enabled.md

---
title: Azure Cognitive Search public network access enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Azure Cognitive Search public network access
  enabled
---

# Azure Cognitive Search public network access enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4a9e0f00-0765-4f72-a0d4-d31110b78279`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/search_service#public_network_access_enabled)

### Description{% #description %}

Allowing public network access to Azure Cognitive Search exposes the service to the internet, increasing the risk of unauthorized access and data exposure. In Terraform, this is controlled by the `public_network_access_enabled` attribute; setting this attribute to `true` permits public connections, while setting it to `false` restricts access to trusted, private networks only. For example, a secure configuration would look like the following:

```
resource "azurerm_search_service" "example" {
  name                          = "example-search-service"
  resource_group_name           = azurerm_resource_group.example.name
  location                      = azurerm_resource_group.example.location
  sku                           = "standard"
  public_network_access_enabled = false
}
```

Leaving public access enabled may allow attackers to enumerate, access, or exfiltrate sensitive search indexes and data.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_search_service" "example" {
  name                = "example-search-service"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku                 = "standard"
  public_network_access_enabled = false
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_search_service" "positive2" {
  name                = "example-search-service"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku                 = "standard"
}
```

```terraform
resource "azurerm_search_service" "positive1" {
  name                = "example-search-service"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  sku                 = "standard"
  public_network_access_enabled = true
}
```
