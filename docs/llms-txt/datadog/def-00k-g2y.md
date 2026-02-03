# Source: https://docs.datadoghq.com/security/default_rules/def-00k-g2y.md

---
title: The `controller-manager.conf` file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The `controller-manager.conf` file
  should be owned by root
---

# The `controller-manager.conf` file should be owned by root
 
## Description{% #description %}

The `controller-manager.conf` file ownership should be set to `root:root`. The `controller-manager.conf` file is the kubeconfig file for the Controller Manager. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/controller-manager.conf
   ```
