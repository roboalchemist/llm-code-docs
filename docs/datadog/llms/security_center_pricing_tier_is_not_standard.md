# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/security_center_pricing_tier_is_not_standard.md

---
title: Security center pricing tier is not standard
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security center pricing tier is not standard
---

# Security center pricing tier is not standard

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `819d50fd-1cdf-45c3-9936-be408aaad93e`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/security_center_subscription_pricing)

### Description{% #description %}

Selecting the appropriate pricing tier for Azure Security Center is crucial for ensuring comprehensive security monitoring and protection. If the `tier` attribute in the `azurerm_security_center_subscription_pricing` resource is set to `"Free"`, as in the following configuration, only limited security features and monitoring capabilities are enabled, leaving the environment more vulnerable to threats:

```
resource "azurerm_security_center_subscription_pricing" "example" {
   tier = "Free"
}
```

To enhance security coverage, upgrade to the `"Standard"` tier, as shown below. This enables advanced features such as threat detection and automated response, significantly reducing the risk of undetected attacks and data breaches:

```
resource "azurerm_security_center_subscription_pricing" "example" {
   tier = "Standard"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_security_center_subscription_pricing" "negative1" {
   tier = "Standard"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_security_center_subscription_pricing" "positive1" {
   tier = "Free"
}
```
