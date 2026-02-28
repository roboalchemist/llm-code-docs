# Source: https://docs.datadoghq.com/security/default_rules/def-000-ro8.md

---
title: Cluster VPC flow logs and intranode visibility should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cluster VPC flow logs and intranode
  visibility should be enabled
---

# Cluster VPC flow logs and intranode visibility should be enabled

## Description{% #description %}

VPC Flow Logs and intranode visibility should be enabled. This allows monitoring and analysis of network traffic within your GKE cluster.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list).
1. Select Kubernetes clusters for which intranode visibility is disabled.
1. Within the **Details** pane, under the **Network** section, click on the pencil icon named **Edit intranode visibility**.
1. Check the box next to **Enable Intranode visibility**.
1. Click **SAVE CHANGES**.

### From the command line{% #from-the-command-line %}

1. To enable intranode visibility, run the following command:
   ```
   gcloud container clusters update <cluster_name> --enable-intra-node-visibility
   ```

## References{% #references %}
