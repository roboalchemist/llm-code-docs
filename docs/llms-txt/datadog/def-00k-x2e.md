# Source: https://docs.datadoghq.com/security/default_rules/def-00k-x2e.md

---
title: The etcd data directory should be owned by the etcd user and group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The etcd data directory should be owned
  by the etcd user and group
---

# The etcd data directory should be owned by the etcd user and group

## Description{% #description %}

The etcd data directory ownership should be set to `etcd:etcd`. Etcd is a highly-available key-value store used by Kubernetes deployments for persistent storage of all of its REST API objects. This data directory should be protected from any unauthorized reads or writes.

## Remediation{% #remediation %}

1. Use the below command to retrieve the etcd data directory, passed as an argument `--data-dir`:
   ```
   ps -ef | grep etcd
   ```
1. Run the following command to adjust the file ownership based on the file location from above:
   ```
   chown etcd:etcd /<path-to-etcd-data-dir>/etcd.yaml
   ```
