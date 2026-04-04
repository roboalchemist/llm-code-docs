# Source: https://docs.datadoghq.com/security/default_rules/def-00k-7jy.md

---
title: The etcd data directory should have permissions of 700 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The etcd data directory should have
  permissions of 700 or more restrictive
---

# The etcd data directory should have permissions of 700 or more restrictive

## Description{% #description %}

The etcd data directory should have permissions of `700` or more restrictive. Etcd is a highly-available key-value store used by Kubernetes deployments for persistent storage of all of its REST API objects. This data directory should be protected from any unauthorized reads or writes. It should not be readable or writable by any group members or the world.

## Remediation{% #remediation %}

1. Use the below command to retrieve the etcd data directory, passed as an argument `--data-dir`:
   ```
   ps -ef | grep etcd
   ```
1. Run the following command to adjust the file permissions based on the file location from above:
   ```
   chmod 700 /<path-to-etcd-data-dir>/etcd.yaml
   ```
