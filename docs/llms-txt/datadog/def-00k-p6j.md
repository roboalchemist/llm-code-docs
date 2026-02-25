# Source: https://docs.datadoghq.com/security/default_rules/def-00k-p6j.md

---
title: >-
  The Kubernetes API server should use secure authentication methods and avoid
  using token-based authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server should use
  secure authentication methods and avoid using token-based authentication
---

# The Kubernetes API server should use secure authentication methods and avoid using token-based authentication

## Description{% #description %}

Token-based authentication should not be used. Token-based authentication uses static tokens to authenticate requests to the API server. The tokens are stored in clear-text in a file on the API server, and cannot be revoked or rotated without restarting the API server.

## Remediation{% #remediation %}

1. Follow the configuration documentation for an alternate authentication method like [TLS](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/).
1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and remove the `--token-auth-file=<filename>` parameter.
