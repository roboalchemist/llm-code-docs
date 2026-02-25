# Source: https://docs.datadoghq.com/security/default_rules/def-000-tak.md

---
title: An AKS Cluster's Kubelet's read-only port should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An AKS Cluster's Kubelet's read-only
  port should be disabled
---

# An AKS Cluster's Kubelet's read-only port should be disabled

## Description{% #description %}

The read-only port should be disabled to prevent unauthenticated users from potentially retrieving sensitive information about the cluster.

## Remediation{% #remediation %}

Choose one of the following remediation methods. For both methods, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the following JSON to the `/etc/kubernetes/kubelet/kubelet-config.json` file.

```json
"readOnlyPort": 0
```

### Executable arguments{% #executable-arguments %}

1. Edit the Kubelet service file on each worker node and ensure the following parameters are part of the `KUBELET_ARGS` variable string.

```bash
--read-only-port=0
```
