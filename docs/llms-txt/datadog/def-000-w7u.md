# Source: https://docs.datadoghq.com/security/default_rules/def-000-w7u.md

---
title: Clusters should use binary authorization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Clusters should use binary
  authorization
---

# Clusters should use binary authorization
 
## Description{% #description %}

Enable Binary Authorization on the cluster. This ensures that only signed images are allowed inside the cluster, increasing the supply-chain security of your clusters.

## Remediation{% #remediation %}

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list).
1. Select the cluster.
1. Under the `details` pane, within the `Security` section, ensure that `Binary Authorization` is set to `Enabled`.
1. Click `SAVE`.
1. Go to [Binary Authorization](https://console.cloud.google.com/security/binary-authorization).
1. Check that there is a policy defined and it does not specify `Allow all images`.

## References{% #references %}
