# Source: https://docs.datadoghq.com/security/default_rules/def-000-axz.md

---
title: GKE nodes should use the metadata server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GKE nodes should use the metadata
  server
---

# GKE nodes should use the metadata server

## Description{% #description %}

Pods should not have full access to a node's metadata. Using the GKE metadata server keeps sensitive metadata on a separate server for workloads instead of locally on a node. This prevents additional impact to your organization if the workload becomes compromised.

## Remediation{% #remediation %}

Follow the steps in Google Cloud's [Enable Workload Identity Federation for GKE on clusters and node pools](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools) documentation to enable the GKE metadata server.
