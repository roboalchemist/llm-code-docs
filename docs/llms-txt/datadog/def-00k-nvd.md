# Source: https://docs.datadoghq.com/security/default_rules/def-00k-nvd.md

---
title: The Kubernetes admission controller 'NamespaceLifecycle' should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes admission controller
  'NamespaceLifecycle' should be enabled
---

# The Kubernetes admission controller 'NamespaceLifecycle' should be enabled

## Description{% #description %}

Reject creating objects in a namespace that is undergoing termination. Using the [`NamespaceLifecycle`](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#namespacelifecycle) admission controller plugin ensures that objects cannot be created in non-existent namespaces, and that namespaces undergoing termination are not used for creating the new objects. This is recommended to enforce the integrity of the namespace termination process and also for the availability of the newer objects.

## Remediation{% #remediation %}

1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--disable-admission-plugins` parameter to ensure it does **not** include `NamespaceLifecycle`.
