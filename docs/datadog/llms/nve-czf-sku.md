# Source: https://docs.datadoghq.com/security/default_rules/nve-czf-sku.md

---
title: Controller Manager profiling should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Controller Manager profiling should be
  disabled
---

# Controller Manager profiling should be disabled
Classification:complianceFramework:cis-kubernetesControl:1.3.2
## Description{% #description %}

Disable profiling, if not needed.

## Rationale{% #rationale %}

Profiling allows for the identification of specific performance bottlenecks. It generates a significant amount of program data that could potentially be exploited to uncover system and program details. If you are not experiencing any bottlenecks and do not need the profiler for troubleshooting purposes, it is recommended to turn it off to reduce the potential attack surface.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-controller-manager
```

Verify that the `--profiling` argument is set to `false`.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and set the below parameter:

```
--profiling=false
```

## Impact{% #impact %}

Profiling information would not be available.

## Default value{% #default-value %}

By default, profiling is enabled.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-controller-manager/](https://kubernetes.io/docs/admin/kube-controller-manager/)
1. [https://github.com/kubernetes/community/blob/master/contributors/devel/profiling.md](https://github.com/kubernetes/community/blob/master/contributors/devel/profiling.md)

## CIS controls{% #cis-controls %}

Version 6.14 Controlled Access Based on the Need to Know

Version 7.4 Controlled Use of Administrative Privileges
