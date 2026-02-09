# Source: https://docs.datadoghq.com/security/default_rules/def-00k-gnc.md

---
title: The Controller Manager API service should be bound to localhost
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Controller Manager API service
  should be bound to localhost
---

# The Controller Manager API service should be bound to localhost
 
## Description{% #description %}

The Controller Manager service should not be bound to a non-loopback address. The Controller Manager API service which runs on port 10252/TCP by default is used for health and metrics information and is available without authentication or encryption.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and ensure the correct value for the `--bind-address` parameter. For example, `--bind-address=127.0.0.1`.
