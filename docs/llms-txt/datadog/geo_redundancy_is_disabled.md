# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/geo_redundancy_is_disabled.md

---
title: Geo redundancy is disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Geo redundancy is disabled
---

# Geo redundancy is disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8b042c30-e441-453f-b162-7696982ebc58`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_server)

### Description{% #description %}

Geo-redundant backups should be enabled on Azure PostgreSQL servers to ensure critical data is protected and recoverable even if a regional outage occurs. The `geo_redundant_backup_enabled` attribute should be set to `true` for high availability; otherwise, setting it to `false` can leave backups vulnerable to loss in disaster recovery scenarios. For example, a secure configuration would look like the following:

```gdscript3
resource "azurerm_postgresql_server" "example" {
    name                = "dbserver"
    location            = "usgovvirginia"
    resource_group_name = azurerm_resource_group.jira_rg.name

    sku_name   = "GP_Gen5_4"
    version    = "9.6"
    storage_mb = 640000

    backup_retention_days        = var.jira_postgre_data_retention
    geo_redundant_backup_enabled = true
    auto_grow_enabled            = true

    administrator_login          = var.mp_db_username
    administrator_login_password = azurerm_key_vault_secret.db_pswd.value
    ssl_enforcement_enabled      = true

    tags                         = local.postgresqlserver_tags
}
```

Without geo-redundant backups enabled, business-critical data may become unrecoverable if the primary region experiences a catastrophic failure, risking significant data loss and service disruption.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_postgresql_server" "negative1" {
    name                = "dbserver"
    location            = "usgovvirginia"
    resource_group_name = azurerm_resource_group.jira_rg.name

    sku_name   = "GP_Gen5_4"
    version    = "9.6"
    storage_mb = 640000

    backup_retention_days        = var.jira_postgre_data_retention
    geo_redundant_backup_enabled = true
    auto_grow_enabled            = true

    administrator_login          = var.mp_db_username
    administrator_login_password = azurerm_key_vault_secret.db_pswd.value
    ssl_enforcement_enabled      = false

    tags                         = local.postgresqlserver_tags
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform

resource "azurerm_postgresql_server" "positive1" {
    name                = "dbserver"
    location            = "usgovvirginia"
    resource_group_name = azurerm_resource_group.jira_rg.name

    sku_name   = "GP_Gen5_4"
    version    = "9.6"
    storage_mb = 640000

    backup_retention_days        = var.jira_postgre_data_retention
    auto_grow_enabled            = true

    administrator_login          = var.mp_db_username
    administrator_login_password = azurerm_key_vault_secret.db_pswd.value
    ssl_enforcement_enabled      = true

    tags                         = local.postgresqlserver_tags
}

resource "azurerm_postgresql_server" "positive2" {
    name                = "dbserver"
    location            = "usgovvirginia"
    resource_group_name = azurerm_resource_group.jira_rg.name

    sku_name   = "GP_Gen5_4"
    version    = "9.6"
    storage_mb = 640000

    backup_retention_days        = var.jira_postgre_data_retention
    geo_redundant_backup_enabled = false
    auto_grow_enabled            = true

    administrator_login          = var.mp_db_username
    administrator_login_password = azurerm_key_vault_secret.db_pswd.value
    ssl_enforcement_enabled      = false

    tags                         = local.postgresqlserver_tags
}
```
