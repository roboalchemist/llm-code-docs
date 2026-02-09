# Source: https://docs.datadoghq.com/security/default_rules/bk7-jyi-j6m.md

---
title: Kubelet authentication should require certificate-based authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet authentication should require
  certificate-based authentication
---

# Kubelet authentication should require certificate-based authentication
Classification:complianceFramework:cis-kubernetesControl:1.2.5 
## Description{% #description %}

Enable certificate based kubelet authentication.

## Rationale{% #rationale %}

The apiserver, by default, does not authenticate itself to the kubelet's HTTPS endpoints. The requests from the apiserver are treated anonymously. You should set up certificate-based kubelet authentication to ensure that the apiserver authenticates itself to kubelets when submitting requests.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--kubelet-client-certificate` and `--kubelet-client-key` arguments exist and they are set as appropriate.

## Remediation{% #remediation %}

Follow the Kubernetes documentation and set up the TLS connection between the apiserver and kubelets. Then, edit API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the kubelet client certificate and key parameters as below.

```
--kubelet-client-certificate=<path/to/client-certificate-file> 
--kubelet-client-key=<path/to/client-key-file>
```

## Impact{% #impact %}

You require TLS to be configured on apiserver as well as kubelets.

## Default value{% #default-value %}

By default, certificate-based kubelet authentication is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://kubernetes.io/docs/admin/kubelet-authentication-authorization/](https://kubernetes.io/docs/admin/kubelet-authentication-authorization/)
1. [https://kubernetes.io/docs/concepts/cluster-administration/master-node-communication/#apiserverâkubelet](https://kubernetes.io/docs/concepts/cluster-administration/master-node-communication/#apiserver---kubelet)

## CIS controls{% #cis-controls %}

Version 6.3.4 Use Only Secure Channels For Remote System Administration - Perform all remote administration of servers, workstation, network devices, and similar equipment over secure channels. Protocols such as telnet, VNC, RDP, or others that do not actively support strong encryption should only be used if they are performed over a secondary encryption channel, such as SSL, TLS or IPSEC.

Version 7.4.5 Use Multifactor Authentication For All Administrative Access - Use multi-factor authentication and encrypted channels for all administrative account access.
