# Source: https://docs.datadoghq.com/security/default_rules/def-000-jt8.md

---
title: EKS cluster should use a network policy between nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EKS cluster should use a network policy
  between nodes
---

# EKS cluster should use a network policy between nodes
 
## Description{% #description %}

Network policies restrict pod-to-pod traffic and should be implemented in EKS clusters.

## Remediation{% #remediation %}

1. Use the [Kubernetes network policies](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html) documentation from AWS for configuring network policies.
