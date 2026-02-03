# Source: https://docs.datadoghq.com/security/default_rules/ipi-wby-anc.md

---
title: The scheduler pod specification file ownership should be set to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The scheduler pod specification file
  ownership should be set to root
---

# The scheduler pod specification file ownership should be set to root
Classification:complianceFramework:cis-kubernetesControl:1.1.6 
## Description{% #description %}

Ensure that the scheduler pod specification file ownership is set to root:root.

## Rationale{% #rationale %}

The scheduler pod specification file controls various parameters that set the behavior of the kube-scheduler service in the master node. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Audit{% #audit %}

Run the below command (based on the file location on your system) on the master node.

```bash
stat -c %U:%G /etc/kubernetes/manifests/kube-scheduler.yaml
```

Verify the ownership is set to `root:root`.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chown root:root /etc/kubernetes/manifests/kube-scheduler.yaml`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `kube-scheduler.yaml` file ownership is set to root:root.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-scheduler/](https://kubernetes.io/docs/admin/kube-scheduler/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
