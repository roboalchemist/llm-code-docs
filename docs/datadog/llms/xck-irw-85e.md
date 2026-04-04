# Source: https://docs.datadoghq.com/security/default_rules/xck-irw-85e.md

---
title: The API server should verify the kubelet's certificate before connecting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API server should verify the
  kubelet's certificate before connecting
---

# The API server should verify the kubelet's certificate before connecting
Classification:complianceFramework:cis-kubernetesControl:1.2.6
## Description{% #description %}

Verify kubelet's certificate before establishing connection.

## Rationale{% #rationale %}

The connections from the apiserver to the kubelet are used for fetching logs for pods, attaching (through kubectl) to running pods, and using the kubelets port-forwarding functionality. These connections terminate at the kubelets HTTPS endpoint. By default, the apiserver does not verify the kubelets serving certificate, which makes the connection subject to man-in-the-middle attacks, and unsafe to run over untrusted and/or public networks.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--kubelet-certificate-authority` argument exists and is set as appropriate.

## Remediation{% #remediation %}

Follow the Kubernetes documentation and setup the TLS connection between the apiserver and kubelets. Then, edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--kubelet-certificate-authority` parameter to the path to the cert file for the certificate authority.

```
--kubelet-certificate-authority=<ca-string>
```

## Impact{% #impact %}

You require TLS to be configured on apiserver as well as kubelets.

## Default value{% #default-value %}

By default, `--kubelet-certificate-authority` argument is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://kubernetes.io/docs/admin/kubelet-authentication-authorization/](https://kubernetes.io/docs/admin/kubelet-authentication-authorization/)
1. [https://kubernetes.io/docs/concepts/cluster-administration/master-node-communication/#apiserver---kubelet](https://kubernetes.io/docs/concepts/cluster-administration/master-node-communication/#apiserver---kubelet)

## CIS controls{% #cis-controls %}

Version 6.3.4 Use Only Secure Channels For Remote System Administration - Perform all remote administration of servers, workstation, network devices, and similar equipment over secure channels. Protocols such as telnet, VNC, RDP, or others that do not actively support strong encryption should only be used if they are performed over a secondary encryption channel, such as SSL, TLS or IPSEC.

Version 7.4.5 Use Multifactor Authentication For All Administrative Access - Use multi-factor authentication and encrypted channels for all administrative account access.
