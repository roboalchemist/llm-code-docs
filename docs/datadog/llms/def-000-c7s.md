# Source: https://docs.datadoghq.com/security/default_rules/def-000-c7s.md

---
title: The GKE kubeconfig file should have permissions set to 644 or more restrictive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The GKE kubeconfig file should have
  permissions set to 644 or more restrictive
---

# The GKE kubeconfig file should have permissions set to 644 or more restrictive

## Description{% #description %}

If kubelet is configured by a kubeconfig file, ensure that the kubeconfig file has permissions of `644` or more restrictive. The kubelet kubeconfig file contains authentication credentials used by the kubelet service in the worker node to connect to the main Kubernetes API. You should restrict its file permissions to maintain the integrity of the file. The file should only be writable by the administrators on the system.

## Remediation{% #remediation %}

Run the following command to fix the kubelet configuration file's permissions:

```bash
chmod 644 /var/lib/kubelet/kubeconfig
```

**Note**: The path above is the default location.
