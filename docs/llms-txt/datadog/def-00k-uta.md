# Source: https://docs.datadoghq.com/security/default_rules/def-00k-uta.md

---
title: The `admin.conf` file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The `admin.conf` file should be owned
  by root
---

# The `admin.conf` file should be owned by root
 
## Description{% #description %}

Ensure that the `admin.conf` file ownership is set to `root:root`. This file contains the admin credentials for the cluster. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/admin.conf
   ```
