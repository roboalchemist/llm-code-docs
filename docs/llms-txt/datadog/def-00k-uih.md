# Source: https://docs.datadoghq.com/security/default_rules/def-00k-uih.md

---
title: Etcd should use TLS encryption for peer connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd should use TLS encryption for peer
  connections
---

# Etcd should use TLS encryption for peer connections
 
## Description{% #description %}

Etcd should be configured to make use of TLS encryption for peer connections. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be encrypted in transit and also amongst peers in the etcd clusters.

## Remediation{% #remediation %}

1. Follow the [etcd service documentation](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/) and configure peer TLS encryption as appropriate for your etcd cluster.
1. Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and set the following parameters:

```
--peer-cert-file=</path/to/peer-cert-file> 
--peer-key-file=</path/to/peer-key-file>
```
