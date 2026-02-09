# Source: https://docs.datadoghq.com/security/default_rules/def-000-axx.md

---
title: Alpha clusters should not be used for production workloads
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Alpha clusters should not be used for
  production workloads
---

# Alpha clusters should not be used for production workloads
 
## Description{% #description %}

Alpha clusters are not suitable for production workloads. They are intended for early adopters to test new features before they become production-ready. Although they enable all Kubernetes API features, alpha clusters are not covered by the GKE SLA, do not receive security updates, have node auto-upgrade and node auto-repair disabled, cannot be upgraded, and are automatically deleted after 30 days.

**Note:** Alpha features cannot be disabled. To remediate, a new cluster must be created.

## Remediation{% #remediation %}

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list).
1. Click `CREATE CLUSTER`.
1. Configure the cluster as required.
1. Confirm that the `Enable Kubernetes alpha features in this cluster` checkbox is not selected.
1. Click `CREATE`.

## References{% #references %}
