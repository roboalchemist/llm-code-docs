# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/function_app_http2_disabled.md

---
title: Function App HTTP2 disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Function App HTTP2 disabled
---

# Function App HTTP2 disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ace823d1-4432-4dee-945b-cdf11a5a6bd0`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/function_app#http2_enabled)

### Description{% #description %}

Enabling HTTP/2 for Azure Function Apps improves security and performance by providing better encryption and more efficient use of network resources compared to HTTP/1.1. If the `http2_enabled` attribute is not set to `true` in the `site_config` block, as shown below, the Function App defaults to HTTP/1.1, exposing it to potential vulnerabilities such as protocol downgrade attacks and inefficient data transfer:

```
site_config {
  http2_enabled = true
}
```

Leaving HTTP/2 disabled can result in degraded application security and responsiveness, making services more vulnerable to exploitation and less performant for end users.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_function_app" "negative" {
  name                       = "test-azure-functions"
  location                   = azurerm_resource_group.example.location
  resource_group_name        = azurerm_resource_group.example.name
  app_service_plan_id        = azurerm_app_service_plan.example.id
  storage_account_name       = azurerm_storage_account.example.name
  storage_account_access_key = azurerm_storage_account.example.primary_access_key

  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
    min_tls_version = 1.2
    http2_enabled = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_function_app" "positive2" {
  name                       = "test-azure-functions"
  location                   = azurerm_resource_group.example.location
  resource_group_name        = azurerm_resource_group.example.name
  app_service_plan_id        = azurerm_app_service_plan.example.id
  storage_account_name       = azurerm_storage_account.example.name
  storage_account_access_key = azurerm_storage_account.example.primary_access_key

  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
    min_tls_version = 1.2
  }
}
```

```terraform
resource "azurerm_function_app" "positive3" {
  name                       = "test-azure-functions"
  location                   = azurerm_resource_group.example.location
  resource_group_name        = azurerm_resource_group.example.name
  app_service_plan_id        = azurerm_app_service_plan.example.id
  storage_account_name       = azurerm_storage_account.example.name
  storage_account_access_key = azurerm_storage_account.example.primary_access_key

  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
    min_tls_version = 1.2
    http2_enabled = false
  }
}
```

```terraform
resource "azurerm_function_app" "positive1" {
  name                       = "test-azure-functions"
  location                   = azurerm_resource_group.example.location
  resource_group_name        = azurerm_resource_group.example.name
  app_service_plan_id        = azurerm_app_service_plan.example.id
  storage_account_name       = azurerm_storage_account.example.name
  storage_account_access_key = azurerm_storage_account.example.primary_access_key
}
```
