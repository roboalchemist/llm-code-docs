# Source: https://docs.datadoghq.com/security/default_rules/def-00k-6k8.md

---
title: >-
  TLS connections between etcd peers should not use self-signed certificates
  that are automatically generated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > TLS connections between etcd peers
  should not use self-signed certificates that are automatically generated
---

# TLS connections between etcd peers should not use self-signed certificates that are automatically generated
 
## Description{% #description %}

Automatically generated self-signed certificates for TLS connections between peers should not be used. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of REST API objects. These objects are sensitive in nature and should be accessible only by authenticated etcd peers in the etcd cluster. Hence, do not use self-signed certificates for authentication.

## Remediation{% #remediation %}

Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and either remove the `--peer-auto-tls` parameter or set it to false.

```
--peer-auto-tls=false
```
