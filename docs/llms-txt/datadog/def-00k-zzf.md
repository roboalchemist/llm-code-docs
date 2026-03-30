# Source: https://docs.datadoghq.com/security/default_rules/def-00k-zzf.md

---
title: The Kubernetes PKI directories should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes PKI directories should
  be owned by root
---

# The Kubernetes PKI directories should be owned by root

## Description{% #description %}

Ensure that the Kubernetes PKI directories and subsequent certificate files are owned by `root:root`. Kubernetes makes use of a number of certificates as part of its operation. You should set the ownership of the directory containing the PKI information and all files in that directory to maintain their integrity.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown -R root:root /etc/kubernetes/pki/
   ```
