# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/azure_instance_using_basic_authentication.md

---
title: Azure instance using basic authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Azure instance using basic authentication
---

# Azure instance using basic authentication

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dafe30ec-325d-4516-85d1-e8e6776f012c`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine#admin_ssh_key)

### Description{% #description %}

Allowing basic password authentication for Azure virtual machines introduces a significant security risk, as passwords can be easily guessed, brute-forced, or leaked. When `disable_password_authentication = false` is set in the `os_profile_linux_config` block, as shown below, the VM permits password-based SSH logins:

```
os_profile_linux_config {
  disable_password_authentication = false
}
```

Instead, SSH key authentication should be required to ensure secure, cryptographically strong access to the instance, as in the following configuration:

```
admin_ssh_key {
  username   = "adminuser"
  public_key = file("~/.ssh/id_rsa.pub")
}
```

Failure to enforce SSH key authentication can lead to unauthorized access, data breaches, or compromise of critical resources.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_virtual_machine" "negative1" {
  name                  = "${var.prefix}-vm"
  location              = azurerm_resource_group.main.location
  resource_group_name   = azurerm_resource_group.main.name
  network_interface_ids = [azurerm_network_interface.main.id]
  vm_size               = "Standard_DS1_v2"

  os_profile_linux_config {
    disable_password_authentication = true
  }

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }
}
```

```terraform
resource "azurerm_linux_virtual_machine" "negative1" {
  name                  = "${var.prefix}-vm"
  location              = azurerm_resource_group.main.location
  resource_group_name   = azurerm_resource_group.main.name
  network_interface_ids = [azurerm_network_interface.main.id]
  vm_size               = "Standard_DS1_v2"

  admin_ssh_key {
    username   = "adminuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_linux_virtual_machine" "positive1" {
  name                  = "${var.prefix}-vm"
  location              = azurerm_resource_group.main.location
  resource_group_name   = azurerm_resource_group.main.name
  network_interface_ids = []
  vm_size               = "Standard_DS1_v2"
  disable_password_authentication = false
}
```

```terraform
resource "azurerm_virtual_machine" "positive1" {
  name                  = "${var.prefix}-vm"
  location              = azurerm_resource_group.main.location
  resource_group_name   = azurerm_resource_group.main.name
  network_interface_ids = []
  vm_size               = "Standard_DS1_v2"

  os_profile_linux_config {
    disable_password_authentication = false
  }
}
```
