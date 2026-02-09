# Source: https://docs.datadoghq.com/security/default_rules/def-00k-g9s.md

---
title: >-
  Kubernetes PKI certificate files should have permissions of 600 or more
  restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubernetes PKI certificate files should
  have permissions of 600 or more restrictive
---

# Kubernetes PKI certificate files should have permissions of 600 or more restrictive
 
## Description{% #description %}

Ensure that Kubernetes PKI certificate files have permissions of `600` or more restrictive. Kubernetes makes use of a number of certificate files as part of the operation of its components. The permissions on these files should be set to 600 or more restrictive to protect their integrity.

## Remediation{% #remediation %}

1. Run the following command to adjust the file permissions:
   ```
   chmod -R 600 /etc/kubernetes/pki/*.crt
   ```
