# Source: https://docs.datadoghq.com/security/default_rules/def-000-dn7.md

---
title: GKE Kubelet kubeconfig file ownership should be assigned to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GKE Kubelet kubeconfig file ownership
  should be assigned to root
---

# GKE Kubelet kubeconfig file ownership should be assigned to root

## Description{% #description %}

Ensure that the file ownership of the kubelet's kubeconfig file is set to `root:root`. You should set its file ownership to maintain integrity.

## Remediation{% #remediation %}

Run the following command to fix the kubelet configuration file's ownership:

```bash
chown root:root /var/lib/kubelet/kubeconfig
```

**Note**: The path above is the default location.
