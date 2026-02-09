# Source: https://docs.datadoghq.com/security/default_rules/g4y-d5m-gaj.md

---
title: Kubelet default kernel parameter values should be protected from overriding.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet default kernel parameter values
  should be protected from overriding.
---

# Kubelet default kernel parameter values should be protected from overriding.
Classification:complianceFramework:cis-kubernetesControl:4.2.6 
## Description{% #description %}

Protect tuned kernel parameters from overriding kubelet default kernel parameter values.

## Rationale{% #rationale %}

Kernel parameters are usually tuned and hardened by the system administrators before putting the systems into production. These parameters protect the kernel and the system. Your kubelet kernel defaults that rely on such parameters should be appropriately set to match the desired secured system state. Ignoring this could potentially lead to running pods with undesired kernel behavior.

## Audit{% #audit %}

Run the following command on each node: `ps -ef | grep kubelet`. Verify that the `--protect-kernel-defaults` argument is set to true. If the `--protect-kernel-defaults` argument is not present, check that there is a Kubelet config file specified by `--config`, and that the file sets `protectKernelDefaults` to `true`.

## Remediation{% #remediation %}

If using a Kubelet config file, edit the file to set `protectKernelDefaults: true`. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_SYSTEM_PODS_ARGS` variable.

`--protect-kernel-defaults=true`

Based on your system, restart the kubelet service. For example: `systemctl daemon-reload systemctl restart kubelet.service`

## Impact{% #impact %}

You would have to re-tune kernel parameters to match kubelet parameters.

## Default value{% #default-value %}

By default, `--protect-kernel-defaults` is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubelet/](https://kubernetes.io/docs/admin/kubelet/)

## CIS controls{% #cis-controls %}

Version 6.3 Secure Configurations for Hardware and Software on Mobile Devices, Laptops, Workstations, and Servers
