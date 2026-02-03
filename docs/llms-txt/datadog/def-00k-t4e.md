# Source: https://docs.datadoghq.com/security/default_rules/def-00k-t4e.md

---
title: API server audit logs should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > API server audit logs should be enabled
---

# API server audit logs should be enabled
 
## Description{% #description %}

Auditing should be enabled on the Kubernetes API Server. Auditing the Kubernetes API Server provides a security-relevant chronological set of records documenting the sequence of activities that have affected the system by individual users, administrators, or other components of the system.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the parameter to a desired location. For example, `--audit-log-path=/var/log/apiserver/audit.log`.
