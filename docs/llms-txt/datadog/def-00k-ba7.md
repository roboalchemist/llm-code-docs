# Source: https://docs.datadoghq.com/security/default_rules/def-00k-ba7.md

---
title: The Kubernetes admission controller 'AlwaysAdmit' should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes admission controller
  'AlwaysAdmit' should be disabled
---

# The Kubernetes admission controller 'AlwaysAdmit' should be disabled
 
## Description{% #description %}

The cluster should not allow all requests. The `AlwaysAdmit` admission controller plugin allows all requests and does not filter any requests; it should not be enabled.

## Remediation{% #remediation %}

1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and either remove the `--enable-admission-plugins` parameter, or set it to a value that does not include `AlwaysAdmit`.

**Note**: The `AlwaysAdmit` admission controller was deprecated in v1.13 and should not be used. Its behavior is equivalent to having no admission controller. Refer to the [Kubernetes admission controller documentation](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#alwaysadmit) for additional information.
