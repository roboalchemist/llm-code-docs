# Source: https://docs.datadoghq.com/security/default_rules/def-00k-gqk.md

---
title: RBAC should be enabled for the Kubernetes API server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RBAC should be enabled for the
  Kubernetes API server
---

# RBAC should be enabled for the Kubernetes API server

## Description{% #description %}

Role Based Access Control (RBAC) should be enabled. RBAC allows fine-grained control over the operations that different entities can perform on different objects in the cluster.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node, and set the `--authorization-mode` parameter to a value that includes `RBAC`. For example, `--authorization-mode=Node,RBAC`.
