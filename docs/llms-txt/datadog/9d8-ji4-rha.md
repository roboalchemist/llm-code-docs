# Source: https://docs.datadoghq.com/security/default_rules/9d8-ji4-rha.md

---
title: All requests should not be allowed; explicit authorization should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > All requests should not be allowed;
  explicit authorization should be enabled
---

# All requests should not be allowed; explicit authorization should be enabled
Classification:complianceFramework:cis-kubernetesControl:4.2.2 
## Description{% #description %}

Do not allow all requests. Enable explicit authorization.

## Rationale{% #rationale %}

Kubelets, by default, allow all authenticated requests (even anonymous ones) without needing explicit authorization checks from the API server. You should restrict this behavior and only allow explicitly authorized requests.

## Audit{% #audit %}

Run the following command on each node: `ps -ef | grep kubelet`. If the `--authorization-mode` argument is present check that it is not set to AlwaysAllow. If it is not present check that there is a Kubelet config file specified by `--config`, and that file sets authorization: mode to something other than AlwaysAllow. It is also possible to review the running configuration of a Kubelet via the /configs endpoint on the Kubelet API port (typically `10250/TCP`). Accessing these with appropriate credentials will provide details of the Kubelet's configuration.

## Remediation{% #remediation %}

If using a Kubelet config file, edit the file to set authorization: mode to Webhook. If using executable arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_AUTHZ_ARGS` variable.

`--authorization-mode=Webhook`

Based on your system, restart the kubelet service. For example: `systemctl daemon-reload systemctl restart kubelet.service`

## Impact{% #impact %}

Unauthorized requests will be denied.

## Default value{% #default-value %}

By default, `--authorization-mode` argument is set to `AlwaysAllow`.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kubelet/](https://kubernetes.io/docs/admin/kubelet/)
1. [https://kubernetes.io/docs/admin/kubelet-authentication-authorization/#kubelet-authentication](https://kubernetes.io/docs/admin/kubelet-authentication-authorization/#kubelet-authentication)

## CIS controls{% #cis-controls %}

Version 6.14 Controlled Access Based on the Need to Know Version 7.14 Controlled Access Based on the Need to Know
