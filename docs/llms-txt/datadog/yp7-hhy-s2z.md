# Source: https://docs.datadoghq.com/security/default_rules/yp7-hhy-s2z.md

---
title: etcd should use TLS encryption for client connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > etcd should use TLS encryption for
  client connections
---

# etcd should use TLS encryption for client connections
Classification:complianceFramework:cis-kubernetesControl:1.2.32
## Description{% #description %}

etcd should be configured to make use of TLS encryption for client connections.

## Rationale{% #rationale %}

etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be protected by client authentication. This requires the API server to identify itself to the etcd server using a SSL Certificate Authority file.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--etcd-cafile` argument exists and it is set as appropriate.

## Remediation{% #remediation %}

Follow the Kubernetes documentation and set up the TLS connection between the apiserver and etcd. Then, edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the etcd certificate authority file parameter: `--etcd-cafile=<path/to/ca-file>`

## Impact{% #impact %}

TLS and client certificate authentication must be configured for etcd.

## Default value{% #default-value %}

By default, `--etcd-cafile` is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://coreos.com/etcd/docs/latest/op-guide/security.html](https://coreos.com/etcd/docs/latest/op-guide/security.html)

## CIS controls{% #cis-controls %}

Version 6 14.2 Encrypt All Sensitive Information Over Less-trusted Networks - All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted.

Version 7 14.4 Encrypt All Sensitive Information in Transit - Encrypt all sensitive information in transit.
