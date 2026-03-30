# Source: https://docs.datadoghq.com/security/default_rules/def-00k-j6m.md

---
title: Certificate-based kubelet authentication should be required
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Certificate-based kubelet
  authentication should be required
---

# Certificate-based kubelet authentication should be required

## Description{% #description %}

Certificate based kubelet authentication should be enabled. The API server, by default, does not authenticate itself to the kubelet's HTTPS endpoints. The requests from the API server are treated anonymously. Certificate-based kubelet authentication should be set up to ensure that the apiserver authenticates itself to kubelets when submitting requests.

## Remediation{% #remediation %}

Follow the [Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) and set up the TLS connection between the apiserver and kubelets. Then, edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the kubelet client certificate and key parameters as below.

```
--kubelet-client-certificate=<path/to/client-certificate-file>
--kubelet-client-key=<path/to/client-key-file>
```
