# Source: https://docs.datadoghq.com/security/default_rules/q7w-nkp-qda.md

---
title: The scheduler.conf file should be owned by root:root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The scheduler.conf file should be owned
  by root:root
---

# The scheduler.conf file should be owned by root:root
Classification:complianceFramework:cis-kubernetesControl:1.1.16 
## Description{% #description %}

Ensure that the `scheduler.conf` file ownership is set to `root:root`.

## Rationale{% #rationale %}

The `scheduler.conf` file is the kubeconfig file for the Scheduler. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Audit{% #audit %}

Run the below command (based on the file location on your system) on the master node.

```bash
stat -c %U:%G /etc/kubernetes/scheduler.conf
```

Verify the ownership is set to `root:root`.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chown root:root /etc/kubernetes/scheduler.conf`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `scheduler.conf` file ownership is set to root:root.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubeadm/](https://kubernetes.io/docs/admin/kubeadm/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7

5.2 Maintain Secure Images Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
