# Source: https://docs.datadoghq.com/security/default_rules/def-00k-5j9.md

---
title: A Kubernetes audit policy should exist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > A Kubernetes audit policy should exist
---

# A Kubernetes audit policy should exist
 
## Description{% #description %}

Kubernetes should audit the details of requests made to the API server.

## Remediation{% #remediation %}

1. Refer to the [Kubernetes documentation](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) on how to create an audit policy file for your cluster.
1. Assign the policy to the `--audit-policy-file` parameter.

```
--audit-policy-file=<path-to-audit-policy-file>
```
