# Source: https://docs.datadoghq.com/security/default_rules/def-00k-4nb.md

---
title: The Kubernetes admission controller 'NodeRestriction' should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes admission controller
  'NodeRestriction' should be enabled
---

# The Kubernetes admission controller 'NodeRestriction' should be enabled

## Description{% #description %}

The Node and Pod objects that a kubelet could modify should be limited. Using the [`NodeRestriction`](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction) admission controller plugin limits the Node and Pod objects that a kubelet can modify. When limited by this admission controller, kubelets are only allowed to modify their own Node API object, and only modify Pod API objects that are bound to their node.

## Remediation{% #remediation %}

### Kubelet{% #kubelet %}

1. On every node, set the authorization mode to `webhook` with parameters:
   ```
   --authorization-mode=webhook
   ```
1. Use the [Kubernetes Webhook Mode documentation](https://kubernetes.io/docs/reference/access-authn-authz/webhook/) to configure `Webhook` mode.

### API Server{% #api-server %}

1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--enable-admission-plugins=NodeRestriction,...` parameter.
