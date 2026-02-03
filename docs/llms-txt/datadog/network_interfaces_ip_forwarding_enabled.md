# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/network_interfaces_ip_forwarding_enabled.md

---
title: Network interfaces IP forwarding enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Network interfaces IP forwarding enabled
---

# Network interfaces IP forwarding enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4216ebac-d74c-4423-b437-35025cb88af5`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_interface#enable_ip_forwarding)

### Description{% #description %}

Enabling IP forwarding on network interfaces allows packets to be routed between networks, which can make the network interface behave like a router. This may expose your environment to lateral movement and man-in-the-middle attacks if an attacker gains access to the interface. To prevent this risk, set the `enable_ip_forwarding` attribute to `false` in your Terraform configuration, as shown below:

```
resource "azurerm_network_interface" "secure" {
  // ... other configuration ...
  enable_ip_forwarding = false
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_network_interface" "negative2" {
  name                = "example-nic"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.example.id
    private_ip_address_allocation = "Dynamic"
  }
}
```

```terraform
resource "azurerm_network_interface" "negative1" {
  name                = "example-nic"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.example.id
    private_ip_address_allocation = "Dynamic"
  }

  enable_ip_forwarding = false
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_network_interface" "positive" {
  name                = "example-nic"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.example.id
    private_ip_address_allocation = "Dynamic"
  }

  enable_ip_forwarding = true
}
```
