# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/postgresql_server_infrastructure_encryption_disabled.md

---
title: PostgreSQL server infrastructure encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > PostgreSQL server infrastructure encryption
  disabled
---

# PostgreSQL server infrastructure encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `6425c98b-ca4e-41fe-896a-c78772c131f8`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_server#infrastructure_encryption_enabled)

### Description{% #description %}

PostgreSQL Server infrastructure encryption provides an additional layer of protection for data at rest, beyond the default storage encryption. If the `infrastructure_encryption_enabled` attribute is set to `false` in the Terraform `azurerm_postgresql_server` resource, sensitive data may be exposed in the event of unauthorized access to underlying disks or snapshots. To secure the configuration, set `infrastructure_encryption_enabled = true`.

This ensures that the PostgreSQL server uses Azure's strong encryption mechanisms to protect data at the infrastructure level, significantly reducing the risk of data compromise.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_postgresql_server" "negative" {
  name                = "example-psqlserver"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  administrator_login          = "psqladminun"
  administrator_login_password = "H@Sh1CoR3!"

  sku_name   = "GP_Gen5_4"
  version    = "9.6"
  storage_mb = 640000

  backup_retention_days        = 7
  geo_redundant_backup_enabled = true
  auto_grow_enabled            = true

  public_network_access_enabled    = false
  ssl_enforcement_enabled          = true
  ssl_minimal_tls_version_enforced = "TLS1_2"

  infrastructure_encryption_enabled = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_postgresql_server" "positive2" {
  name                = "example-psqlserver"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  administrator_login          = "psqladminun"
  administrator_login_password = "H@Sh1CoR3!"

  sku_name   = "GP_Gen5_4"
  version    = "9.6"
  storage_mb = 640000

  backup_retention_days        = 7
  geo_redundant_backup_enabled = true
  auto_grow_enabled            = true

  public_network_access_enabled    = false
  ssl_enforcement_enabled          = true
  ssl_minimal_tls_version_enforced = "TLS1_2"
}
```

```terraform
resource "azurerm_postgresql_server" "positive1" {
  name                = "example-psqlserver"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  administrator_login          = "psqladminun"
  administrator_login_password = "H@Sh1CoR3!"

  sku_name   = "GP_Gen5_4"
  version    = "9.6"
  storage_mb = 640000

  backup_retention_days        = 7
  geo_redundant_backup_enabled = true
  auto_grow_enabled            = true

  public_network_access_enabled    = false
  ssl_enforcement_enabled          = true
  ssl_minimal_tls_version_enforced = "TLS1_2"

  infrastructure_encryption_enabled = false
}
```
