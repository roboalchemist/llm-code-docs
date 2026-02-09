# Source: https://docs.datadoghq.com/security/default_rules/def-00k-t3u.md

---
title: >-
  The API server audit log files should be rotated once the file reaches 100 MB
  or more
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API server audit log files should
  be rotated once the file reaches 100 MB or more
---

# The API server audit log files should be rotated once the file reaches 100 MB or more
 
## Description{% #description %}

On the API server, the log file should be at least 100 MB in size prior to log rotation. Retaining old log files ensures that you have sufficient log data available for carrying out any investigation or correlation.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--audit-log-maxsize` parameter to an appropriate size in MB.
