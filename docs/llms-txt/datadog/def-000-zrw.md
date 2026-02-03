# Source: https://docs.datadoghq.com/security/default_rules/def-000-zrw.md

---
title: AKS Cluster should have public access limited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AKS Cluster should have public access
  limited
---

# AKS Cluster should have public access limited
 
## Description{% #description %}

When public access is enabled in an AKS cluster, it should be limited to a specific set of CIDRs. For security, public access should be limited to only the bare minimum set of IPs.

## Remediation{% #remediation %}

1. To limit public access, see the Azure AKS documentation on [Modifying cluster endpoint access](https://learn.microsoft.com/en-us/azure/aks/api-server-authorized-ip-ranges).
