# Source: https://docs.datadoghq.com/security/default_rules/def-000-h8d.md

---
title: >-
  PingFederate Admin Alert: multiple login attempts by locked account in a short
  time period
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PingFederate Admin Alert: multiple
  login attempts by locked account in a short time period
---

# PingFederate Admin Alert: multiple login attempts by locked account in a short time period

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect an unusually high number of login attempts by locked account.

## Strategy{% #strategy %}

Monitor PingFederate logs where a user generates a high number of login attempts by a locked account within a short period. This detection rule aims to identify potential threats early, allowing for timely investigation and mitigation to protect server resources and maintain service availability.

## Triage and response{% #triage-and-response %}

1. Analyze the pattern and volume of requests to distinguish between legitimate traffic and potential attacks.
1. Investigate the source user `{{@usr.name}}` to determine if the activity is malicious.
1. Implement immediate measures to block or limit the impact of the suspicious activity if confirmed as a threat.
