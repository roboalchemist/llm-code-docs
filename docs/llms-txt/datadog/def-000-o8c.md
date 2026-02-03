# Source: https://docs.datadoghq.com/security/default_rules/def-000-o8c.md

---
title: PingOne user locked after too many failed attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PingOne user locked after too many
  failed attempts
---

# PingOne user locked after too many failed attempts

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTechnique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect a user locked by PingOne.

## Strategy{% #strategy %}

Monitor PingOne logs where a user will be automatically locked after too many failed authentication attempts for that specific device.

## Triage and response{% #triage-and-response %}

1. Analyze the pattern and volume of requests to distinguish between legitimate traffic and potential attacks.
1. Investigate the source user `{{@resources.name}}` to determine if locked user's activities are suspicious.
