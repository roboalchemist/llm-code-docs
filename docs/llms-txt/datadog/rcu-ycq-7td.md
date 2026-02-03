# Source: https://docs.datadoghq.com/security/default_rules/rcu-ycq-7td.md

---
title: The admin.conf file should have permissions of 644 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The admin.conf file should have
  permissions of 644 or more restrictive
---

# The admin.conf file should have permissions of 644 or more restrictive
Classification:complianceFramework:cis-kubernetesControl:1.1.13 
## Description{% #description %}

Ensure that the `admin.conf` file has permissions of 644 or more restrictive.

## Rationale{% #rationale %}

The admin.conf is the administrator kubeconfig file defining various settings for the administration of the cluster. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Audit{% #audit %}

Run the following command (based on the file location on your system) on the master node.

```bash
stat -c %a /etc/kubernetes/admin.conf
```

Verify the permissions are `644` or more restrictive.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chmod 644 /etc/kubernetes/admin.conf`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, admin.conf has permissions of 640.

## References{% #references %}

1. [https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
