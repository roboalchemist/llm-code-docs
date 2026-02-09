# Source: https://docs.datadoghq.com/security/default_rules/def-00k-9y8.md

---
title: The controller manager should have a service account private key file set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The controller manager should have a
  service account private key file set
---

# The controller manager should have a service account private key file set
 
## Description{% #description %}

A service account private key file should be set for service accounts on the controller manager. To ensure that keys for service account tokens can be rotated as needed, a separate public/private key pair should be used for signing service account tokens.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and set the `--service-account-private-key-file` parameter to the private key file for service accounts:

```
--service-account-private-key-file=<filename>
```
