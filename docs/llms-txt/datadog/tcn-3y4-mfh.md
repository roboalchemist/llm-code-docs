# Source: https://docs.datadoghq.com/security/default_rules/tcn-3y4-mfh.md

---
title: The kubelet service file should have permissions of 644 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet service file should have
  permissions of 644 or stricter
---

# The kubelet service file should have permissions of 644 or stricter
Classification:complianceFramework:cis-kubernetesControl:4.1.1 
## Description{% #description %}

Ensure that the kubelet service file has permissions of 644 or more restrictive.

## Rationale{% #rationale %}

The kubelet service file controls various parameters that set the behavior of the kubelet service in the worker node. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Audit{% #audit %}

Run the following command (based on the file location on your system) on the each worker node. For example, `stat -c %a /etc/systemd/system/kubelet.service.d/10-kubeadm.conf`. Verify that the permissions are 644 or more restrictive.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the each worker node.

For example, `chmod 644 /etc/systemd/system/kubelet.service.d/10-kubeadm.conf`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the kubelet service file has permissions of 640.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubelet/](https://kubernetes.io/docs/admin/kubelet/)
1. [https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#44-joining-your-nodes](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#44-joining-your-nodes)
1. [https://kubernetes.io/docs/admin/kubeadm/#kubelet-drop-in](https://kubernetes.io/docs/admin/kubeadm/#kubelet-drop-in)

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7.5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
