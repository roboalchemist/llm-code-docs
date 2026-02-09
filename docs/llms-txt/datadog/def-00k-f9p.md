# Source: https://docs.datadoghq.com/security/default_rules/def-00k-f9p.md

---
title: Etcd key-value store should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd key-value store should be
  encrypted at rest
---

# Etcd key-value store should be encrypted at rest
 
## Description{% #description %}

The etcd key-value store should be encrypted at rest. Etcd is a highly available key-value store used by Kubernetes deployments for persistent storage of all of its REST API objects. These objects are sensitive in nature and should be encrypted at rest to avoid any disclosures.

## Remediation{% #remediation %}

Follow the [Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) and configure a EncryptionConfig file. Then, edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--encryption-provider-config` parameter to the path of that file: `--encryption-provider-config=</path/to/EncryptionConfig/File>`
