# Source: https://docs.datadoghq.com/security/default_rules/def-000-ub6.md

---
title: EKS Cluster should have private endpoint enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EKS Cluster should have private
  endpoint enabled
---

# EKS Cluster should have private endpoint enabled
 
## Description{% #description %}

The EKS cluster should have `Private Endpoint` enabled. This ensures that outside access to the Kubernetes API is disabled if not required.

## Remediation{% #remediation %}

Follow the [Modifying cluster endpoint access](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) documentation to enabled `Private Access`.
