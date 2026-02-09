# Source: https://docs.datadoghq.com/security/default_rules/def-00k-dnt.md

---
title: Pods should use `root-ca-file` to pass serving certificates to the API server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Pods should use `root-ca-file` to pass
  serving certificates to the API server
---

# Pods should use `root-ca-file` to pass serving certificates to the API server
 
## Description{% #description %}

Pods should be allowed to verify the API server's serving certificate before establishing connections. Processes running in pods that need to contact the API server must verify the API server's serving certificate. Failure to do so could result in the pod being subject to man-in-the-middle attacks.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and set the `--root-ca-file` parameter to the certificate bundle file: `--root-ca-file=<path/to/file>`
