# Source: https://docs.datadoghq.com/security/default_rules/ywu-bzc-zzf.md

---
title: The Kubernetes PKI directory should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes PKI directory should be
  owned by root
---

# The Kubernetes PKI directory should be owned by root
Classification:complianceFramework:cis-kubernetesControl:1.1.19 
## Description{% #description %}

Ensure that the Kubernetes PKI directory and file ownership is set to root:root.

## Rationale{% #rationale %}

Kubernetes makes use of a number of certificates as part of its operation. You should set the ownership of the directory containing the PKI information and all files in that directory to maintain their integrity. The directory and files should be owned by root:root.

## Audit{% #audit %}

Run the below command (based on the file location on your system) on the master node.

```bash
ls -laR /etc/kubernetes/pki/
```

Verify the ownership of all files and directories in this hierarchy is set to `root:root`.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the master node. For example, `chown -R root:root /etc/kubernetes/pki/`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, the `/etc/kubernetes/pki/` directory and all of the files and directories contained within it, are set to be owned by the root user.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)

## CIS controls{% #cis-controls %}

Version 6

5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.
