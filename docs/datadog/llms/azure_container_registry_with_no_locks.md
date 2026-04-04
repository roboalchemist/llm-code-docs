# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/azure_container_registry_with_no_locks.md

---
title: Azure Container Registry with no locks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Azure Container Registry with no locks
---

# Azure Container Registry with no locks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a187ac47-8163-42ce-8a63-c115236be6fb`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_registry)

### Description{% #description %}

Azure Container Registry without proper management locks is vulnerable to accidental deletion or modification, which can lead to service disruptions, data loss, and potentially severe business impact. Management locks provide an additional layer of protection by preventing unauthorized or unintended changes to critical resources. To properly secure an Azure Container Registry, ensure the management lock's scope correctly references the container registry resource, as shown below:

```
resource "azurerm_container_registry" "acr" {
  name = "containerRegistry1"
  resource_group_name = azurerm_resource_group.rg.name
  location = azurerm_resource_group.rg.location
  sku = "Standard"
  admin_enabled = false
}

resource "azurerm_management_lock" "public-ip" {
  name = "resource-ip"
  scope = azurerm_container_registry.acr.id
  lock_level = "CanNotDelete"
  notes = "Locked because it's needed by a third-party"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_container_registry" "acr" {
name = "containerRegistry1"
resource_group_name = azurerm_resource_group.rg.name
location = azurerm_resource_group.rg.location
sku = "Standard"
admin_enabled = false
}


resource "azurerm_management_lock" "public-ip" {
name = "resource-ip"
scope = azurerm_container_registry.acr.id
lock_level = "CanNotDelete"
notes = "Locked because it's needed by a third-party"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_container_registry" "acr" {
name = "containerRegistry1"
resource_group_name = azurerm_resource_group.rg.name
location = azurerm_resource_group.rg.location
sku = "Standard"
admin_enabled = false
}


resource "azurerm_management_lock" "public-ip" {
name = "resource-ip"
scope = azurerm_container_registry.acr1.id
lock_level = "CanNotDelete"
notes = "Locked because it's needed by a third-party"
}
```
