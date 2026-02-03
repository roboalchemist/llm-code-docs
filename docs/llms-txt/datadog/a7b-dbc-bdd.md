# Source: https://docs.datadoghq.com/security/default_rules/a7b-dbc-bdd.md

---
title: Google Cloud Pub/Sub Subscriber modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud Pub/Sub Subscriber
  modified
---

# Google Cloud Pub/Sub Subscriber modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect changes to Google Cloud Pub/Sub subscriptions, which can stop audit logs from being sent to Datadog.

## Strategy{% #strategy %}

Monitor Google Cloud admin activity audit logs to determine when any of the following methods are invoked:

- `google.pubsub.v1.Subscriber.UpdateSubscription`
- `google.pubsub.v1.Subscriber.DeleteSubscription`

## Triage and response{% #triage-and-response %}

Review the subscription and ensure it is properly configured.
