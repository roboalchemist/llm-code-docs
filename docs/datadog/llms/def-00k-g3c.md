# Source: https://docs.datadoghq.com/security/default_rules/def-00k-g3c.md

---
title: The kubelet server certificate rotation should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet server certificate rotation
  should be enabled
---

# The kubelet server certificate rotation should be enabled

## Description{% #description %}

Kubelet server certificate rotation should be enabled. `RotateKubeletServerCertificate` causes the kubelet to both request a serving certificate after bootstrapping its client credentials and rotate the certificate as its existing credentials expire. This automated periodic rotation ensures that the there are no downtimes due to expired certificates and thus addressing availability in the CIA security triad.

*Note*: This recommendation only applies if you let kubelets get their certificates from the API server. If your kubelet certificates come from an outside authority/tool (e.g. Vault), you need to handle the rotation manually.

## Remediation{% #remediation %}

1. On the master node, edit `/var/lib/kubelet/kubeadm-flags.env` and set the parameter `KUBELET_CERTIFICATE_ARGS` to include `--feature-gates=RotateKubeletServerCertificate=true` or as an alternative, and suggested as a last resort, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_CERTIFICATE_ARGS` variable:

```
--feature-gates=RotateKubeletServerCertificate=true
```
Restart the kubelet service.