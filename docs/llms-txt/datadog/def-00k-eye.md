# Source: https://docs.datadoghq.com/security/default_rules/def-00k-eye.md

---
title: The kubelet client certificate rotation should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet client certificate rotation
  should be enabled
---

# The kubelet client certificate rotation should be enabled
 
## Description{% #description %}

Kubelet client certificate rotation should be enabled. The `--rotate-certificates` setting tells the kubelet to rotate its client certificates by creating new CSRs when its existing credentials expire. This automated periodic rotation ensures that there is no downtime due to expired certificates and thus addresses availability in the CIA security triad.

**Note**: This recommendation only applies if you let kubelets get their certificates from the API server. In cases where your kubelet certificates come from an outside authority or tool (for example, Vault), then you need to manually do the rotation.

## Remediation{% #remediation %}

1. If using a kubelet config file, edit the file to add the line `rotateCertificates: true`.
1. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and add the argument below from the `KUBELET_CERTIFICATE_ARGS` variable.
   ```
   --rotate-certificates=true
   ```
1. Restart the kubelet service.
