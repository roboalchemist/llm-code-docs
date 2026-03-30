# Source: https://docs.datadoghq.com/security/default_rules/def-000-scc.md

---
title: An AKS Cluster's Kubelet should rotate server certificates automatically
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An AKS Cluster's Kubelet should rotate
  server certificates automatically
---

# An AKS Cluster's Kubelet should rotate server certificates automatically

## Description{% #description %}

Server certificates should be rotated. This ensures there is no downtime due to expired certificates.

## Remediation{% #remediation %}

Follow the [documentation from Azure](https://learn.microsoft.com/en-us/azure/aks/certificate-rotation#certificate-auto-rotation) on how to manage server certificate rotation.
