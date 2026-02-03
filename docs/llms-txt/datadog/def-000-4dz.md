# Source: https://docs.datadoghq.com/security/default_rules/def-000-4dz.md

---
title: PingOne multiple Kerberos check failed attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PingOne multiple Kerberos check failed
  attempts
---

# PingOne multiple Kerberos check failed attempts

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTechnique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect when an unusually high number of Kerberos check failed attempts are made from a single user.

## Strategy{% #strategy %}

Monitor PingOne logs where a user generates a high number of requests within a short period. This detection rule aims to identify potential threats early, allowing for timely investigation and mitigation to protect server resources and maintain service availability.

## Triage and response{% #triage-and-response %}

1. Analyze the pattern and volume of requests to distinguish between legitimate traffic and potential attacks.
1. Investigate the source user `{{@resources.name}}` to determine if the activity is malicious.
1. Implement immediate measures to block or limit the impact of the suspicious activity if confirmed as a threat.
