# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/security_contact_email.md

---
title: Security contact email
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security contact email
---

# Security contact email

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `34664094-59e0-4524-b69f-deaa1a68cce3`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/security_center_contact#email)

### Description{% #description %}

Defining a security contact email in the `azurerm_security_center_contact` resource is essential for ensuring that security alerts and notifications from Azure are sent to the correct personnel. If the `email` attribute is omitted, as shown below, important security incidents may go unnoticed, increasing the risk of delayed responses to threats:

```
resource "azurerm_security_center_contact" "insecure" {
  phone = "+1-555-555-5555"
  alert_notifications = true
  alerts_to_admins    = true
}
```

To address this, always specify the `email` attribute to ensure security alerts reach a monitored mailbox:

```
resource "azurerm_security_center_contact" "secure" {
  email = "contact@example.com"
  phone = "+1-555-555-5555"
  alert_notifications = true
  alerts_to_admins    = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_security_center_contact" "negative" {
  email = "contact@example.com"
  phone = "+1-555-555-5555"

  alert_notifications = true
  alerts_to_admins    = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_security_center_contact" "positive" {
  phone = "+1-555-555-5555"

  alert_notifications = true
  alerts_to_admins    = true
}
```
