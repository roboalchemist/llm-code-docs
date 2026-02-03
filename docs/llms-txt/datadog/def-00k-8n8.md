# Source: https://docs.datadoghq.com/security/default_rules/def-00k-8n8.md

---
title: >-
  API server audit log files should be retained for at least 10 log file
  rotations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API server audit log files should be
  retained for at least 10 log file rotations
---

# API server audit log files should be retained for at least 10 log file rotations
 
## Description{% #description %}

Ten or more log files should be retained on the API server. Kubernetes automatically rotates the log files. Retaining old log files ensures that you would have sufficient log data available for carrying out any investigation or correlation.

## Remediation{% #remediation %}

1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--audit-log-maxbackup` parameter to at least `10`
