# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/email_alerts_disabled.md

---
title: Email alerts disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Email alerts disabled
---

# Email alerts disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9db38e87-f6aa-4b5e-a1ec-7266df259409`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/security_center_contact)

### Description{% #description %}

Azure Security Center contact alert notifications should be enabled to ensure that designated security contacts receive email alerts about security issues or threats in your Azure environment. If the `alert_notifications` attribute is set to `false`, such as shown below, critical security incidents could go unnoticed, increasing the risk of delayed response to threats.

```
resource "azurerm_security_center_contact" "example" {
    email = "contact@example.com"
    phone = "+1-555-555-5555"
    alert_notifications = false
}
```

Setting `alert_notifications = true` ensures timely awareness and response to potential security incidents.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_security_center_contact" "negative1" {
    email = "contact@example.com"
    phone = "+1-555-555-5555"
    alert_notifications = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_security_center_contact" "positive1" {
    email = "contact@example.com"
    phone = "+1-555-555-5555"
   alert_notifications = false
}
```
