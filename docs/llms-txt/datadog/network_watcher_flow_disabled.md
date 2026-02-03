# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/network_watcher_flow_disabled.md

---
title: Network watcher flow disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Network watcher flow disabled
---

# Network watcher flow disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b90842e5-6779-44d4-9760-972f4c03ba1c`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_watcher_flow_log)

### Description{% #description %}

This check ensures that the `enabled` attribute in the `azurerm_network_watcher_flow_log` resource is set to `true`, which activates flow logging for the associated network security group. Disabling flow logs by setting `enabled = false` can result in a lack of visibility into network traffic, making it difficult to detect and investigate security incidents and unauthorized access attempts in Azure environments. To maintain proper monitoring and auditing, the flow log should be enabled, as shown below:

```
resource "azurerm_network_watcher_flow_log" "secure_example" {
  network_watcher_name       = azurerm_network_watcher.test.name
  resource_group_name        = azurerm_resource_group.test.name
  network_security_group_id  = azurerm_network_security_group.test.id
  storage_account_id         = azurerm_storage_account.test.id
  enabled                    = true

  retention_policy {
    enabled = true
    days    = 7
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_network_watcher_flow_log" "negative1" {
  network_watcher_name = azurerm_network_watcher.test.name
  resource_group_name  = azurerm_resource_group.test.name

  network_security_group_id = azurerm_network_security_group.test.id
  storage_account_id        = azurerm_storage_account.test.id
  enabled                   = true

  retention_policy {
    enabled = true
    days    = 7
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_network_watcher_flow_log" "positive1" {
  network_watcher_name = azurerm_network_watcher.test.name
  resource_group_name  = azurerm_resource_group.test.name

  network_security_group_id = azurerm_network_security_group.test.id
  storage_account_id        = azurerm_storage_account.test.id
  enabled                   = false

  retention_policy {
    enabled = true
    days    = 7
  }
}
```
