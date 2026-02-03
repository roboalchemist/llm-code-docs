# Source: https://docs.datadoghq.com/security/default_rules/def-00k-4dk.md

---
title: The Kubernetes API server request timeout should not exceed 60 seconds
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server request
  timeout should not exceed 60 seconds
---

# The Kubernetes API server request timeout should not exceed 60 seconds
 
## Description{% #description %}

The global request timeout for API server requests should not exceed 60 seconds. Setting the timeout limit above 60 seconds can exhaust the API server resources making it prone to Denial-of-Service attacks. It is recommended to only change the default limit of 60 seconds when necessary.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` and set the below parameter to 60. For example, `--request-timeout=60s`.
