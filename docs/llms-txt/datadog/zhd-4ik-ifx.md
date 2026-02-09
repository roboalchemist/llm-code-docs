# Source: https://docs.datadoghq.com/security/default_rules/zhd-4ik-ifx.md

---
title: >-
  Kubelet should enable authentication using certificates for TLS client
  authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet should enable authentication
  using certificates for TLS client authentication
---

# Kubelet should enable authentication using certificates for TLS client authentication
Classification:complianceFramework:cis-kubernetesControl:4.2.3 
## Description{% #description %}

Enable Kubelet authentication using certificates.

## Rationale{% #rationale %}

The connections from the API server to the kubelet are used for fetching logs for pods, attaching (through kubectl) to running pods, and using the kubelet's port-forwarding functionality. These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle attacks, and unsafe to run over untrusted and/or public networks. Enabling Kubelet certificate authentication ensures that the API server could authenticate the Kubelet before submitting any requests.

## Audit{% #audit %}

Run the following command on each node: `ps -ef | grep kubelet`. Verify that the `--client-ca-file` argument exists and is set to the location of the client certificate authority file. If the `--client-ca-file` argument is not present, check that there is a Kubelet config file specified by `--config`, and that the file sets authentication: x509: clientCAFile to the location of the client certificate authority file.

## Remediation{% #remediation %}

If using a Kubelet config file, edit the file to set `authentication: x509: clientCAFile` to the location of the client CA file. If using command line arguments, edit the kubelet service file `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf` on each worker node and set the below parameter in `KUBELET_AUTHZ_ARGS` variable.

`--client-ca-file=<path/to/client-ca-file>`

Based on your system, restart the kubelet service. For example: `systemctl daemon-reload systemctl restart kubelet.service`

## Impact{% #impact %}

You require TLS to be configured on API server as well as kubelets.

## Default value{% #default-value %}

By default, `--client-ca-file argument` is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)

## CIS controls{% #cis-controls %}

Version 6.14.2 Encrypt All Sensitive Information Over Less-trusted Networks - All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted.

Version 7.14.4 Encrypt All Sensitive Information in Transit - Encrypt all sensitive information in transit.
