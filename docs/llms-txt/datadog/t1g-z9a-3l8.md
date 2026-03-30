# Source: https://docs.datadoghq.com/security/default_rules/t1g-z9a-3l8.md

---
title: The Private Cluster feature for AKS should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Private Cluster feature for AKS
  should be enabled
---

# The Private Cluster feature for AKS should be enabled

## Description{% #description %}

The Private Cluster feature for Azure Kubernetes Service (AKS) cluster is enabled.

## Rationale{% #rationale %}

The Private Cluster feature ensures that network traffic between your API server and your node pools remains solely on the private network. The API server is not exposed over the internet as it is with the standard AKS deployment. This configuration is a common requirement in many regulatory and industry compliance standards.

## Remediation{% #remediation %}

**Note**: This setting cannot be changed after AKS deployment. Changing the setting requires recreating your cluster.

## Impact{% #impact %}

Creating and managing a Private AKS Cluster requires additional considerations when compared to a standard AKS deployment. It requires understanding how Azure Private Link and Private Endpoints work. It also requires a thorough assessment of your AKS networking architecture and dependencies. If your AKS cluster is on an isolated Azure Virtual Network (VNET), the Private Cluster feature requires additional configurations to allow connectivity between your AKS Cluster and your management VNET. Microsoft's official documentation, which is included in `references`, helps you navigate the deployment of Private AKS Clusters.

## References{% #references %}

1. [https://docs.microsoft.com/en-us/azure/aks/private-clusters](https://docs.microsoft.com/en-us/azure/aks/private-clusters)
1. [https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview)
1. [https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
