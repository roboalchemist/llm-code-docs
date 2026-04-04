# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/cosmos_db_account_without_tags.md

---
title: Cosmos DB account without tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cosmos DB account without tags
---

# Cosmos DB account without tags

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `56dad03e-e94f-4dd6-93a4-c253a03ff7a0`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Build Process

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_account)

### Description{% #description %}

Cosmos DB accounts should be configured with appropriate tags to ensure resources are identifiable, manageable, and auditable within an Azure environment. Without tags, as shown below, critical contextual informationâsuch as environment, owner, or cost centerâis missing, making resource management and cost tracking difficult:

```
resource "azurerm_cosmosdb_account" "example" {
  // ...other configuration...
}
```

By specifying the `tags` attribute, as demonstrated here, organizations can better enforce governance, automate resource management, and control costs:

```
resource "azurerm_cosmosdb_account" "example" {
  // ...other configuration...
  tags = {
    Environment = "Production"
    Owner       = "AppTeam"
  }
}
```

Leaving tags unconfigured can lead to unmanaged resources, increased risk of misconfiguration, and operational inefficiencies.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_cosmosdb_account" "negative1" {
  name                = "tfex-cosmos-db-${random_integer.ri.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  tags                = "tag_1"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_cosmosdb_account" "positive1" {
  name                = "tfex-cosmos-db-${random_integer.ri.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
}
```
