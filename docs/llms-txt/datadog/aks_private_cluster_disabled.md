# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/aks_private_cluster_disabled.md

---
title: AKS private cluster disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > AKS private cluster disabled
---

# AKS private cluster disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `599318f2-6653-4569-9e21-041d06c63a89`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster#private_cluster_enabled)

### Description{% #description %}

The Azure Kubernetes Service (AKS) API server should not be exposed directly to the internet, as this increases the risk of unauthorized access and potential exploitation of the cluster. When the `private_cluster_enabled` attribute is set to `false`, as shown below, the AKS API endpoint is accessible publicly, allowing threat actors to attempt brute force or other attacks:

```
resource "azurerm_kubernetes_cluster" "example" {
  // ...
  private_cluster_enabled = false
}
```

To mitigate this risk, the attribute should be set to `true`, ensuring the API server is only accessible from internal networks and reducing the attack surface:

```
resource "azurerm_kubernetes_cluster" "example" {
  // ...
  private_cluster_enabled = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_kubernetes_cluster" "negative" {
  name                = "example-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks1"

  private_cluster_enabled = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_kubernetes_cluster" "positive2" {
  name                = "example-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks1"

}
```

```terraform
resource "azurerm_kubernetes_cluster" "positive1" {
  name                = "example-aks1"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "exampleaks1"

  private_cluster_enabled = false
}
```
