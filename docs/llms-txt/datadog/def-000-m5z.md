# Source: https://docs.datadoghq.com/security/default_rules/def-000-m5z.md

---
title: '''Regular'' or ''Stable'' release channels should be used for GKE clusters'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Regular' or 'Stable' release channels
  should be used for GKE clusters
---

# 'Regular' or 'Stable' release channels should be used for GKE clusters
 
## Description{% #description %}

Release channels should be used to automate version upgrades and reduce potential difficulties associated with version management. To prevent outages, a [maintenance window](https://cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) should be set up as well.

## Remediation{% #remediation %}

Follow the steps from Google Cloud and [Enable Release Channels](https://cloud.google.com/kubernetes-engine/docs/how-to/release-channels).
