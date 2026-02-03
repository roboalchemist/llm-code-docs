# Source: https://docs.datadoghq.com/security/default_rules/def-000-be3.md

---
title: An AKS Cluster's Kubelet should not allow hostname overrides
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An AKS Cluster's Kubelet should not
  allow hostname overrides
---

# An AKS Cluster's Kubelet should not allow hostname overrides
 
## Description{% #description %}

Hostnames in the cluster should not be overriden. This could potentially break the TLS setup between Kubelet and the API server. You should set up your kubelet nodes with resolvable FQDNs and avoid overriding the hostnames with IPs.

## Remediation{% #remediation %}

1. Edit the kubelet service file on each worker node and remove the following parameters are part of the `KUBELET_ARGS` variable string.

```bash
--hostname-override=<any-string>
```
