# Source: https://docs.datadoghq.com/security/default_rules/pgl-8ie-264.md

---
title: Google Cloud Service Account accessing anomalous number of Google Cloud APIs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud Service Account accessing
  anomalous number of Google Cloud APIs
---

# Google Cloud Service Account accessing anomalous number of Google Cloud APIs
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580) 
## Goal{% #goal %}

Detect when a Google Cloud service account is compromised.

## Strategy{% #strategy %}

Inspect the Google Cloud admin activity logs (`@data.logName:*%2Factivity`) and filter for only Google Cloud service accounts (`@usr.id:*.iam.gserviceaccount.com`). Count the unique number of Google Cloud API calls (`@evt.name`) which are being made for each service account (`@usr.id`). The anomaly detection baselines each service account and then generates a security signal when a service account deviates from their baseline.

To read more about Google Cloud audit logs, read the [blog post](https://www.datadoghq.com/blog/monitoring-gcp-audit-logs/).

## Triage and response{% #triage-and-response %}

Investigate the logs and determine whether or not the Google Cloud service account is compromised.

## Changelog{% #changelog %}

- 17 October 2022 - Updated tags.
