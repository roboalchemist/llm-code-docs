# Source: https://docs.datadoghq.com/security/default_rules/def-000-xgm.md

---
title: Zendesk IP restriction settings is disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Zendesk IP restriction settings is
  disabled
---

# Zendesk IP restriction settings is disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when IP restriction is disabled.

## Strategy{% #strategy %}

Monitor Zendesk audit logs to look for events with an `@source_label` value of `"Security: Enable IP restrictions"` and `message:"Turned off"`. IP restriction allows administrators to limit access to Zendesk to users within a certain range of IP addresses only.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` intended to disable IP restriction.
1. If there is not a legitimate business use case, reset the IP restrictions to the original configuration.
