# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/app_service_not_using_latest_tls_encryption_version.md

---
title: App Service not using latest TLS encryption version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > App Service not using latest TLS encryption
  version
---

# App Service not using latest TLS encryption version

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b7b9d1c7-2d3b-49b4-b867-ebbe68d0b643`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/app_service#min_tls_version)

### Description{% #description %}

App Service instances should be configured to use the latest version of TLS encryption to ensure secure data transmission. Using outdated TLS versions, such as setting `min_tls_version = 1.1`, exposes applications to vulnerabilities and known exploits that exist in deprecated protocols. Setting `min_tls_version = "1.2"` in the `site_config` block helps protect data in transit and reduces the risk of security breaches due to weaker encryption standards.

```
resource "azurerm_app_service" "example" {
  // ...
  site_config {
    min_tls_version = "1.2"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_app_service" "negative3" {
  name                = "example-app-service"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id
}
```

```terraform
resource "azurerm_app_service" "negative1" {
  name                = "example-app-service"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
  }
}
```

```terraform
resource "azurerm_app_service" "negative1" {
  name                = "example-app-service"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
    min_tls_version = 1.2
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_app_service" "positive1" {
  name                = "example-app-service"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  site_config {
    dotnet_framework_version = "v4.0"
    scm_type                 = "LocalGit"
    min_tls_version          = 1.1
  }
}
```
