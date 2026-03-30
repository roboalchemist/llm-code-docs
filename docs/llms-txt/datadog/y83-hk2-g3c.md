# Source: https://docs.datadoghq.com/security/default_rules/y83-hk2-g3c.md

---
title: Kubelet server certificate rotation should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet server certificate rotation
  should be enabled
---

# Kubelet server certificate rotation should be enabled
Classification:complianceFramework:cis-kubernetesControl:4.2.12
## Description{% #description %}

Enable kubelet server certificate rotation.

## Rationale{% #rationale %}

`RotateKubeletServerCertificate` causes the kubelet to both request a serving certificate after bootstrapping its client credentials and rotate the certificate as its existing credentials expire. This automated periodic rotation ensures that the there are no downtimes due to expired certificates and thus addressing availability in the CIA security triad.

*Note*: This recommendation only applies if you let kubelets get their certificates from the API server. In case your kubelet certificates come from an outside authority/tool (e.g. Vault) then you need to take care of rotation yourself.

## Audit{% #audit %}

Run the following command on each node: `ps -ef | grep kubelet`. Verify that `RotateKubeletServerCertificate` argument exists and is set to `true`.

## Remediation{% #remediation %}

On the master edit `/var/lib/kubelet/kubeadm-flags.env` and set the parameter `KUBELET_CERTIFICATE_ARGS --feature-gates=RotateKubeletServerCertificate=true` or as an alternative, and suggested as a last resort, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_CERTIFICATE_ARGS` variable:

```
--feature-gates=RotateKubeletServerCertificate=true
```

Based on your system, restart the kubelet service. For example: `systemctl daemon-reload systemctl restart kubelet.service`

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, kubelet server certificate rotation is disabled.

## References{% #references %}

1. [https://github.com/kubernetes/kubernetes/pull/45059](https://github.com/kubernetes/kubernetes/pull/45059)
1. [https://kubernetes.io/docs/admin/kubelet-tls-bootstrapping/#kubelet-configuration](https://kubernetes.io/docs/admin/kubelet-tls-bootstrapping/#kubelet-configuration)

## CIS controls{% #cis-controls %}

Version 6.14.2 Encrypt All Sensitive Information Over Less-trusted Networks - All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted.

Version 7.14.4 Encrypt All Sensitive Information in Transit - Encrypt all sensitive information in transit.
