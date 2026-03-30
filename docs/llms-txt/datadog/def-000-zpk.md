# Source: https://docs.datadoghq.com/security/default_rules/def-000-zpk.md

---
title: AKS cluster should use a network policy between nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AKS cluster should use a network policy
  between nodes
---

# AKS cluster should use a network policy between nodes

## Description{% #description %}

Network policies restrict pod-to-pod traffic and should be implemented in AKS clusters.

## Remediation{% #remediation %}

1. To configure network policies, see the Azure documentation on [Kubernetes network policies](https://learn.microsoft.com/en-us/azure/aks/use-network-policies).
