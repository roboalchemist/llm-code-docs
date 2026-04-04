# Source: https://docs.datadoghq.com/security/default_rules/def-00k-fa2.md

---
title: Kubelets should be allowed to manage changes to the iptables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelets should be allowed to manage
  changes to the iptables
---

# Kubelets should be allowed to manage changes to the iptables

## Description{% #description %}

Kubelet should be allowed to manage iptables. Kubelets can automatically manage the required changes to iptables based on how you choose your networking options for the pods. This ensures that the iptables configuration remains in sync with pods networking configuration. Manually configuring iptables with dynamic pod network configuration changes might block the communication between pods and containers to the outside world.

## Remediation{% #remediation %}

1. If using a kubelet config file, edit the file to set `makeIPTablesUtilChains: true`.

1. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and remove the argument below from the `KUBELET_SYSTEM_PODS_ARGS` variable:

```
--make-iptables-util-chains
```
Restart the kubelet service.