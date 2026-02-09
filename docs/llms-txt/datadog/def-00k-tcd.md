# Source: https://docs.datadoghq.com/security/default_rules/def-00k-tcd.md

---
title: The kubelet service file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet service file should be
  owned by root
---

# The kubelet service file should be owned by root
 
## Description{% #description %}

The kubelet service file ownership should be set to `root:root`. The kubelet service file controls various parameters that set the behavior of the kubelet service in the worker node. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
   ```
