# Source: https://docs.datadoghq.com/security/default_rules/jeq-xry-fa2.md

---
title: Kubelet should be able to manage changes to iptables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet should be able to manage
  changes to iptables
---

# Kubelet should be able to manage changes to iptables
Classification:complianceFramework:cis-kubernetesControl:4.2.7
## Description{% #description %}

Allow Kubelet to manage `iptables`.

## Rationale{% #rationale %}

Kubelets can automatically manage the required changes to `iptables` based on how you choose your networking options for the pods. It is recommended to let kubelets manage the changes to `iptables`. This ensures that the `iptables` configuration remains in sync with pods networking configuration. Manually configuring `iptables` with dynamic pod network configuration changes might hamper the communication between pods/containers and to the outside world. You might have `iptables` rules too restrictive or too open.

## Audit{% #audit %}

Run the following command on each node: `ps -ef | grep kubelet`. Verify that if the `--make-iptables-util-chains` argument exists then it is set to true. If the `--make-iptables-util-chains` argument does not exist, and there is a Kubelet config file specified by `--config`, verify that the file does not set `makeIPTablesUtilChains` to `false`.

## Remediation{% #remediation %}

If using a kubelet config file, edit the file to set `makeIPTablesUtilChains: true`. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and remove the `--make-iptables-util-chains` argument from the `KUBELET_SYSTEM_PODS_ARGS` variable. Based on your system, restart the kubelet service. For example: `systemctl daemon-reload systemctl restart kubelet.service`

## Impact{% #impact %}

Kubelet would manage the `iptables` on the system and keep it in sync. If you are using any other `iptables` management solution, then there might be some conflicts.

## Default value{% #default-value %}

By default, `--make-iptables-util-chains argument` is set to true.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubelet/](https://kubernetes.io/docs/admin/kubelet/)

## CIS controls{% #cis-controls %}

Version 6.9 Limitation and Control of Network Ports, Protocols, and Services
