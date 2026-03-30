# Source: https://docs.datadoghq.com/security/default_rules/zqy-4jm-w98.md

---
title: The API server should only bind to secure, known ports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API server should only bind to
  secure, known ports
---

# The API server should only bind to secure, known ports
Classification:complianceFramework:cis-kubernetesControl:1.2.19
## Description{% #description %}

Do not bind to insecure port.

## Rationale{% #rationale %}

Setting up the apiserver to serve on an insecure port would allow unauthenticated and unencrypted access to your master node. This would allow attackers who could access this port, to easily take control of the cluster.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--insecure-port` argument is set to `0`.

## Remediation{% #remediation %}

Edit the API server pod specification file /etc/kubernetes/manifests/kube-apiserver.yaml on the master node and set the below parameter. âinsecure-port=0

## Impact{% #impact %}

All components that use the API must connect via the secured port, authenticate themselves, and be authorized to use the API. This includes: kube-controller-manager kube-proxy kube-scheduler kubelets

## Default value{% #default-value %}

By default, the insecure port is set to 8080.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)

## CIS controls{% #cis-controls %}

Version 6 9.1 Limit Open Ports, Protocols, and Services Ensure that only ports, protocols, and services with validated business needs are running on each system. Version 7 9.2 Ensure Only Approved Ports, Protocols and Services Are Running Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.
