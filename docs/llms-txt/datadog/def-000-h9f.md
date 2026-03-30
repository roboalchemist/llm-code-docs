# Source: https://docs.datadoghq.com/security/default_rules/def-000-h9f.md

---
title: An AKS Cluster's Kubelet configuration file should disable anonymous requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An AKS Cluster's Kubelet configuration
  file should disable anonymous requests
---

# An AKS Cluster's Kubelet configuration file should disable anonymous requests

## Description{% #description %}

Disable anonymous requests to the Kubelet server. You should rely on authentication to authorize access and disallow anonymous requests to prevent unwanted actions in your cluster.

## Remediation{% #remediation %}

Choose one of the following remediation methods. For both methods, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the following JSON to the `/etc/kubernetes/kubelet/kubelet-config.json` file.

```json
"authentication": { "anonymous": { "enabled": false } }
```

### Executable arguments{% #executable-arguments %}

1. Edit the kubelet service file on each worker node and ensure the following parameters are part of the `KUBELET_ARGS` variable string.

```bash
--anonymous-auth=false
```
