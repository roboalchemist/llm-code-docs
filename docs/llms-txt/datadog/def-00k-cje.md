# Source: https://docs.datadoghq.com/security/default_rules/def-00k-cje.md

---
title: >-
  Kubelet nodes should only be authorized to read objects they are associated
  with
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet nodes should only be authorized
  to read objects they are associated with
---

# Kubelet nodes should only be authorized to read objects they are associated with

## Description{% #description %}

Kubelet nodes should only read objects associated to them. The Node authorization mode only allows kubelets to read `Secret`, `ConfigMap`, `PersistentVolume`, and `PersistentVolumeClaim` objects associated with their nodes.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node, and set the `--authorization-mode` parameter to a value that includes `Node`. For example, `--authorization-mode=Node,RBAC`.
