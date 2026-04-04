# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/postgresql_log_duration_not_set.md

---
title: PostgreSQL log duration not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > PostgreSQL log duration not set
---

# PostgreSQL log duration not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `16e0879a-c4ae-4ff8-a67d-a2eed5d67b8f`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_configuration)

### Description{% #description %}

The PostgreSQL server parameter `log_duration` should be set to `ON` to ensure that the duration of each completed SQL statement is logged. Without this setting enabled (for example, if `value = "off"` is used in the `azurerm_postgresql_configuration` resource), critical visibility into query performance and potential issues will be lost, making it difficult to identify slow-running queries or investigate security incidents. Setting `log_duration` to `ON`, as shown below, enables enhanced monitoring and auditing capabilities for your database:

```
resource "azurerm_postgresql_configuration" "secure_example" {
    name                = "log_duration"
    resource_group_name = "example_resource_group_name"
    server_name         = "example_server_name"
    value               = "ON"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "azurerm_postgresql_configuration" "negative1" {
    name                = "log_duration"
    resource_group_name = "example1_resource_group_name"
    server_name         = "example1_server_name"
    value               = "on"
}

resource "azurerm_postgresql_configuration" "negative2" {
    name                = "log_duration"
    resource_group_name = "example2_resource_group_name"
    server_name         = "example2_server_name"
    value               = "On"
}

resource "azurerm_postgresql_configuration" "negative3" {
    name                = "log_duration"
    resource_group_name = "example3_resource_group_name"
    server_name         = "example3_server_name"
    value               = "ON"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
resource "azurerm_postgresql_configuration" "positive1" {
    name                = "log_duration"
    resource_group_name = "example1_resource_group_name"
    server_name         = "example1_server_name"
    value               = "off"
}

resource "azurerm_postgresql_configuration" "positive2" {
    name                = "log_duration"
    resource_group_name = "example2_resource_group_name"
    server_name         = "example2_server_name"
    value               = "Off"
}

resource "azurerm_postgresql_configuration" "positive3" {
    name                = "log_duration"
    resource_group_name = "example3_resource_group_name"
    server_name         = "example3_server_name"
    value               = "OFF"
}
```
