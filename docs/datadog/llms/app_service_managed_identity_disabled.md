# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/app_service_managed_identity_disabled.md

---
title: App Service managed identity disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > App Service managed identity disabled
---

# App Service managed identity disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b61cce4b-0cc4-472b-8096-15617a6d769b`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Resource Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/app_service#identity)

### Description{% #description %}

Azure App Services should have managed identities enabled to provide secure, automated identity management for accessing Azure resources. Without specifying the `identity { type = "SystemAssigned" }` block in the Terraform configuration, the service may rely on insecure credential storage or hardcoded secrets, increasing the risk of credential exposure. Enabling managed identity ensures the App Service can securely authenticate to Azure resources without the need to manage credentials manually, reducing the attack surface and enhancing overall security.

```
resource "azurerm_app_service" "example" {
  // ...other configuration...

  identity {
    type = "SystemAssigned"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

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

  app_settings = {
    "SOME_KEY" = "some-value"
  }

  connection_string {
    name  = "Database"
    type  = "SQLServer"
    value = "Server=some-server.mydomain.com;Integrated Security=SSPI"
  }

  identity {
    type = "SystemAssigned"
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
  }

  app_settings = {
    "SOME_KEY" = "some-value"
  }

  connection_string {
    name  = "Database"
    type  = "SQLServer"
    value = "Server=some-server.mydomain.com;Integrated Security=SSPI"
  }
}
```
