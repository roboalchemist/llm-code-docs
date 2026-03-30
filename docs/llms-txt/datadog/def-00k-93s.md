# Source: https://docs.datadoghq.com/security/default_rules/def-00k-93s.md

---
title: The kubelet.conf file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet.conf file should be owned
  by root
---

# The kubelet.conf file should be owned by root

## Description{% #description %}

The `kubelet.conf` file ownership should be set to `root:root`. The `kubelet.conf` file is the kubeconfig file for the node, and controls various parameters that set the behavior and identity of the worker node. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/kubelet.conf
   ```
