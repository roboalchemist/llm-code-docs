# Source: https://docs.datadoghq.com/security/default_rules/def-00k-qda.md

---
title: The scheduler configuration file ownership should be assigned to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The scheduler configuration file
  ownership should be assigned to root
---

# The scheduler configuration file ownership should be assigned to root
 
## Description{% #description %}

The `scheduler.conf` file ownership should be set to `root:root`. This is the kubeconfig file for the scheduler. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/scheduler.conf
   ```
