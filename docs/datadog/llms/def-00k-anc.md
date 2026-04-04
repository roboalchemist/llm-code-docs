# Source: https://docs.datadoghq.com/security/default_rules/def-00k-anc.md

---
title: The scheduler pod specification file ownership should be assigned to root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The scheduler pod specification file
  ownership should be assigned to root
---

# The scheduler pod specification file ownership should be assigned to root

## Description{% #description %}

The scheduler pod specification file ownership should be set to `root:root`. The scheduler pod specification file controls various parameters that set the behavior of the kube-scheduler service in the master node. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/manifests/kube-scheduler.yaml
   ```
