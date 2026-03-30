# Source: https://docs.datadoghq.com/security/default_rules/def-00k-ehd.md

---
title: The Kubernetes API server should use TLS certificate client authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Kubernetes API server should use
  TLS certificate client authentication
---

# The Kubernetes API server should use TLS certificate client authentication

## Description{% #description %}

TLS connections should be enabled on the API server. The API server communication contains sensitive parameters that should remain encrypted in transit.

## Remediation{% #remediation %}

1. Follow the Kubernetes documentation and set up the [TLS](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) connection on the apiserver.
1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the client certificate authority file: `--client-ca-file=<path/to/client-ca-file>`
