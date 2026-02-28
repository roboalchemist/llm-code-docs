# Source: https://docs.datadoghq.com/security/default_rules/def-000-3wd.md

---
title: Timeouts for streaming connections in an AKS worker node should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Timeouts for streaming connections in
  an AKS worker node should be enabled
---

# Timeouts for streaming connections in an AKS worker node should be enabled

## Description{% #description %}

Timeouts on streaming connections should be enabled. Setting idle timeouts ensures that the node is protected against Denial-of-Service attacks, inactive connections, and running out of ephemeral ports.

## Remediation{% #remediation %}

Choose one of the following remediation methods. For both methods, a restart of the Kubelet service is required.

### Kubelet config file{% #kubelet-config-file %}

1. Add the following JSON to the `/etc/kubernetes/kubelet/kubelet-config.json` file.

```json
"streamingConnectionIdleTimeout": "4h0m0s"
```

### Executable arguments{% #executable-arguments %}

1. Edit the Kubelet service file on each worker node and ensure the following parameters are part of the `KUBELET_ARGS` variable string.

```bash
--streaming-connection-idle-timeout=4h0m0s
```
