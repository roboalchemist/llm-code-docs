# Source: https://docs.datadoghq.com/security/default_rules/rf4-zcq-5j9.md

---
title: >-
  The --audit-policy-file flag should be set for Kubernetes logging to be
  enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The --audit-policy-file flag should be
  set for Kubernetes logging to be enabled
---

# The --audit-policy-file flag should be set for Kubernetes logging to be enabled
Classification:complianceFramework:cis-kubernetesControl:3.2.1
## Description{% #description %}

Kubernetes can audit the details of requests made to the API server. The `--audit-policy-file` flag must be set for this logging to be enabled.

## Rationale{% #rationale %}

Logging is an important detective control for all systems, to detect potential unauthorised access.

## Audit{% #audit %}

Run the following command on one of the cluster master nodes:

```
ps -ef | grep kube-apiserver
```

Verify that the `--audit-policy-file` is set. Review the contents of the file specified and ensure that it contains a valid audit policy.

## Remediation{% #remediation %}

Create an audit policy file for your cluster.

## Impact{% #impact %}

Audit logs will be created on the master nodes, which will consume disk space. Care should be taken to avoid generating too large volumes of log information as this could impact the available of the cluster nodes.

## Default value{% #default-value %}

Unless the `--audit-policy-file` flag is specified, no auditing will be carried out.

## References{% #references %}

1. [https://kubernetes.io/docs/tasks/debug-application-cluster/audit/](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/)

## CIS controls{% #cis-controls %}

Version 7.6.2 Activate audit logging - Ensure that local logging has been enabled on all systems and networking devices.
