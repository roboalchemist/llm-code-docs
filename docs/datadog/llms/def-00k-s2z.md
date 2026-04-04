# Source: https://docs.datadoghq.com/security/default_rules/def-00k-s2z.md

---
title: >-
  The etcd server should require API servers to present an SSL CA file when
  connecting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The etcd server should require API
  servers to present an SSL CA file when connecting
---

# The etcd server should require API servers to present an SSL CA file when connecting

## Description{% #description %}

Etcd should be configured to make use of TLS encryption for client connections. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be protected by client authentication. This requires the API server to identify itself to the etcd server using a SSL Certificate Authority file.

## Remediation{% #remediation %}

Follow the Kubernetes documentation and set up the TLS connection between the apiserver and etcd. Then, edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the etcd certificate authority file parameter: `--etcd-cafile=<path/to/ca-file>`
