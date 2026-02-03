# Source: https://docs.datadoghq.com/security/default_rules/def-000-5nt.md

---
title: >-
  An EKS Cluster's kubelet configuration file ownership should be assigned to
  root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An EKS Cluster's kubelet configuration
  file ownership should be assigned to root
---

# An EKS Cluster's kubelet configuration file ownership should be assigned to root
 
## Description{% #description %}

Ensure that if the kubelet refers to a configuration file with the `--config` argument. You should set its file ownership to maintain integrity and the file should be owned by `root:root`.

## Remediation{% #remediation %}

Run the following command to fix the kubelet configuration file's permissions:

```bash
chown root:root /etc/kubernetes/kubelet/kubelet-config.json
```

**Note**: The path above is the default location in EKS.
