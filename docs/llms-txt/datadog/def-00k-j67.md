# Source: https://docs.datadoghq.com/security/default_rules/def-00k-j67.md

---
title: >-
  The scheduler API service should not be bound to non-loopback insecure
  addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The scheduler API service should not be
  bound to non-loopback insecure addresses
---

# The scheduler API service should not be bound to non-loopback insecure addresses
 
## Description{% #description %}

The scheduler service should not be bound to non-loopback addresses. The Scheduler API service which runs on port 10251/TCP by default is used for health and metrics information and is available without authentication or encryption. As such, it should only be bound to a localhost interface to minimize the cluster's attack surface.

## Remediation{% #remediation %}

Edit the Scheduler pod specification file `/etc/kubernetes/manifests/kube-scheduler.yaml` on the master node and ensure the correct value for the `--bind-address` parameter. For example, `--bind-address=127.0.0.1`.
