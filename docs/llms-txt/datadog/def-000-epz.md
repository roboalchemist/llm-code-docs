# Source: https://docs.datadoghq.com/security/default_rules/def-000-epz.md

---
title: EKS Cluster should have public access limited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EKS Cluster should have public access
  limited
---

# EKS Cluster should have public access limited

## Description{% #description %}

When public access is enabled in an EKS cluster, it should be limited to a specific set of CIDRs. For security, public access should be limited to only the bare minimum set of IPs.

## Remediation{% #remediation %}

1. Use step 6 from the [Modifying cluster endpoint access](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) documentation to limit public access.
