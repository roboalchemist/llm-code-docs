# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/storage_account_not_using_latest_tls_encryption_version.md

---
title: Storage account not using latest TLS encryption version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Storage account not using latest TLS
  encryption version
---

# Storage account not using latest TLS encryption version

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8263f146-5e03-43e0-9cfe-db960d56d1e7`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account)

### Description{% #description %}

To ensure data transmitted to and from Azure storage accounts remains protected, it is important to enforce the use of the latest supported TLS encryption protocol. If the `min_tls_version` attribute is set to an outdated protocol such as `"TLS1_1"`, as seen below, the storage account may be vulnerable to known security exploits:

```
  min_tls_version = "TLS1_1"
```

To mitigate this risk, configure storage accounts to use at least TLS 1.2 by setting:

```
  min_tls_version = "TLS1_2"
```

Failing to enforce modern TLS versions can expose sensitive data in transit to interception or tampering by attackers.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_storage_account" "negative1" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  min_tls_version = "TLS1_2"

  tags = {
    environment = "staging"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_storage_account" "positive2" {
  name                     = "storageaccountname"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  min_tls_version = "TLS1_1"

  tags = {
    environment = "staging"
  }
}
```
