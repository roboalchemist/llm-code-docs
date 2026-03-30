# Source: https://docs.datadoghq.com/security/default_rules/pra-z9v-3ig.md

---
title: >-
  [Deprecated The /etc/kubernetes/manifests/etcd.yaml file ownership should be
  root:root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > [Deprecated The
  /etc/kubernetes/manifests/etcd.yaml file ownership should be root:root
---

# [Deprecated The /etc/kubernetes/manifests/etcd.yaml file ownership should be root:root
Classification:complianceFramework:cis-kubernetesControl:1.1.8
## Description{% #description %}

Ensure that the `/etc/kubernetes/manifests/etcd.yaml` file ownership is set to `root:root`.

## Rationale{% #rationale %}

The etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` controls various parameters that set the behavior of the etcd service in the master node. etcd is a highly-available key-value store which Kubernetes uses for persistent storage of all of its REST API object. You should set its file ownership to maintain the integrity of the file. The file should be owned by `root:root`.

## Audit{% #audit %}

Run the below command (based on the file location on your system) on the master node.

```bash
stat -c %U:%G /etc/kubernetes/manifests/etcd.yaml
```

Verify the ownership is set to `root:root`.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chown root:root /etc/kubernetes/manifests/etcd.yaml`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `/etc/kubernetes/manifests/etcd.yaml` file ownership is set to root:root.

## References{% #references %}

1. [https://coreos.com/etcd](https://coreos.com/etcd)
1. [https://kubernetes.io/docs/admin/etcd/](https://kubernetes.io/docs/admin/etcd/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7

5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
