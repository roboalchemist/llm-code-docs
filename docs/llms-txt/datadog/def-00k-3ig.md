# Source: https://docs.datadoghq.com/security/default_rules/def-00k-3ig.md

---
title: The etcd pod specification file should be owned by root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The etcd pod specification file should
  be owned by root
---

# The etcd pod specification file should be owned by root

## Description{% #description %}

The `/etc/kubernetes/manifests/etcd.yaml` file ownership should be set to `root:root`. The file controls various parameters that set the behavior of the etcd service in the master node. Etcd is a highly-available key-value store which Kubernetes uses for persistent storage of all of its REST API object. You should set its file ownership to maintain the integrity of the file.

## Remediation{% #remediation %}

1. Run the following command to adjust the file ownership:
   ```
   chown root:root /etc/kubernetes/manifests/etcd.yaml
   ```
