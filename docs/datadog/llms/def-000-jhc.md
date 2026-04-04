# Source: https://docs.datadoghq.com/security/default_rules/def-000-jhc.md

---
title: An EKS Cluster's Kubelet should only allow explicitly authorized requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An EKS Cluster's Kubelet should only
  allow explicitly authorized requests
---

# An EKS Cluster's Kubelet should only allow explicitly authorized requests

## Description{% #description %}

Kubelets can be configured to allow all authenticated requests (even anonymous ones) without needing explicit authorization checks from the apiserver. You should restrict this behavior and only allow explicitly authorized requests.

## Remediation{% #remediation %}

Choose a remediation method from below. For both steps, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the json below to this file: `/etc/kubernetes/kubelet/kubelet-config.json`

```json
"authentication": { "webhook": { "enabled": true } }
"authorization": { "mode": "Webhook" }
```

### Executable arguments{% #executable-arguments %}

1. Edit the kubelet service file on each worker node and ensure the below parameters are part of the `KUBELET_ARGS` variable string.

```bash
--authentication-token-webhook
--authorization-mode=Webhook
```
