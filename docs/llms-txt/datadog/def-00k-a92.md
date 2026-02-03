# Source: https://docs.datadoghq.com/security/default_rules/def-00k-a92.md

---
title: API server should have the anonymous-auth argument set to false
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API server should have the
  anonymous-auth argument set to false
---

# API server should have the anonymous-auth argument set to false
 
## Description{% #description %}

Anonymous requests to the kubelet server should be disabled. When enabled, requests that are not rejected by other configured authentication methods are treated as anonymous requests. These requests are then served by the kubelet server.

## Remediation{% #remediation %}

1. If using a kubelet config file, edit the file to set `authentication: anonymous:enabled` to `authentication: anonymous:false`.

1. If using executable arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in the `KUBELET_SYSTEM_PODS_ARGS` variable:

```
--anonymous-auth=false
```
Restart the kubelet service.