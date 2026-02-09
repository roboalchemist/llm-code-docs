# Source: https://docs.datadoghq.com/security/default_rules/b8a-e8g-h6k.md

---
title: The etcd service should be configured with TLS encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The etcd service should be configured
  with TLS encryption
---

# The etcd service should be configured with TLS encryption
Classification:complianceFramework:cis-kubernetesControl:2.1 
## Description{% #description %}

Configure TLS encryption for the etcd service.

## Rationale{% #rationale %}

Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be encrypted in transit.

## Audit{% #audit %}

Run the following command on the etcd server node:

```
ps -ef | grep etcd
```

Verify that the `--cert-file` and the `--key-file` arguments are set as appropriate.

## Remediation{% #remediation %}

Follow the etcd service documentation and configure TLS encryption. Then, edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and set the below parameters:

```
--cert-file=</path/to/ca-file> 
--key-file=</path/to/key-file>
```

## Impact{% #impact %}

Client connections only over TLS would be served.

## Default value{% #default-value %}

By default, TLS encryption is not set.

## References{% #references %}

1. [https://coreos.com/etcd/docs/latest/op-guide/security.html](https://coreos.com/etcd/docs/latest/op-guide/security.html)
1. [https://kubernetes.io/docs/admin/etcd/](https://kubernetes.io/docs/admin/etcd/)

## CIS controls{% #cis-controls %}

Version 6.14.2 Encrypt All Sensitive Information Over Less-trusted Networks - All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted.

Version 7.14.4 Encrypt All Sensitive Information in Transit - Encrypt all sensitive information in transit.
