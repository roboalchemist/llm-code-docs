# Source: https://docs.datadoghq.com/security/default_rules/def-000-txc.md

---
title: The API server pod specification file ownership should be assigned to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API server pod specification file
  ownership should be assigned to root
---

# The API server pod specification file ownership should be assigned to root

## Description{% #description %}

The API server pod specification file ownership should be set to `root:root`. The API server pod specification file controls various parameters that set the behavior of the API server. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/manifests/kube-apiserver.yaml
   ```
