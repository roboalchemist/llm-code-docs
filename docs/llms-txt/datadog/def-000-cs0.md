# Source: https://docs.datadoghq.com/security/default_rules/def-000-cs0.md

---
title: The Web UI Dashboard should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > The Web UI Dashboard should be disabled
---

# The Web UI Dashboard should be disabled

## Description{% #description %}

The Web UI dashboard should be disabled since it is historically a good source of vulnerabilities for a cluster.

**Note:** The Kubernetes web UI (Dashboard) does not have admin access by default in GKE 1.7 and higher. The Kubernetes web UI is disabled by default in GKE 1.10 and higher. In GKE 1.15 and higher, the Kubernetes web UI add-on KubernetesDashboard is no longer supported as a managed add-on.

## Remediation{% #remediation %}

### From the commandline{% #from-the-commandline %}

1. To disable the Kubernetes Dashboard on an existing cluster, run the following command:

   ```
   gcloud container clusters update <cluster_name> --zone <zone> --update-
   addons=KubernetesDashboard=DISABLED
   ```
