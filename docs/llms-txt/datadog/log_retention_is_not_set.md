# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/log_retention_is_not_set.md

---
title: Log retention is not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Log retention is not set
---

# Log retention is not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ffb02aca-0d12-475e-b77c-a726f7aeff4b`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_configuration)

### Description{% #description %}

The `log_retention` server parameter in Azure PostgreSQL determines whether database logs are retained, which is essential for auditing and troubleshooting purposes. If this parameter is set to `OFF`, as shown below, log data will not be persisted, potentially hindering investigations into security incidents or operational issues:

```
resource "azurerm_postgresql_configuration" "example" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "OFF"
}
```

To address this, ensure that `log_retention` is set to `ON`, as in the configuration below, so that important logs are retained and available for review:

```
resource "azurerm_postgresql_configuration" "example" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "ON"
}
```

Failing to enable log retention can result in loss of critical data needed for compliance, monitoring, and incident response.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_postgresql_configuration" "negative1" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "on"
}

resource "azurerm_postgresql_configuration" "negative2" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "On"
}

resource "azurerm_postgresql_configuration" "negative3" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "ON"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_postgresql_configuration" "positive1" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "off"
}

resource "azurerm_postgresql_configuration" "positive2" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "Off"
}

resource "azurerm_postgresql_configuration" "positive3" {
    name                = "log_retention"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "OFF"
}
```
