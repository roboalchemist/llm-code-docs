# Source: https://docs.datadoghq.com/security/default_rules/def-00k-b9s.md

---
title: The kubelet read-only port should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet read-only port should be
  disabled
---

# The kubelet read-only port should be disabled
 
## Description{% #description %}

The read-only port should be disabled. The Kubelet process provides a read-only API in addition to the main Kubelet API. Unauthenticated access is provided to this read-only API which could possibly retrieve potentially sensitive information about the cluster.

## Remediation{% #remediation %}

1. If using a Kubelet config file, edit the file to set `readOnlyPort` to 0.
1. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_SYSTEM_PODS_ARGS` variable.

```
--read-only-port=0
```
Restart the kubelet service.