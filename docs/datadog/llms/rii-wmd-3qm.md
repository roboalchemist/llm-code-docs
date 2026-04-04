# Source: https://docs.datadoghq.com/security/default_rules/rii-wmd-3qm.md

---
title: Streaming connections should have timeouts enabled and not be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Streaming connections should have
  timeouts enabled and not be disabled
---

# Streaming connections should have timeouts enabled and not be disabled
Classification:complianceFramework:cis-kubernetesControl:4.2.5
## Description{% #description %}

Do not disable timeouts on streaming connections.

## Rationale{% #rationale %}

Setting idle timeouts ensures that you are protected against denial-of-service attacks, inactive connections, and running out of ephemeral ports.

*Note*: By default, `--streaming-connection-idle-timeout` is set to four hours, which might be too high for your environment. Setting this as appropriate would additionally ensure that such streaming connections are timed out after serving legitimate use cases.

## Audit{% #audit %}

Run the following command on each node: `ps -ef | grep kubelet`. Verify that the `--streaming-connection-idle-timeout` argument is not set to 0. If the argument is not present, and there is a Kubelet config file specified by `--config`, check that it does not set `streamingConnectionIdleTimeout` to 0.

## Remediation{% #remediation %}

If using a Kubelet config file, edit the file to set `streamingConnectionIdleTimeout` to a value other than 0. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_SYSTEM_PODS_ARGS` variable.

`--streaming-connection-idle-timeout=5m`

Based on your system, restart the kubelet service. For example: `systemctl daemon-reload systemctl restart kubelet.service`

## Impact{% #impact %}

Long-lived connections could be interrupted.

## Default value{% #default-value %}

By default, `--streaming-connection-idle-timeout` is set to four hours.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubelet/](https://kubernetes.io/docs/admin/kubelet/)
1. [https://github.com/kubernetes/kubernetes/pull/18552](https://github.com/kubernetes/kubernetes/pull/18552)

## CIS controls{% #cis-controls %}

Version 6.9 Limitation and Control of Network Ports, Protocols, and Services
