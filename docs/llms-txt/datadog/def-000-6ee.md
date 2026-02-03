# Source: https://docs.datadoghq.com/security/default_rules/def-000-6ee.md

---
title: Auto-Repair for nodes should be enabled in GKE clusters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Auto-Repair for nodes should be enabled
  in GKE clusters
---

# Auto-Repair for nodes should be enabled in GKE clusters
 
## Description{% #description %}

Auto-repair should be enabled for nodes. Auto-repair fixes nodes in a degraded state. Fixing nodes in a degraded state can help prevent unknown situations that could affect the security of the cluster.

**Note**: Auto-repair is not available on Alpha clusters.

## Remediation{% #remediation %}

Follow the steps in Google Cloud's [Auto-repair nodes guide](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) to enable auto-repair nodes.
