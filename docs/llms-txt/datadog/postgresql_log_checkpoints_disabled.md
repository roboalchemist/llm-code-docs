# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/postgresql_log_checkpoints_disabled.md

---
title: PostgreSQL log checkpoints disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > PostgreSQL log checkpoints disabled
---

# PostgreSQL log checkpoints disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3790d386-be81-4dcf-9850-eaa7df6c10d9`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_configuration)

### Description{% #description %}

The PostgreSQL `log_checkpoints` parameter controls whether checkpoint activities are logged, which is critical for monitoring and troubleshooting database performance and reliability. If `log_checkpoints` is set to `off`, important information about checkpoint events will not be recorded, making it more difficult to detect or respond to potential issues or attacks. To mitigate this risk, the parameter should be enabled, as shown below:

```
resource "azurerm_postgresql_configuration" "secure_example" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "on"
}
```

Failing to enable this logging may leave administrators unaware of problems that can impact data durability or signal malicious activity, increasing the risk of unnoticed outages or data loss.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_postgresql_configuration" "negative1" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "on"
}

resource "azurerm_postgresql_configuration" "negative2" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "On"
}

resource "azurerm_postgresql_configuration" "negative3" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "ON"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_postgresql_configuration" "positive1" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "off"
}

resource "azurerm_postgresql_configuration" "positive2" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "Off"
}

resource "azurerm_postgresql_configuration" "positive3" {
    name                = "log_checkpoints"
    resource_group_name = data.azurerm_resource_group.example.name
    server_name         = azurerm_postgresql_server.example.name
    value               = "OFF"
}
```
