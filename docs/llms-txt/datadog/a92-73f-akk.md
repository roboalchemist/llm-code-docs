# Source: https://docs.datadoghq.com/security/default_rules/a92-73f-akk.md

---
title: The proxy kubeconfig file should have permissions of 644 or stricter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The proxy kubeconfig file should have
  permissions of 644 or stricter
---

# The proxy kubeconfig file should have permissions of 644 or stricter
Classification:complianceFramework:cis-kubernetesControl:4.1.3 
## Description{% #description %}

If kube-proxy is running, and if it is using a file-based kubeconfig file, ensure that the proxy kubeconfig file has permissions of 644 or more restrictive.

## Rationale{% #rationale %}

The kube-proxy kubeconfig file controls various parameters of the kube-proxy service in the worker node. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system. It is possible to run kube-proxy with the kubeconfig parameters configured as a Kubernetes ConfigMap instead of a file. In this case, there is no proxy kubeconfig file.

## Audit{% #audit %}

Find the kubeconfig file being used by `kube-proxy` by running the following command: `ps -ef | grep kube-proxy`. If `kube-proxy` is running, get the kubeconfig file location from the `--kubeconfig` parameter.

Run the following command (based on the file location on your system) on the each worker node. For example, `stat -c %a <proxy kubeconfig file>`. Verify that if a file is specified and it exists, the permissions are 644 or more restrictive.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the each worker node:

```
chmod 644 <proxy kubeconfig file>
```

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, proxy file has permissions of 640.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-proxy/](https://kubernetes.io/docs/admin/kube-proxy/)

## CIS controls{% #cis-controls %}

Version 6.5.1 Minimize And Sparingly Use Administrative Privileges - Minimize administrative privileges and only use administrative accounts when they are required. Implement focused auditing on the use of administrative privileged functions and monitor for anomalous behavior.

Version 7.5.2 Maintain Secure Images - Maintain secure images or templates for all systems in the enterprise based on the organization's approved configuration standards. Any new system deployment or existing system that becomes compromised should be imaged using one of those images or templates.
