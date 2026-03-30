# Source: https://docs.datadoghq.com/security/default_rules/def-00k-akk.md

---
title: >-
  Kube-proxy configuration file should have permissions of 600 or more
  restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kube-proxy configuration file should
  have permissions of 600 or more restrictive
---

# Kube-proxy configuration file should have permissions of 600 or more restrictive

## Description{% #description %}

If kube-proxy is running, ensure that the file permissions of the kubeconfig file is set to `600`. The kube-proxy's kubeconfig file controls various parameters for the the service in the worker node. You should set its file permissions to maintain the integrity of the file.

## Remediation{% #remediation %}

Run the below command (based on the file location on your system) on the each worker node:

```
chmod 600 <proxy kubeconfig file>
```
