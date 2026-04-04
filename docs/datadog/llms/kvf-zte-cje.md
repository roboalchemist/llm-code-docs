# Source: https://docs.datadoghq.com/security/default_rules/kvf-zte-cje.md

---
title: Kubelet nodes should only read objects associated with them
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet nodes should only read objects
  associated with them
---

# Kubelet nodes should only read objects associated with them
Classification:complianceFramework:cis-kubernetesControl:1.2.8
## Description{% #description %}

Restrict kubelet nodes to reading only objects associated with them.

## Rationale{% #rationale %}

The Node authorization mode only allows kubelets to read Secret, ConfigMap, PersistentVolume, and PersistentVolumeClaim objects associated with their nodes.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--authorization-mode` argument exists and is set to a value to include Node.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--authorization-mode` parameter to a value that includes Node. `--authorization-mode=Node,RBAC`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, Node authorization is not enabled.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://kubernetes.io/docs/admin/authorization/node/](https://kubernetes.io/docs/admin/authorization/node/)
1. [https://github.com/kubernetes/kubernetes/pull/46076](https://github.com/kubernetes/kubernetes/pull/46076)
1. [https://acotten.com/post/kube17-security](https://acotten.com/post/kube17-security)

## CIS controls{% #cis-controls %}

Version 6.9.1 Limit Open Ports, Protocols, and Services - Ensure that only ports, protocols, and services with validated business needs are running on each system.

Version 7.9.2 Ensure Only Approved Ports, Protocols and Services Are Running - Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.
