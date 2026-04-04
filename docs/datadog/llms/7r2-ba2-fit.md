# Source: https://docs.datadoghq.com/security/default_rules/7r2-ba2-fit.md

---
title: The insecure API service should not be bound
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The insecure API service should not be
  bound
---

# The insecure API service should not be bound
Classification:complianceFramework:cis-kubernetesControl:1.2.18
## Description{% #description %}

Do not bind the insecure API service.

## Rationale{% #rationale %}

If you bind the apiserver to an insecure address, basically anyone who could connect to it over the insecure port, would have unauthenticated and unencrypted access to your master node. The apiserver doesn't do any authentication checking for insecure binds and traffic to the Insecure API port is not encrpyted, allowing attackers to potentially read sensitive data in transit.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--insecure-bind-address` argument does not exist.

## Remediation{% #remediation %}

Edit the API server pod specification file /etc/kubernetes/manifests/kube-apiserver.yaml on the master node and remove the âinsecure-bind-address parameter.

## Impact{% #impact %}

Connections to the API server will require valid authentication credentials.

## Default value{% #default-value %}

By default, the insecure bind address is not set.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)

## CIS controls{% #cis-controls %}

Version 6 9.1 Limit Open Ports, Protocols, and Services Ensure that only ports, protocols, and services with validated business needs are running on each system. Version 7 9.2 Ensure Only Approved Ports, Protocols and Services Are Running Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.
