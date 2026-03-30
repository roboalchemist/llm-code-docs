# Source: https://docs.datadoghq.com/security/default_rules/def-00k-3nh.md

---
title: The kubelet.conf file should have permissions of 600 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet.conf file should have
  permissions of 600 or more restrictive
---

# The kubelet.conf file should have permissions of 600 or more restrictive

## Description{% #description %}

The kubelet.conf file should have permissions of `600` or more restrictive. The `kubelet.conf` file is the kubeconfig file for the node, and controls various parameters that set the behavior and identity of the worker node. You should restrict its file permissions to maintain the integrity of the file. The file should be writable only by the administrators of the system.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chmod 600 /etc/kubernetes/kubelet.conf
   ```
