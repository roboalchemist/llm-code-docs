# Source: https://docs.datadoghq.com/security/default_rules/def-000-gcu.md

---
title: Trellix Endpoint Security suspicious call was detected and blocked
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Trellix Endpoint Security suspicious
  call was detected and blocked
---

# Trellix Endpoint Security suspicious call was detected and blocked

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detect suspicious system calls or communications that were blocked by Trellix Endpoint Security, which may indicate malicious activity.

## Strategy{% #strategy %}

Monitor for blocked suspicious calls, such as unauthorized API calls, system modifications, or external communications. These events could signal potential malware or unauthorized software attempting to interact with the system or network.

## Triage and Response{% #triage-and-response %}

1. Confirm the details of the blocked suspicious call, including the originating process or user.
1. Review the event details to determine the nature of the suspicious call, such as whether it was an external communication or a system modification attempt.
1. Investigate the endpoint involved by analyzing its hostname - `{{@attributes.analyzerhostname}}` and IP address - `{{@attributes.analyzeripv4}}`.
1. If the suspicious activity is confirmed as a potential threat, take immediate steps to isolate the endpoint and perform a deeper investigation into the process or user responsible for the activity.
1. Review and strengthen security policies to ensure further calls of this type are blocked and investigate whether similar suspicious calls have occurred on other systems
