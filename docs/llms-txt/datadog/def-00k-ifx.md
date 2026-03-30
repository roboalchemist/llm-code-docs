# Source: https://docs.datadoghq.com/security/default_rules/def-00k-ifx.md

---
title: Kubelet should use TLS certificate client authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet should use TLS certificate
  client authentication
---

# Kubelet should use TLS certificate client authentication

## Description{% #description %}

Kubelet authentication should use certificates. The connections from the API server to the kubelet are used for fetching logs for pods, attaching (through kubectl) to running pods, and using the kubelet's port-forwarding functionality. These connections terminate at the kubelet's HTTPS endpoint.

## Remediation{% #remediation %}

1. If using a Kubelet config file, edit the file to set `authentication: x509: clientCAFile` to the location of the client CA file.
1. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in the `KUBELET_AUTHZ_ARGS` variable.

```
--client-ca-file=<path/to/client-ca-file>
```
Restart the kubelet service.