# Source: https://docs.datadoghq.com/security/default_rules/h4p-ch8-wwd.md

---
title: Kubelet connections should use HTTPS for enhanced security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubelet connections should use HTTPS
  for enhanced security
---

# Kubelet connections should use HTTPS for enhanced security
Classification:complianceFramework:cis-kubernetesControl:1.2.4 
## Description{% #description %}

Use https for kubelet connections.

## Rationale{% #rationale %}

Connections from apiserver to kubelets could potentially carry sensitive data such as secrets and keys. It is thus important to use in-transit encryption for any communication between the apiserver and kubelets.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--kubelet-https` argument either does not exist or is set to `true`.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and remove the `--kubelet-https` parameter.

## Impact{% #impact %}

You require TLS to be configured on apiserver as well as kubelets.

## Default value{% #default-value %}

By default, kubelet connections are over https.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://kubernetes.io/docs/admin/kubelet-authentication-authorization/](https://kubernetes.io/docs/admin/kubelet-authentication-authorization/)

## CIS controls{% #cis-controls %}

Version 6 14.2 Encrypt All Sensitive Information Over Less-trusted Networks All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted.

Version 7 14.4 Encrypt All Sensitive Information in Transit Encrypt all sensitive information in transit.
