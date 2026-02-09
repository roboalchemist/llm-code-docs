# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/role_definition_allows_custom_role_creation.md

---
title: Role definition allows custom role creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role definition allows custom role creation
---

# Role definition allows custom role creation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3fa5900f-9aac-4982-96b2-a6143d9c99fb`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_definition#actions)

### Description{% #description %}

Allowing the `Microsoft.Authorization/roleDefinitions/write` action in a custom Azure role definition grants users the ability to create, modify, or delete role definitions within the assigned scope. This level of permission can lead to privilege escalation, where a malicious or compromised user can create overly permissive roles or alter existing ones. To mitigate this risk, custom roles should be limited to `Microsoft.Authorization/roleDefinitions/read`, as shown below:

```
permissions {
  actions = ["Microsoft.Authorization/roleDefinitions/read"]
  not_actions = []
}
```

Restricting write access helps protect against unauthorized changes to role definitions and reduces the attack surface for privilege escalation.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_role_definition" "example3" {
  role_definition_id = "00000000-0000-0000-0000-000000000000"
  name               = "my-custom-role-definition"
  scope              = data.azurerm_subscription.primary.id

  permissions {
    actions     = ["Microsoft.Authorization/roleDefinitions/read"]
    not_actions = []
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_role_definition" "example" {
  name        = "my-custom-role"
  scope       = data.azurerm_subscription.primary.id
  description = "This is a custom role created via Terraform"

  permissions {
    actions     = ["*"]
    not_actions = []
  }
}
```

```terraform
resource "azurerm_role_definition" "example2" {
  role_definition_id = "00000000-0000-0000-0000-000000000000"
  name               = "my-custom-role-definition"
  scope              = data.azurerm_subscription.primary.id

  permissions {
    actions     = ["Microsoft.Authorization/roleDefinitions/write"]
    not_actions = []
  }
}
```
