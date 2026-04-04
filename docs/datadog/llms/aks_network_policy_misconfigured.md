# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/aks_network_policy_misconfigured.md

---
title: AKS network policy misconfigured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > AKS network policy misconfigured
---

# AKS network policy misconfigured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f5342045-b935-402d-adf1-8dbbd09c0eef`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/kubernetes_cluster)

### Description{% #description %}

Azure Kubernetes Service (AKS) clusters should have a proper network policy configured using the `network_profile.network_policy` attribute to enforce the principle of least privilege and restrict unnecessary network traffic between pods. If this attribute is omitted or misconfigured, as shown below, it leaves the cluster vulnerable to unrestricted communication between pods, increasing the risk of lateral movement and exposure if one pod is compromised:

```
network_profile {
  // network_policy not defined
}
```

A secure AKS configuration explicitly sets a network policy. For example:

```
network_profile {
  network_policy = "azure"
}
```

Without strict network policies, attackers could exploit insecure inter-pod communications to access sensitive resources or escalate privileges within the Kubernetes environment.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_kubernetes_cluster" "negative1" {
  name                = "example-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks1"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }

  network_profile {
    network_policy = "azure"
  }
}

resource "azurerm_kubernetes_cluster" "negative2" {
  name                = "example-aks2"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks2"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }

  network_profile {
    network_policy = "calico"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_kubernetes_cluster" "positive1" {
  name                = "example-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks1"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }

  network_profile {
    #...other configurations
  }
}

resource "azurerm_kubernetes_cluster" "positive2" {
  name                = "example-aks2"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks2"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }

}

resource "azurerm_kubernetes_cluster" "positive3" {
  name                = "example-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks1"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }

  network_profile {
    network_policy = "roxanne"
  }
}
```
