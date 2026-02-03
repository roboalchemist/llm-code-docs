# Source: https://docs.datadoghq.com/security/default_rules/def-00k-kyz.md

---
title: Each controller should use individual service account credentials
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Each controller should use individual
  service account credentials
---

# Each controller should use individual service account credentials
 
## Description{% #description %}

Each controller should use individual service account credentials. The controller manager creates a service account per controller in the kube-system namespace, generates a credential for it, and builds a dedicated API client with that service account credential for each controller loop to use. Setting the `--use-service-account-credentials` to true runs each control loop within the controller manager using a separate service account credential. When used in combination with RBAC, this ensures that the control loops run with the minimum permissions required to perform their intended tasks.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node to set the below parameter:

```
--use-service-account-credentials=true
```
