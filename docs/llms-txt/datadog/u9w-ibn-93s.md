# Source: https://docs.datadoghq.com/security/default_rules/u9w-ibn-93s.md

---
title: The kubelet.conf file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet.conf file should be owned
  by root
---

# The kubelet.conf file should be owned by root
Classification:complianceFramework:cis-kubernetesControl:4.1.6
## Description{% #description %}

Ensure that the `kubelet.conf` file ownership is set to `root:root`.

## Rationale{% #rationale %}

The `kubelet.conf` file is the kubeconfig file for the node, and controls various parameters that set the behavior and identity of the worker node. You should set its file ownership to maintain the integrity of the file. The file should be owned by root:root.

## Audit{% #audit %}

Run the following command (based on the file location on your system) on the each worker node. For example, `stat -c %U:%G /etc/kubernetes/kubelet.conf`. Verify that the ownership is set to `root:root`.

## Remediation{% #remediation %}

Run this command (based on the file location on your system) on the each worker node. For example, `chown root:root /etc/kubernetes/kubelet.conf`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `kubelet.conf` file ownership is set to `root:root`.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubelet/](https://kubernetes.io/docs/admin/kubelet/)

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7.5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
