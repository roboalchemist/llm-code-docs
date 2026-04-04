# Source: https://docs.datadoghq.com/security/default_rules/wgm-8ss-pvn.md

---
title: >-
  Scheduler.conf file should only be alterable by owners with permissions of 644
  or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Scheduler.conf file should only be
  alterable by owners with permissions of 644 or more restrictive
---

# Scheduler.conf file should only be alterable by owners with permissions of 644 or more restrictive
Classification:complianceFramework:cis-kubernetesControl:1.1.15
## Description{% #description %}

Ensure that the `scheduler.conf` file has permissions of 644 or more restrictive.

## Rationale{% #rationale %}

The `scheduler.conf` file is the kubeconfig file for the Scheduler. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Audit{% #audit %}

Run the following command (based on the file location on your system) on the master node.

```bash
stat -c %a /etc/kubernetes/scheduler.conf
```

Verify the permissions are `644` or more restrictive.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chmod 644 /etc/kubernetes/scheduler.conf`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `scheduler.conf` has permissions of 640.

## References{% #references %}

1. [https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
