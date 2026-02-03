# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/sql_server_alert_email_disabled.md

---
title: SQL server alert email disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SQL server alert email disabled
---

# SQL server alert email disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `55975007-f6e7-4134-83c3-298f1fe4b519`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/mssql_server_security_alert_policy#email_account_admins)

### Description{% #description %}

SQL Server alert emails should be enabled to ensure that administrators are promptly notified of suspicious activities or potential security threats, such as SQL injection or data exfiltration attempts. Without setting the `email_account_admins` attribute to `true` in the `azurerm_mssql_server_security_alert_policy` resource, critical security alerts may go unnoticed, delaying incident response and potentially increasing the risk of a successful attack. A secure configuration is shown below:

```
resource "azurerm_mssql_server_security_alert_policy" "example" {
  resource_group_name        = azurerm_resource_group.example.name
  server_name                = azurerm_sql_server.example.name
  state                      = "Enabled"
  storage_endpoint           = azurerm_storage_account.example.primary_blob_endpoint
  storage_account_access_key = azurerm_storage_account.example.primary_access_key
  disabled_alerts = [
    "Sql_Injection",
    "Data_Exfiltration"
  ]
  retention_days = 20
  email_account_admins = true
}
```

Enabling alert emails reduces the risk of missing critical security events by ensuring they are communicated in real time to account administrators.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_mssql_server_security_alert_policy" "negative" {
  resource_group_name        = azurerm_resource_group.example.name
  server_name                = azurerm_sql_server.example.name
  state                      = "Enabled"
  storage_endpoint           = azurerm_storage_account.example.primary_blob_endpoint
  storage_account_access_key = azurerm_storage_account.example.primary_access_key
  disabled_alerts = [
    "Sql_Injection",
    "Data_Exfiltration"
  ]
  retention_days = 20
  email_account_admins = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_mssql_server_security_alert_policy" "positive2" {
  resource_group_name        = azurerm_resource_group.example.name
  server_name                = azurerm_sql_server.example.name
  state                      = "Enabled"
  storage_endpoint           = azurerm_storage_account.example.primary_blob_endpoint
  storage_account_access_key = azurerm_storage_account.example.primary_access_key
  disabled_alerts = [
    "Sql_Injection",
    "Data_Exfiltration"
  ]
  retention_days = 20
  email_account_admins = false
}
```

```terraform
resource "azurerm_mssql_server_security_alert_policy" "positive1" {
  resource_group_name        = azurerm_resource_group.example.name
  server_name                = azurerm_sql_server.example.name
  state                      = "Enabled"
  storage_endpoint           = azurerm_storage_account.example.primary_blob_endpoint
  storage_account_access_key = azurerm_storage_account.example.primary_access_key
  disabled_alerts = [
    "Sql_Injection",
    "Data_Exfiltration"
  ]
  retention_days = 20
}
```
