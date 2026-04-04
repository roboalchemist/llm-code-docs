# Source: https://docs.datadoghq.com/security/default_rules/def-000-7vv.md

---
title: Trellix Endpoint Security tampering with exploit prevention has been detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trellix Endpoint Security tampering
  with exploit prevention has been detected
---

# Trellix Endpoint Security tampering with exploit prevention has been detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Identify attempts to tamper with exploit prevention mechanisms as detected by Trellix Endpoint Security, indicating potential malicious activity.

## Strategy{% #strategy %}

Monitor for events related to tampering with exploit prevention settings. Such activities may indicate an attempt to disable or circumvent security measures designed to protect against exploitation.

## Triage and Response{% #triage-and-response %}

1. Review the details of the tampering event, including the user or process involved.
1. Analyze the event data to determine the nature and extent of the tampering.
1. Investigate the impacted endpoint using its hostname - `{{@attributes.analyzerhostname}}` and IP address - `{{@attributes.analyzeripv4}}`.
1. If tampering is confirmed, take immediate action to restore protection settings and mitigate potential security risks.
1. Strengthen security configurations and monitor for further tampering attempts.
