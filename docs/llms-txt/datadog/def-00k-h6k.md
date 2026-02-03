# Source: https://docs.datadoghq.com/security/default_rules/def-00k-h6k.md

---
title: Etcd should be configured with TLS encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd should be configured with TLS
  encryption
---

# Etcd should be configured with TLS encryption
 
## Description{% #description %}

TLS encryption for the etcd service should be configured.

## Rationale{% #rationale %}

Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of REST API objects. These objects are sensitive in nature and should be encrypted in transit.

## Remediation{% #remediation %}

Follow the [etcd service documentation](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/) and configure TLS encryption. Then, edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and set the following parameters:

```
--cert-file=</path/to/ca-file> 
--key-file=</path/to/key-file>
```
