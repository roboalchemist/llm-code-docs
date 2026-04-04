# Source: https://docs.datadoghq.com/security/default_rules/f68-e1e-db8.md

---
title: Google Cloud Pub/Sub topic deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Google Cloud Pub/Sub topic deleted
---

# Google Cloud Pub/Sub topic deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect deletion of Google Cloud Pub/Sub subscriptions, which can stop audit logs from being sent to Datadog.

## Strategy{% #strategy %}

Monitor Google Cloud admin activity audit logs to determine when the following method is invoked:

- `google.pubsub.v1.Publisher.DeleteTopic`

## Triage and response{% #triage-and-response %}

Review the subscription and ensure it is properly configured.
