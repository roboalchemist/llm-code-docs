# Source: https://docs.datadoghq.com/security/default_rules/def-00k-rvn.md

---
title: Kube-proxy configuration file ownership should be assigned to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kube-proxy configuration file ownership
  should be assigned to root
---

# Kube-proxy configuration file ownership should be assigned to root
 
## Description{% #description %}

If kube-proxy is running, ensure that the file ownership of its kubeconfig file is set to `root:root`. The kube-proxy's kubeconfig file controls various parameters for the the service in the worker node. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the below command on each worker node:

```
chown root:root <proxy kubeconfig file>
```
