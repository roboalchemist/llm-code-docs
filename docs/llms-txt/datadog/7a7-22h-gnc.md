# Source: https://docs.datadoghq.com/security/default_rules/7a7-22h-gnc.md

---
title: The Controller Manager API service should only bind to localhost
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Controller Manager API service
  should only bind to localhost
---

# The Controller Manager API service should only bind to localhost
Classification:complianceFramework:cis-kubernetesControl:1.3.7 
## Description{% #description %}

Do not bind the Controller Manager service to non-loopback insecure addresses.

## Rationale{% #rationale %}

The Controller Manager API service which runs on port 10252/TCP by default is used for health and metrics information and is available without authentication or encryption. As such it should only be bound to a localhost interface, to minimize the cluster's attack surface

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-controller-manager
```

Verify that the `--bind-address` argument is set to `127.0.0.1`.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and ensure the correct value for the `--bind-address` parameter.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the `--bind-address` parameter is set to `0.0.0.0`.

## References{% #references %}

1. [https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)

*Notes*: Although the current Kubernetes documentation site says that `--address` is deprecated in favour of `--bind-address`. Kubeadm 1.11 still makes use of `--address`.

## CIS controls{% #cis-controls %}

Version 6.9.1 Limit Open Ports, Protocols, and Services - Ensure that only ports, protocols, and services with validated business needs are running on each system.

Version 7.9.2 Ensure Only Approved Ports, Protocols and Services Are Running - Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.
