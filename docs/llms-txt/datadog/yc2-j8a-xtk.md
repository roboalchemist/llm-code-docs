# Source: https://docs.datadoghq.com/security/default_rules/yc2-j8a-xtk.md

---
title: The default service account should not be used
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The default service account should not
  be used
---

# The default service account should not be used
Classification:complianceFramework:cis-kubernetesControl:5.1.5 
## Description{% #description %}

The default service account should not be used to ensure that rights granted to applications can be more easily audited and reviewed.

## Rationale{% #rationale %}

Kubernetes provides a default service account which is used by cluster workloads where no specific service account is assigned to the pod. Where access to the Kubernetes API from a pod is required, a specific service account should be created for that pod, and rights granted to that service account. The default service account should be configured such that it does not provide a service account token and does not have any explicit rights assignments.

## Audit{% #audit %}

For each namespace in the cluster, review the rights assigned to the default service account and ensure that it has no roles or cluster roles bound to it apart from the defaults. Additionally ensure that the `automountServiceAccountToken: false` setting is in place for each default service account.

## Remediation{% #remediation %}

Create explicit service accounts wherever a Kubernetes workload requires specific access to the Kubernetes API server. Modify the configuration of each default service account to include this value `automountServiceAccountToken: false`.

## Impact{% #impact %}

All workloads which require access to the Kubernetes API will require an explicit service account to be created.

## Default value{% #default-value %}

By default the default service account allows for its service account token to be mounted in pods in its namespace.

## References{% #references %}

1. [https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

## CIS controls{% #cis-controls %}

None
