# Source: https://docs.datadoghq.com/security/default_rules/def-000-3fk.md

---
title: Asana role change to admin or super-admin detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Asana role change to admin or
  super-admin detected
---

# Asana role change to admin or super-admin detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Identify role changes to admin or super-admin, as these could indicate privilege escalation attempts or improper access assignments.

## Strategy{% #strategy %}

This rule monitors log events specifically for changes where roles are elevated to admin or super-admin. It aims to detect unauthorized access or misconfigurations that could impact system security.

## Triage and response{% #triage-and-response %}

1. Examine the logs to identify the user `{{@usr.email}}` whose role was changed to admin or super-admin and determine the initiator of the change `{{@resource.email}}`.
1. Confirm if the role change was expected or authorized by consulting relevant stakeholders or referring to change management records.
1. Analyze whether the user or initiator has recently engaged in unusual or high-risk activities, which could indicate a compromised account or intentional misuse.
1. If the role change is unauthorized, consider reverting the role, notifying affected parties, and initiating a security review.
