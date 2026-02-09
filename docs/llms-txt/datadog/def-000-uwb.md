# Source: https://docs.datadoghq.com/security/default_rules/def-000-uwb.md

---
title: An EKS Cluster's Kubelet should rotate server certificates automatically
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An EKS Cluster's Kubelet should rotate
  server certificates automatically
---

# An EKS Cluster's Kubelet should rotate server certificates automatically
 
## Description{% #description %}

Server certificates should be rotated. This ensures there is no downtime due to expired certificates.

## Remediation{% #remediation %}

Choose a remediation method from below. For both steps, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the json below to the feature gates section of this file: `/etc/kubernetes/kubelet/kubelet-config.json`

```json
"RotateKubeletServerCertificate": true
```

### Executable arguments{% #executable-arguments %}

```bash
--rotate-kubelet-server-certificate=true
```
