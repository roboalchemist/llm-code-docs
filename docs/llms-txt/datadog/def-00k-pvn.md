# Source: https://docs.datadoghq.com/security/default_rules/def-00k-pvn.md

---
title: The scheduler configuration file should only be alterable by owners
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The scheduler configuration file should
  only be alterable by owners
---

# The scheduler configuration file should only be alterable by owners
 
## Description{% #description %}

Ensure that the `scheduler.conf` file has permissions of `600` or more restrictive. This is the kubeconfig file for the scheduler. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Remediation{% #remediation %}

1. Run the following command to adjust the file permissions:
   ```
   chmod 600 /etc/kubernetes/scheduler.conf
   ```
