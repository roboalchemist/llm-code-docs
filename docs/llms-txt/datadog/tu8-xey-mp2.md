# Source: https://docs.datadoghq.com/security/default_rules/tu8-xey-mp2.md

---
title: Self-signed certificates should not be used for etcd TLS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Self-signed certificates should not be
  used for etcd TLS
---

# Self-signed certificates should not be used for etcd TLS
Classification:complianceFramework:cis-kubernetesControl:2.3 
## Description{% #description %}

Do not use self-signed certificates for TLS.

## Rationale{% #rationale %}

Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should not be available to unauthenticated clients. You should enable the client authentication via valid certificates to secure the access to the etcd service.

## Audit{% #audit %}

Run the following command on the etcd server node:

```
ps -ef | grep etcd
```

Verify that if the `--auto-tls` argument exists, it is not set to `true`.

## Remediation{% #remediation %}

Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and either remove the `--auto-tls` parameter or set it to false:

```
--auto-tls=false
```

## Impact{% #impact %}

Clients will not be able to use self-signed certificates for TLS.

## Default value{% #default-value %}

By default, `--auto-tls` is set to false.

## References{% #references %}

1. [https://coreos.com/etcd/docs/latest/op-guide/security.html](https://coreos.com/etcd/docs/latest/op-guide/security.html)
1. [https://kubernetes.io/docs/admin/etcd/](https://kubernetes.io/docs/admin/etcd/)
1. [https://coreos.com/etcd/docs/latest/op-guide/configuration.html#auto-tls](https://coreos.com/etcd/docs/latest/op-guide/configuration.html#auto-tls)

## CIS controls{% #cis-controls %}

Version 6 14.2 Encrypt All Sensitive Information Over Less-trusted Networks All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted. Version 7 14.4 Encrypt All Sensitive Information in Transit Encrypt all sensitive information in transit.
