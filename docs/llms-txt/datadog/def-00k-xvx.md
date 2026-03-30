# Source: https://docs.datadoghq.com/security/default_rules/def-00k-xvx.md

---
title: >-
  The controller manager pod specification file should have permissions of 600
  or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The controller manager pod
  specification file should have permissions of 600 or more restrictive
---

# The controller manager pod specification file should have permissions of 600 or more restrictive

## Description{% #description %}

The controller manager pod specification file should have permissions of 600 or more restrictive. The controller manager pod specification file controls various parameters that set the behavior of the controller manager on the master node. You should restrict its file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Remediation{% #remediation %}

1. Run the following command to adjust the file permissions:
   ```
   chmod 600 /etc/kubernetes/manifests/kube-apiserver.yaml
   ```
