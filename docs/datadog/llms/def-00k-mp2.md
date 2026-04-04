# Source: https://docs.datadoghq.com/security/default_rules/def-00k-mp2.md

---
title: Etcd should only allow the use of valid client certificates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd should only allow the use of valid
  client certificates
---

# Etcd should only allow the use of valid client certificates

## Description{% #description %}

Self-signed certificates for TLS should not be used. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of REST API objects. These objects are sensitive in nature and should not be available to unauthenticated clients. You should enable the client authentication via valid certificates to secure the access to the etcd service.

## Remediation{% #remediation %}

Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and either remove the `--auto-tls` parameter or set it to false:

```
--auto-tls=false
```
