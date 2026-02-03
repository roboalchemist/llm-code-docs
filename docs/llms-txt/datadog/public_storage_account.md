# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/public_storage_account.md

---
title: Public storage account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Public storage account
---

# Public storage account

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `17f75827-0684-48f4-8747-61129c7e4198`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account)

### Description{% #description %}

Public Azure storage accounts represent a significant security risk as they potentially expose sensitive data to unauthorized access from the internet. When storage accounts have their default_action set to `Allow` or include overly permissive IP rules (`0.0.0.0/0`), attackers can potentially access, exfiltrate, or manipulate stored data including PII, credentials, or business-critical information.

To secure storage accounts, configure network rules with `default_action` set to `Deny` and explicitly allow only specific IP addresses or virtual networks that require access. For example:

```
resource "azurerm_storage_account" "secure_example" {
  // Required properties
  name                = "storageaccountname"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  account_tier        = "Standard"
  account_replication_type = "LRS"

  network_rules {
    default_action             = "Deny"
    ip_rules                   = ["100.0.0.1"]  // Only specific IPs, not 0.0.0.0/0
    virtual_network_subnet_ids = [azurerm_subnet.example.id]
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_storage_account" "negative6" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
}
```

```terraform
resource "azurerm_storage_account" "negative5" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  allow_blob_public_access = false
}
```

```terraform
resource "azurerm_storage_account" "negative1" {
  name                = "storageaccountname"
  resource_group_name = azurerm_resource_group.example.name

  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  network_rules {
    default_action             = "Deny"
    ip_rules                   = ["100.0.0.1"]
    virtual_network_subnet_ids = [azurerm_subnet.example.id]
  }

  tags = {
    environment = "staging"
  }
}

resource "azurerm_storage_account_network_rules" "negative2" {
  resource_group_name  = azurerm_resource_group.test.name
  storage_account_name = azurerm_storage_account.test.name

  default_action             = "Allow"
  ip_rules                   = ["127.0.0.1"]
  virtual_network_subnet_ids = [azurerm_subnet.test.id]
  bypass                     = ["Metrics"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_storage_account" "positive5" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  allow_blob_public_access = true
}
```

```terraform
resource "azurerm_storage_account" "positive1" {
  name                = "storageaccountname"
  resource_group_name = azurerm_resource_group.example.name

  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  network_rules {
    default_action             = "Deny"
    ip_rules                   = ["0.0.0.0/0"]
    virtual_network_subnet_ids = [azurerm_subnet.example.id]
  }

  tags = {
    environment = "staging"
  }
}

resource "azurerm_storage_account" "positive2" {
  name                = "storageaccountname"
  resource_group_name = azurerm_resource_group.example.name

  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  network_rules {
    default_action             = "Allow"
    virtual_network_subnet_ids = [azurerm_subnet.example.id]
  }

  tags = {
    environment = "staging"
  }
}

resource "azurerm_storage_account_network_rules" "positive3" {
  resource_group_name  = azurerm_resource_group.test.name
  storage_account_name = azurerm_storage_account.test.name

  default_action             = "Allow"
  ip_rules                   = ["0.0.0.0/0"]
  virtual_network_subnet_ids = [azurerm_subnet.test.id]
  bypass                     = ["Metrics"]
}

resource "azurerm_storage_account_network_rules" "positive4" {
  resource_group_name  = azurerm_resource_group.test.name
  storage_account_name = azurerm_storage_account.test.name

  default_action             = "Allow"
  virtual_network_subnet_ids = [azurerm_subnet.test.id]
  bypass                     = ["Metrics"]
}
```
