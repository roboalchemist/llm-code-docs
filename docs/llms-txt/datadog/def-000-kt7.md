# Source: https://docs.datadoghq.com/security/default_rules/def-000-kt7.md

---
title: Timeouts for streaming connections in an EKS worker node should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Timeouts for streaming connections in
  an EKS worker node should be enabled
---

# Timeouts for streaming connections in an EKS worker node should be enabled
 
## Description{% #description %}

Timeouts on streaming connections should be enabled. Setting idle timeouts ensures that the node is protected against Denial-of-Service attacks, inactive connections, and running out of ephemeral ports.

## Remediation{% #remediation %}

Choose a remediation method from below. For both steps, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the json below to this file: `/etc/kubernetes/kubelet/kubelet-config.json`

```json
"streamingConnectionIdleTimeout": "4h0m0s"
```

### Executable arguments{% #executable-arguments %}

1. Edit the Kubelet service file on each worker node and ensure the below parameters are part of the `KUBELET_ARGS` variable string.

```bash
--streaming-connection-idle-timeout=4h0m0s
```
