# Source: https://docs.datadoghq.com/security/default_rules/def-000-cev.md

---
title: GKE clusters should have monitoring and logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GKE clusters should have monitoring and
  logging enabled
---

# GKE clusters should have monitoring and logging enabled

## Description{% #description %}

This control validates the configuration of logging and monitoring on GKE Clusters. Exporting logs and metrics to a dedicated, persistent datastore such as Cloud Operations for GKE ensures availability of audit data following a cluster security event, and provides a central location for analysis of log and metric data collected from multiple sources.

## Remediation{% #remediation %}

To enable audit logs for your GKE cluster, see [Observability for GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/observability).
