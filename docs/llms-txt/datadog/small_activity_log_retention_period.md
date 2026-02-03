# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/small_activity_log_retention_period.md

---
title: Small activity log retention period
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Small activity log retention period
---

# Small activity log retention period

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2b856bf9-8e8c-4005-875f-303a8cba3918`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/3.6.0/docs/resources/monitor_log_profile)

### Description{% #description %}

This check ensures that the `retention_policy.days` attribute for the `azurerm_monitor_log_profile` resource in Terraform is set to 365 days or greater. Insufficient log retention (for example, `days = 7` or leaving the value unset) can result in the loss of valuable activity logs, limiting the ability to investigate incidents or meet audit requirements. To address this, configure the retention policy to at least 365 days, as shown below:

```
retention_policy {
  enabled = true
  days    = 367
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_monitor_log_profile" "negative1" {
  name = "default"

  categories = [
    "Action",
    "Delete",
    "Write",
  ]

  locations = [
    "westus",
    "global",
  ]

  servicebus_rule_id = "${azurerm_eventhub_namespace.example.id}/authorizationrules/RootManageSharedAccessKey"
  storage_account_id = azurerm_storage_account.example.id

  retention_policy {
    enabled = true
    days    = 367
  }
}

resource "azurerm_monitor_log_profile" "negative2" {
  name = "default"

  categories = [
    "Action",
    "Delete",
    "Write",
  ]

  locations = [
    "westus",
    "global",
  ]

  servicebus_rule_id = "${azurerm_eventhub_namespace.example.id}/authorizationrules/RootManageSharedAccessKey"
  storage_account_id = azurerm_storage_account.example.id

  retention_policy {
    enabled = true
    days    = 0
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_monitor_log_profile" "positive1" {
  name = "default"

  categories = [
    "Action",
    "Delete",
    "Write",
  ]

  locations = [
    "westus",
    "global",
  ]

  servicebus_rule_id = "${azurerm_eventhub_namespace.example.id}/authorizationrules/RootManageSharedAccessKey"
  storage_account_id = azurerm_storage_account.example.id

  retention_policy {
    enabled = true
    days    = 7
  }
}

resource "azurerm_monitor_log_profile" "positive2" {
  name = "default"

  categories = [
    "Action",
    "Delete",
    "Write",
  ]

  locations = [
    "westus",
    "global",
  ]

  servicebus_rule_id = "${azurerm_eventhub_namespace.example.id}/authorizationrules/RootManageSharedAccessKey"
  storage_account_id = azurerm_storage_account.example.id

  retention_policy {
    enabled = true
  }
}

resource "azurerm_monitor_log_profile" "positive3" {
  name = "default"

  categories = [
    "Action",
    "Delete",
    "Write",
  ]

  locations = [
    "westus",
    "global",
  ]

  servicebus_rule_id = "${azurerm_eventhub_namespace.example.id}/authorizationrules/RootManageSharedAccessKey"
  storage_account_id = azurerm_storage_account.example.id

  retention_policy {
    enabled = false
  }
}
```
