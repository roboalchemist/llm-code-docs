# Source: https://docs.datadoghq.com/security/default_rules/def-00k-d87.md

---
title: >-
  The `controller-manager.conf` file should have permissions of 600 or more
  restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The `controller-manager.conf` file
  should have permissions of 600 or more restrictive
---

# The `controller-manager.conf` file should have permissions of 600 or more restrictive
 
## Description{% #description %}

The `controller-manager.conf` file should have permissions of `600` or more restrictive. The `controller-manager.conf` file is the kubeconfig file for the Controller Manager. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Remediation{% #remediation %}

1. Run the following command to adjust the file permissions:
   ```
   chmod 600 /etc/kubernetes/controller-manager.conf
   ```
