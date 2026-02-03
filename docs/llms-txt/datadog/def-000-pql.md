# Source: https://docs.datadoghq.com/security/default_rules/def-000-pql.md

---
title: A GKE's Cluster's Kubelet should use TLS authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A GKE's Cluster's Kubelet should use
  TLS authentication
---

# A GKE's Cluster's Kubelet should use TLS authentication
 
## Description{% #description %}

Disable anonymous requests to the Kubelet server. You should rely on authentication to authorize access and disallow anonymous requests to prevent unwanted actions in your cluster.

## Remediation{% #remediation %}

Choose a remediation method from below. For both steps, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the json below to this file: `/etc/kubernetes/kubelet/kubelet-config.json`

```json
"authentication": { "x509": {"clientCAFile": "<path/to/client-ca-file>" }}"
```

### Executable arguments{% #executable-arguments %}

1. Edit the kubelet service file on each worker node and ensure the below parameters are part of the `KUBELET_ARGS` variable string.

```bash
--client-ca-file=<path/to/client-ca-file>
```
