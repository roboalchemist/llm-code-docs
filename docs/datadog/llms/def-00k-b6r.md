# Source: https://docs.datadoghq.com/security/default_rules/def-00k-b6r.md

---
title: Etcd should have client authentication enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd should have client authentication
  enabled
---

# Etcd should have client authentication enabled

## Description{% #description %}

Client authentication should be enabled on the etcd service. You should enable the client authentication via valid certificates to secure the access to the etcd service. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of REST API objects. These objects are sensitive in nature and should not be available to unauthenticated clients.

## Remediation{% #remediation %}

Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and set the following parameter:

```
--client-cert-auth=true
```
