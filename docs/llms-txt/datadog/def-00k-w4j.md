# Source: https://docs.datadoghq.com/security/default_rules/def-00k-w4j.md

---
title: >-
  The kubelet server certificate rotation on the controller-manager should be
  enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The kubelet server certificate rotation
  on the controller-manager should be enabled
---

# The kubelet server certificate rotation on the controller-manager should be enabled
 
## Description{% #description %}

Kubelet server certificate rotation should be enabled on the controller manager. This causes the kubelet to request a serving certificate after bootstrapping its client credentials, as well as rotating the certificate when its existing credentials expire. This automated periodic rotation ensures that the there are no downtimes due to expired certificates, thus addressing availability in the CIA security triad.

**Note**: This recommendation only applies if you allow kubelets to retrieve their certificates from the API server. If your kubelet certificates come from an outside authority/tool (e.g. Vault), you must rotate the certificates yourself.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and set the `--feature-gates` parameter to include `RotateKubeletServerCertificate=true`.
