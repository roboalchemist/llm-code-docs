# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/waf_is_disabled_for_azure_application_gateway.md

---
title: WAF is disabled for Azure application gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > WAF is disabled for Azure application gateway
---

# WAF is disabled for Azure application gateway

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2e48d91c-50e4-45c8-9312-27b625868a72`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/application_gateway)

### Description{% #description %}

This check ensures that the Azure Application Gateway has its Web Application Firewall (WAF) correctly configured and enabled, as indicated by the `waf_configuration { enabled = true }` attribute in Terraform. If WAF is not enabled or omitted from the configuration, the application gateway is left unprotected against common web attacks, such as SQL injection and cross-site scripting, increasing the risk of a successful attack. To mitigate this vulnerability, always configure WAF with `enabled = true`, as shown below:

```
resource "azurerm_application_gateway" "example" {
  // ... other settings ...
  waf_configuration {
    enabled = true
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_application_gateway" "negative1" {
  name                = "example-appgateway"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location

  waf_configuration {
    enabled = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_application_gateway" "positive1" {
  name                = "example-appgateway"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location

  waf_configuration {
    enabled = false
  }
}

resource "azurerm_application_gateway" "positive2" {
  name                = "example-appgateway"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
}
```
