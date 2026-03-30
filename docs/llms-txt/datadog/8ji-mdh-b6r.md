# Source: https://docs.datadoghq.com/security/default_rules/8ji-mdh-b6r.md

---
title: Etcd service should have client authentication enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd service should have client
  authentication enabled
---

# Etcd service should have client authentication enabled
Classification:complianceFramework:cis-kubernetesControl:2.2
## Description{% #description %}

Enable client authentication on etcd service.

## Rationale{% #rationale %}

Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should not be available to unauthenticated clients. You should enable the client authentication via valid certificates to secure the access to the etcd service.

## Audit{% #audit %}

Run the following command on the etcd server node:

```
ps -ef | grep etcd
```

Verify that the `--client-cert-auth` argument is set to `true`.

## Remediation{% #remediation %}

Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and set the below parameter:

```
--client-cert-auth="true"
```

## Impact{% #impact %}

All clients attempting to access the etcd server will require a valid client certificate.

## Default value{% #default-value %}

By default, the etcd service can be queried by unauthenticated clients.

## References{% #references %}

1. [https://coreos.com/etcd/docs/latest/op-guide/security.html ][`]
1. [https://kubernetes.io/docs/admin/etcd/](https://coreos.com/etcd/docs/latest/op-guide/security.html)
1. [https://coreos.com/etcd/docs/latest/op-guide/configuration.html#client-cert-auth](https://kubernetes.io/docs/admin/etcd/)

## CIS controls{% #cis-controls %}

Version 6 14 Controlled Access Based on the Need to Know Controlled Access Based on the Need to Know Version 7 4 Controlled Use of Administrative Privileges Controlled Use of Administrative Privileges
