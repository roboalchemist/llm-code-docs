# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/role_assignment_not_limit_guest_users_permissions.md

---
title: Role assignment not limit guest user permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Role assignment not limit guest user
  permissions
---

# Role assignment not limit guest user permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8e75e431-449f-49e9-b56a-c8f1378025cf`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_assignment)

### Description{% #description %}

Role assignments in Terraform should strictly limit permissions granted to guest users. If the `actions` attribute in the `azurerm_role_definition` resource is set to `["*"]`, guest users receive unrestricted permissions within the scope, potentially allowing them to perform any action, escalate privileges, or exfiltrate data. It is recommended to set `actions = []` and `not_actions = ["*"]` to ensure that guest users have no actionable privileges, thereby protecting critical resources from unauthorized access.

```
permissions {
  actions     = []
  not_actions = ["*"]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_role_definition" "example2" {
  name        = "my-custom-role"
  scope       = data.azurerm_subscription.primary.id
  description = "This is a custom role created via Terraform"

  permissions {
    actions     = []
    not_actions = ["*"]
  }

  assignable_scopes = [
    data.azurerm_subscription.primary.id,
  ]
}

resource "azurerm_role_assignment" "example2" {
  name               = "00000000-0000-0000-0000-000000000000"
  scope              = data.azurerm_subscription.primary.id
  role_definition_name = "Guest"
  role_definition_id = azurerm_role_definition.example2.role_definition_resource_id
  principal_id       = data.azurerm_client_config.example.object_id
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

  assignable_scopes = [
    data.azurerm_subscription.primary.id,
  ]
}

resource "azurerm_role_assignment" "example" {
  name               = "00000000-0000-0000-0000-000000000000"
  scope              = data.azurerm_subscription.primary.id
  role_definition_name = "Guest"
  role_definition_id = azurerm_role_definition.example.role_definition_resource_id
  principal_id       = data.azurerm_client_config.example.object_id
}
```
