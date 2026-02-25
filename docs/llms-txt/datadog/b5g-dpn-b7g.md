# Source: https://docs.datadoghq.com/security/default_rules/b5g-dpn-b7g.md

---
title: The API server should validate the service account token in etcd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The API server should validate the
  service account token in etcd
---

# The API server should validate the service account token in etcd
Classification:complianceFramework:cis-kubernetesControl:1.2.27
## Description{% #description %}

Validate service account before validating token.

## Rationale{% #rationale %}

If âservice-account-lookup is not enabled, the apiserver only verifies that the authentication token is valid, and does not validate that the service account token mentioned in the request is actually present in etcd. This allows using a service account token even after the corresponding service account is deleted. This is an example of time of check to time of use security issue.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that if the `--service-account-lookup` argument exists it is set to `true`.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the below parameter. `--service-account-lookup=true` Alternatively, you can delete the `--service-account-lookup` parameter from this file so that the default takes effect.

## Impact{% #impact %}

None

## Default value{% #default-value %}

By default, `--service-account-lookup` argument is set to true.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/)
1. [https://github.com/kubernetes/kubernetes/issues/24167](https://github.com/kubernetes/kubernetes/issues/24167)
1. [https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use](https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use)

## CIS controls{% #cis-controls %}

Version 6 16 Account Monitoring and Control Account Monitoring and Control Version 7 16 Account Monitoring and Control Account Monitoring and Control
