# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/mysql_ssl_connection_disabled.md

---
title: MySQL SSL connection disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > MySQL SSL connection disabled
---

# MySQL SSL connection disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `73e42469-3a86-4f39-ad78-098f325b4e9f`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/3.6.0/docs/resources/mysql_server)

### Description{% #description %}

To ensure data transmitted between clients and the MySQL server is secure, the `ssl_enforcement_enabled` attribute in the `azurerm_mysql_server` resource should be set to `true`. If `ssl_enforcement_enabled` is set to `false`, as shown below, database connections can occur over unencrypted channels, potentially exposing sensitive information such as credentials and application data to interception and misuse.

```
resource "azurerm_mysql_server" "example" {
  ...
  ssl_enforcement_enabled = false
}
```

Enabling SSL enforcement mitigates this risk by ensuring that all clients must connect using SSL, protecting data in transit.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_mysql_server" "negative1" {
  name                = "webflux-mysql-${var.environment}${random_integer.rnd_int.result}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  administrator_login          = "webflux-${var.environment}"
  administrator_login_password = random_string.password.result

  sku_name   = "B_Gen5_2"
  storage_mb = 5120
  version    = "5.7"

  auto_grow_enabled                 = true
  backup_retention_days             = 7
  infrastructure_encryption_enabled = true
  public_network_access_enabled     = true
  ssl_enforcement_enabled           = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_mysql_server" "positive1" {
  name                = "webflux-mysql-${var.environment}${random_integer.rnd_int.result}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  administrator_login          = "webflux-${var.environment}"
  administrator_login_password = random_string.password.result

  sku_name   = "B_Gen5_2"
  storage_mb = 5120
  version    = "5.7"

  auto_grow_enabled                 = true
  backup_retention_days             = 7
  infrastructure_encryption_enabled = true
  public_network_access_enabled     = true
  ssl_enforcement_enabled           = false
}
```
