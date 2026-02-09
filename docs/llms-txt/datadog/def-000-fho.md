# Source: https://docs.datadoghq.com/security/default_rules/def-000-fho.md

---
title: Legacy authorization (ABAC) should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Legacy authorization (ABAC) should be
  disabled
---

# Legacy authorization (ABAC) should be disabled
 
## Description{% #description %}

Legacy Authorization, also known as Attribute-Based Access Control (ABAC) has been superseded by Role-Based Access Control (RBAC) and is not under active development. [RBAC](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) is the recommended way to manage permissions in Kubernetes.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)
1. Select Kubernetes clusters for which Legacy Authorization is enabled
1. Click `EDIT`
1. Set `Legacy Authorization` to `Disabled`
1. Click `SAVE`.

### From the commandline{% #from-the-commandline %}

1. To disable Legacy Authorization for an existing cluster, run the following command:
   ```
   gcloud container clusters update <cluster_name> --zone <compute_zone> --no-
   enable-legacy-authorization
   ```

## References{% #references %}
