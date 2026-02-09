# Source: https://docs.datadoghq.com/security/default_rules/def-00k-bjy.md

---
title: Etcd should have peer authentication configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd should have peer authentication
  configured
---

# Etcd should have peer authentication configured
 
## Description{% #description %}

Etcd should be configured for peer authentication. Etcd is a highly-available key value store used by Kubernetes deployments for persistent storage of REST API objects. These objects are sensitive in nature and should be accessible only by authenticated etcd peers in the etcd cluster.

## Remediation{% #remediation %}

Edit the etcd pod specification file `/etc/kubernetes/manifests/etcd.yaml` on the master node and set the following parameter:

```
--peer-client-cert-auth=true
```
