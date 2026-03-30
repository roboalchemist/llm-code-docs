# Source: https://docs.datadoghq.com/security/default_rules/def-00k-3qm.md

---
title: Streaming connections should have timeouts enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Streaming connections should have
  timeouts enabled
---

# Streaming connections should have timeouts enabled

## Description{% #description %}

Timeouts on streaming connections should not be disabled. Setting idle timeouts ensures that you are protected against denial-of-service attacks, inactive connections, and running out of ephemeral ports.

**Note**: By default, `--streaming-connection-idle-timeout` is set to four hours, which might be too high for your environment. Setting this to the appropriate time would ensure that such streaming connections are timed out after serving legitimate use cases.

## Remediation{% #remediation %}

1. If using a Kubelet config file, edit the file to set `streamingConnectionIdleTimeout` to a value other than `0`.
1. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_SYSTEM_PODS_ARGS` variable.

```
--streaming-connection-idle-timeout=5m
```
Restart the kubelet service.