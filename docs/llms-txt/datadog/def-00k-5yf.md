# Source: https://docs.datadoghq.com/security/default_rules/def-00k-5yf.md

---
title: Etcd pod specification file should have permissions of 600 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Etcd pod specification file should have
  permissions of 600 or more restrictive
---

# Etcd pod specification file should have permissions of 600 or more restrictive
 
## Description{% #description %}

The `/etc/kubernetes/manifests/etcd.yaml` file should have permissions of 600 or more restrictive. The file controls various parameters that set the behavior of the etcd service in the master node. Etcd is a highly-available key-value store which Kubernetes uses for persistent storage of all of its REST API object. You should restrict the file permissions to maintain the integrity of the file. The file should be writable by only the administrators on the system.

## Remediation{% #remediation %}

1. Run the following command to adjust the file permissions:
   ```
   chmod 600 /etc/kubernetes/manifests/etcd.yaml
   ```
