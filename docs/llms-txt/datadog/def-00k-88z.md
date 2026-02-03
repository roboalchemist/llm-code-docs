# Source: https://docs.datadoghq.com/security/default_rules/def-00k-88z.md

---
title: The controller manager pod specification file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The controller manager pod
  specification file should be owned by root
---

# The controller manager pod specification file should be owned by root
 
## Description{% #description %}

The controller manager pod specification file ownership should be set to `root:root`. The controller manager pod specification file controls various parameters that set the behavior of various components of the master node. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/manifests/kube-controller-manager.yaml
   ```
