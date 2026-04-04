# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/postgresql_log_connections_not_set.md

---
title: PostgreSQL log connections not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > PostgreSQL log connections not set
---

# PostgreSQL log connections not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c640d783-10c5-4071-b6c1-23507300d333`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_configuration)

### Description{% #description %}

The PostgreSQL server parameter `log_connections` should be set to `ON` to ensure that all connection attempts, whether successful or not, are logged. Without this setting, unauthorized or suspicious connection attempts can go undetected, making it difficult to identify potential security incidents or troubleshoot access issues. For a secure configuration in Terraform, set the `value` attribute to `"on"`, as shown below:

```
resource "azurerm_postgresql_configuration" "secure" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "on"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_postgresql_configuration" "negative1" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "on"
}

resource "azurerm_postgresql_configuration" "negative2" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "On"
}

resource "azurerm_postgresql_configuration" "negative3" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "ON"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_postgresql_configuration" "positive1" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "off"
}

resource "azurerm_postgresql_configuration" "positive2" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "Off"
}

resource "azurerm_postgresql_configuration" "positive3" {
    name                = "log_connections"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "OFF"
}
```
