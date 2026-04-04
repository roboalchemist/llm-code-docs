# Source: https://docs.datadoghq.com/security/default_rules/def-000-am9.md

---
title: An EKS Cluster's Kubelet should be allowed to manage iptables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An EKS Cluster's Kubelet should be
  allowed to manage iptables
---

# An EKS Cluster's Kubelet should be allowed to manage iptables

## Description{% #description %}

It is recommended that kubelets be allowed to manage changes to `iptables`. This ensures that the `iptables` configuration remains in sync with your pods networking configuration. Manually configuring `iptables` with dynamic pod network configuration changes might hamper the communication between pods/containers and to the outside world.

## Remediation{% #remediation %}

Choose a remediation method from below. For both steps, a restart of the Kubelet service is required afterwards.

### Kubelet config file{% #kubelet-config-file %}

1. Add the json below to this file: `/etc/kubernetes/kubelet/kubelet-config.json`

```json
"makeIPTablesUtilChains": true
```

### Executable arguments{% #executable-arguments %}

1. Edit the kubelet service file on each worker node and ensure the below parameters are part of the `KUBELET_ARGS` variable string.

```bash
--make-iptables-util-chains:true
```
