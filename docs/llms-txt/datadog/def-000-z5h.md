# Source: https://docs.datadoghq.com/security/default_rules/def-000-z5h.md

---
title: Keycloak multiple identity provider login errors detected on realm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Keycloak multiple identity provider
  login errors detected on realm
---

# Keycloak multiple identity provider login errors detected on realm

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detects when there are multiple identity provider login errors from a realm. A realm in Keycloak is an isolated space where users, apps, roles, and groups are managed.

## Strategy{% #strategy %}

This rule monitors logs for multiple identity provider login error events from a realm.

## Triage and Response{% #triage-and-response %}

1. Review the identity provider login error event logs detected for the system: `{{@syslog.hostname}}` and within the realm: `{{@realmName}}`.
1. Investigate the source of the identity provider login error events.
1. Analyze the patterns in the identity provider login error events to determine if there are signs of brute force attacks.
1. Identify the specific identity providers associated with the login error events.
1. Consider temporarily suspending affected accounts until user verification is completed.
1. Notify the impacted users about login error events and advise them to update their passwords.
