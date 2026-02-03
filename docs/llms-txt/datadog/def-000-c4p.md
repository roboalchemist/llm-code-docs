# Source: https://docs.datadoghq.com/security/default_rules/def-000-c4p.md

---
title: An EKS Cluster's Kubelet's read-only port should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An EKS Cluster's Kubelet's read-only
  port should be disabled
---

# An EKS Cluster's Kubelet's read-only port should be disabled
 
## Description{% #description %}

The read-only port should be disabled so unauthenticated users cannot retrieve potentially sensitive information about the cluster.

## Remediation{% #remediation %}

Choose a remediation method from below. For both steps, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the json below to this file: `/etc/kubernetes/kubelet/kubelet-config.json`

```json
"readOnlyPort": 0
```

### Executable arguments{% #executable-arguments %}

1. Edit the Kubelet service file on each worker node and ensure the below parameters are part of the `KUBELET_ARGS` variable string.

```bash
--read-only-port=0
```
