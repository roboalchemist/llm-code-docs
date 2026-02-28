# Source: https://docs.datadoghq.com/security/default_rules/def-00k-mfh.md

---
title: The kubelet service file should have permissions of 600 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet service file should have
  permissions of 600 or more restrictive
---

# The kubelet service file should have permissions of 600 or more restrictive

## Description{% #description %}

The kubelet service file should have permissions of `600` or more restrictive. The kubelet service file controls various parameters that set the behavior of the kubelet service in the worker node. You should restrict its file permissions to maintain the integrity of the file. The file should be writable only by the administrators of the system.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chmod 600 /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
   ```
