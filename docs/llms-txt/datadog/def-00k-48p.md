# Source: https://docs.datadoghq.com/security/default_rules/def-00k-48p.md

---
title: Kubelet should require HTTPS connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet should require HTTPS
  connections
---

# Kubelet should require HTTPS connections
 
## Description{% #description %}

Setup TLS connection on the Kubelets.

## Rationale{% #rationale %}

Kubelet communication contains sensitive parameters that should remain encrypted in transit. Configure the Kubelets to serve only HTTPS traffic.

## Remediation{% #remediation %}

1. If using a Kubelet config file, edit the file to set `tlsCertFile` to the location of the certificate file to use to identify this Kubelet, and `tlsPrivateKeyFile` to the location of the corresponding private key file.
1. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameters in `KUBELET_CERTIFICATE_ARGS` variable.

```
--tls-cert-file=<path/to/tls-certificate-file>
--tls-private-key-file=<path/to/tls-key-file>
```
Restart the kubelet service.