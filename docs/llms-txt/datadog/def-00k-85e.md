# Source: https://docs.datadoghq.com/security/default_rules/def-00k-85e.md

---
title: >-
  API server should verify the kubelet's certificate before establishing
  connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API server should verify the kubelet's
  certificate before establishing connection
---

# API server should verify the kubelet's certificate before establishing connection
 
## Description{% #description %}

A kubelet's certificate should be verified before establishing a connection. The connections from the API server to the kubelet are used for fetching logs from pods, attaching the kubelet (through kubectl) to running pods, and using the kubelet's port-forwarding functionality.

## Remediation{% #remediation %}

1. Follow the Kubernetes documentation and set up the [TLS](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) connection between the apiserver and kubelets.
1. Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--kubelet-certificate-authority` parameter to the path of the cert file for the certificate authority.

```
--kubelet-certificate-authority=<ca-string>
```
