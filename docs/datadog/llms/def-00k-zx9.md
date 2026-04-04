# Source: https://docs.datadoghq.com/security/default_rules/def-00k-zx9.md

---
title: Service accounts management should be automated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Service accounts management should be
  automated
---

# Service accounts management should be automated

## Description{% #description %}

When you create a pod, if you do not specify a service account, it is automatically assigned the default service account in the same namespace. You should create your own service account and let the API server manage its security tokens.

## Remediation{% #remediation %}

1. Follow the [Kubernetes Service Account documentation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) to create ServiceAccount objects for your environment.
1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and ensure that the `--disable-admission-plugins` parameter is set to a value that does not include `ServiceAccount`.
