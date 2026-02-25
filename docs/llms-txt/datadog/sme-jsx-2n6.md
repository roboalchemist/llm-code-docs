# Source: https://docs.datadoghq.com/security/default_rules/sme-jsx-2n6.md

---
title: API server should only authorize explicitly authorized requests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > API server should only authorize
  explicitly authorized requests
---

# API server should only authorize explicitly authorized requests
Classification:complianceFramework:cis-kubernetesControl:1.2.7
## Description{% #description %}

Do not always authorize all requests.

## Rationale{% #rationale %}

The API Server, can be configured to allow all requests. This mode should not be used on any production cluster.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--authorization-mode` argument exists and is not set to `AlwaysAllow`.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the `--authorization-mode` parameter to values other than `AlwaysAllow`. One such example could be as below:

```
--authorization-mode=RBAC
```

## Impact{% #impact %}

Only authorized requests will be served.

## Default value{% #default-value %}

By default, `AlwaysAllow` is not enabled.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://kubernetes.io/docs/admin/authorization/node/](https://kubernetes.io/docs/admin/authorization/node/)

## CIS controls{% #cis-controls %}

Version 6.9.1 Limit Open Ports, Protocols, and Services - Ensure that only ports, protocols, and services with validated business needs are running on each system.

Version 7.9.2 Ensure Only Approved Ports, Protocols and Services Are Running - Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.
