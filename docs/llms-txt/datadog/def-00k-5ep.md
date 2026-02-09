# Source: https://docs.datadoghq.com/security/default_rules/def-00k-5ep.md

---
title: API server audit logs should be retained for at least 30 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API server audit logs should be
  retained for at least 30 days
---

# API server audit logs should be retained for at least 30 days
 
## Description{% #description %}

The audit log's max age should be at least 30 days. Retaining logs for at least 30 days ensures that you can go back in time and investigate or correlate any events.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--audit-log-maxage` parameter to `30` or as an appropriate number of days: `--audit-log-maxage=30`
