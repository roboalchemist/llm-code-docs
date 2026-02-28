# Source: https://docs.datadoghq.com/security/default_rules/def-00k-5rj.md

---
title: The API Server should require HTTPS connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API Server should require HTTPS
  connections
---

# The API Server should require HTTPS connections

## Description{% #description %}

TLS should be set up on the Kubernetes API server. API server communication contains sensitive parameters that should remain encrypted in transit.

## Remediation{% #remediation %}

1. Follow the [Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) and set up the TLS connection on the apiserver.
1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the TLS certificate and private key file parameters.

```
--tls-cert-file=<path/to/tls-certificate-file>
--tls-private-key-file=<path/to/tls-key-file>
```
