# Source: https://docs.datadoghq.com/security/default_rules/def-000-z1p.md

---
title: Container-Optimized OS (cos_containerd) should be used for GKE node images
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Container-Optimized OS (cos_containerd)
  should be used for GKE node images
---

# Container-Optimized OS (cos_containerd) should be used for GKE node images
 
## Description{% #description %}

Container-Optimized OS images should be used in your cluster. These image types are hardened and increase the security of the GKE cluster(s) in your environment.

## Remediation{% #remediation %}

Follow the steps from Google Cloud's [Specify a node image](https://cloud.google.com/kubernetes-engine/docs/how-to/node-images) documentation to configure your cluster's workloads and use Container-Optimized OS with containerd (`cos_containerd`) node image.
