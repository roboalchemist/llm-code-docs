# Source: https://docs.datadoghq.com/security/default_rules/def-000-d5h.md

---
title: Keycloak high number of error events from a realm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Keycloak high number of error events
  from a realm
---

# Keycloak high number of error events from a realm

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
## Goal{% #goal %}

Detects when there is a high number of error events from a realm. A realm in Keycloak is an isolated space where users, apps, roles, and groups are managed.

## Strategy{% #strategy %}

This rule monitors logs for a high number of error events from a realm.

## Triage and Response{% #triage-and-response %}

1. Investigate the error event logs recorded for the system: `{{@syslog.hostname}}` and within the realm: `{{@realmName}}`.
1. Examine the source and types of the detected error events.
1. Determine whether the errors are originating from a specific user or client.
1. Analyze if the errors are of a particular type to assess whether they indicate an attack or a misconfiguration issue.
1. If the events are confirmed as an attack, take action to block the source to prevent further incidents.
1. Notify affected users about the errors and advise them to take protective measures, such as changing their passwords if suspicious activity is confirmed.
1. Consider conducting a thorough review of security configurations within the realm to identify any vulnerabilities.
