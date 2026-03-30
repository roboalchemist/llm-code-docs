# Source: https://docs.datadoghq.com/security/default_rules/ryt-btw-5yf.md

---
title: >-
  The /etc/kubernetes/manifests/etcd.yaml file should have permissions of 644 or
  stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The /etc/kubernetes/manifests/etcd.yaml
  file should have permissions of 644 or stricter
---

# The /etc/kubernetes/manifests/etcd.yaml file should have permissions of 644 or stricter
Classification:complianceFramework:cis-kubernetesControl:1.1.7
## Description{% #description %}

Ensure that the `/etc/kubernetes/manifests/etcd.yaml` file has permissions of 644 or more restrictive.

## Rationale{% #rationale %}

The etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` controls various parameters that set the behavior of the etcd service in the master node. etcd is a highly-available key-value store which Kubernetes uses for persistent storage of all of its REST API object. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Audit{% #audit %}

Run the below command (based on the file location on your system) on the master node.

```bash
stat -c %a /etc/kubernetes/manifests/etcd.yaml
```

Verify the permissions are 644 or more restrictive.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chmod 644 /etc/kubernetes/manifests/etcd.yaml`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `/etc/kubernetes/manifests/etcd.yaml` file has permissions of 640.

## References{% #references %}

1. [https://coreos.com/etcd](https://coreos.com/etcd)
1. [https://kubernetes.io/docs/admin/etcd/](https://kubernetes.io/docs/admin/etcd/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
