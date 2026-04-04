# Source: https://docs.datadoghq.com/security/default_rules/def-00k-8wy.md

---
title: Kubernetes API server profiling should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubernetes API server profiling should
  be disabled
---

# Kubernetes API server profiling should be disabled

## Description{% #description %}

Kubernetes API server profiling should be disabled if not required. Profiling allows for the identification of specific performance bottlenecks, and generates a significant amount of program data that could potentially be exploited to uncover system and program details. If you are not experiencing any bottlenecks and do not need the profiler for troubleshooting purposes, it is recommended to turn it off to reduce the potential attack surface.

## Remediation{% #remediation %}

Edit the API server pod specification file `/etc/kubernetes/manifests/kube-apiserver.yaml` on the master node and set the parameter `--profiling=false`.
