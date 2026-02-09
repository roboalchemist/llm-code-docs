# Source: https://docs.datadoghq.com/security/default_rules/def-00k-ur6.md

---
title: >-
  Etcd server should require API servers to present a client certificate and key
  when connecting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd server should require API servers
  to present a client certificate and key when connecting
---

# Etcd server should require API servers to present a client certificate and key when connecting
 
## Description{% #description %}

Etcd should be configured to make use of TLS encryption for client connections. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be protected by client authentication. This requires the API server to identify itself to the etcd server using a client certificate and key.

## Remediation{% #remediation %}

Follow the [Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/) and set up the TLS connection between the apiserver and etcd. Then, edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the etcd certificate and key file parameters.

```
--etcd-certfile=<path/to/client-certificate-file> 
--etcd-keyfile=<path/to/client-key-file>
```
