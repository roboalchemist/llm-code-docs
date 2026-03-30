# Source: https://docs.datadoghq.com/security/default_rules/pv9-m3h-8wy.md

---
title: Profiling for API server should be disabled, if not needed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Profiling for API server should be
  disabled, if not needed
---

# Profiling for API server should be disabled, if not needed
Classification:complianceFramework:cis-kubernetesControl:1.2.21
## Description{% #description %}

Disable profiling, if not needed.

## Rationale{% #rationale %}

Profiling allows for the identification of specific performance bottlenecks. It generates a significant amount of program data that could potentially be exploited to uncover system and program details. If you are not experiencing any bottlenecks and do not need the profiler for troubleshooting purposes, it is recommended to turn it off to reduce the potential attack surface.

## Audit{% #audit %}

Run the following command on the master node:

```
ps -ef | grep kube-apiserver
```

Verify that the `--profiling` argument is set to `false`.

## Remediation{% #remediation %}

Edit the API server pod specification file /etc/kubernetes/manifests/kube-apiserver.yaml on the master node and set the below parameter. âprofiling=false

## Impact{% #impact %}

Profiling information would not be available.

## Default value{% #default-value %}

By default, profiling is enabled.

## References{% #references %}

1. [https://kubernetes.io/docs/admin/kube-apiserver/](https://kubernetes.io/docs/admin/kube-apiserver/) 2. [https://github.com/kubernetes/community/blob/master/contributors/devel/profiling.md](https://github.com/kubernetes/community/blob/master/contributors/devel/profiling.md)

## CIS controls{% #cis-controls %}

Version 6 14 Controlled Access Based on the Need to Know Controlled Access Based on the Need to Know Version 7 14 Controlled Access Based on the Need to Know Controlled Access Based on the Need to Know
