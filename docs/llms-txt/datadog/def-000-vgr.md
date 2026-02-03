# Source: https://docs.datadoghq.com/security/default_rules/def-000-vgr.md

---
title: Keycloak user disabled by permanent lockout
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Keycloak user disabled by permanent
  lockout
---

# Keycloak user disabled by permanent lockout

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detects when there is an event regarding a user disabled by permanent lockout.

## Strategy{% #strategy %}

This rule monitors logs to identify users disabled by permanent lockout events.

## Triage and Response{% #triage-and-response %}

1. Determine the cause of the permanent lockout for the user: `{{@usr.id}}`(UserId) and from the source: `{{@network.client.ip}}`.
1. Notify the user about the permanent lockout and clarify whether it was triggered by their actions.
1. If the user did not initiate any activity leading to the lockout, consider blocking the source of those events.
