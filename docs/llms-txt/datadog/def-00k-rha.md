# Source: https://docs.datadoghq.com/security/default_rules/def-00k-rha.md

---
title: Kubelet should only allow explicitly authorized requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet should only allow explicitly
  authorized requests
---

# Kubelet should only allow explicitly authorized requests
 
## Description{% #description %}

Explicit authorization should be enabled. Kubelets, by default, allow all authenticated requests (even anonymous ones) without needing explicit authorization checks from the API server.

## Remediation{% #remediation %}

1. If using a Kubelet config file, edit the file to set `authorization: Webhook`.
1. If using executable arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in the `KUBELET_AUTHZ_ARGS` variable.

```
--authorization-mode=Webhook
```
Restart the kubelet service.