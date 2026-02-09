# Source: https://docs.datadoghq.com/security/default_rules/def-00k-sku.md

---
title: The Controller Manager profiling should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Controller Manager profiling should
  be disabled
---

# The Controller Manager profiling should be disabled
 
## Description{% #description %}

Controller manager profiling should be disabled if not required. Profiling allows for the identification of specific performance bottlenecks, and generates a significant amount of program data that could potentially be exploited to uncover system and program details. If you are not experiencing any bottlenecks and do not need the profiler for troubleshooting purposes, it is recommended to turn it off to reduce the potential attack surface.

## Remediation{% #remediation %}

Edit the Controller Manager pod specification file `/etc/kubernetes/manifests/kube-controller-manager.yaml` on the master node and set the following parameter:

```
--profiling=false
```
