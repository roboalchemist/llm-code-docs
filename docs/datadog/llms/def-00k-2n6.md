# Source: https://docs.datadoghq.com/security/default_rules/def-00k-2n6.md

---
title: The Kubernetes API server should only allow explicitly authorized requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server should only
  allow explicitly authorized requests
---

# The Kubernetes API server should only allow explicitly authorized requests

## Description{% #description %}

The API server should not be configured to allow all requests. This mode should not be used on any production cluster.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node, and set the `--authorization-mode` parameter to values other than `AlwaysAllow`. For example, `--authorization-mode=RBAC,Node`.
