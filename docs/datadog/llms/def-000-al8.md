# Source: https://docs.datadoghq.com/security/default_rules/def-000-al8.md

---
title: Google Cloud exposed service account key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud exposed service account
  key
---

# Google Cloud exposed service account key
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552)
## Goal{% #goal %}

Detect when Google Cloud disables a key for being exposed.

## Strategy{% #strategy %}

This rule monitors Cloud Audit Logs and detects when the principal [gcp-compromised-key-response@system.gserviceaccount.com](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable-exposed-keys) disabled a key. If Google Cloud detects an exposed key, it automatically disables the key.

## Triage and response{% #triage-and-response %}

1. An abuse event is created in the [Abuse Event logs](https://cloud.google.com/logging/docs/api/platform-logs#abuse_event).
1. Investigate any other actions carried out by the compromised identity `{{@data.protoPayload.request.name}}` using the Cloud SIEM investigator.
