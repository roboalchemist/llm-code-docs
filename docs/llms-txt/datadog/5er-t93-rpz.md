# Source: https://docs.datadoghq.com/security/default_rules/5er-t93-rpz.md

---
title: The secure port should not be disabled for the API server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The secure port should not be disabled
  for the API server
---

# The secure port should not be disabled for the API server
Classification:complianceFramework:cis-kubernetesControl:1.2.20
## Description{% #description %}

Do not disable the secure port.

## Rationale{% #rationale %}

The secure port is used to serve https with authentication and authorization. If you disable it, no https traffic is served and all traffic is served unencrypted.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--secure-port` argument is either not set or is set to an integer value between `1` and `65535`.

## Remediation{% #remediation %}

Edit the API server pod specification file /etc/kubernetes/manifests/kube-apiserver.yaml on the master node and either remove the âsecure-port parameter or set it to a different (non-zero) desired port.

## Impact{% #impact %}

You need to set the API Server up with the right TLS certificates.

## Default value{% #default-value %}

By default, port 6443 is used as the secure port.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)

## CIS controls{% #cis-controls %}

Version 6 14.2 Encrypt All Sensitive Information Over Less-trusted Networks All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted. Version 7 14.4 Encrypt All Sensitive Information in Transit Encrypt all sensitive information in transit.
