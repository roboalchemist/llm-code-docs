# Source: https://docs.datadoghq.com/security/default_rules/def-000-bts.md

---
title: Windows active directory privileged users or groups reconnaissance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows active directory privileged
  users or groups reconnaissance
---

# Windows active directory privileged users or groups reconnaissance

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1087-account-discovery](https://attack.mitre.org/techniques/T1087) 
## Goal{% #goal %}

Detects reconnaissance activity targeting privileged Active Directory user accounts and groups. Alerts when multiple distinct privileged objects are accessed by a single user.

## Strategy{% #strategy %}

This rule monitors Windows Security Audit events, where `@evt.id` is `4661` for handle-to-object operations targeting Security Accounts Manager (SAM) user or group objects. The detection focuses on access attempts to well-known privileged group security identifiers (SIDs), including Domain Admins (-512), Guest (-501), Administrator (-500), Print Operators (-550), Enterprise Admins (-519), Schema Admins (-518), Domain Controllers (-516), and objects containing "admin" in their names. This pattern indicates potential reconnaissance activity where attackers enumerate privileged accounts to identify high-value targets for lateral movement or privilege escalation.

## Triage and response{% #triage-and-response %}

- Examine the specific privileged objects accessed by `{{@Event.EventData.Data.SubjectUserName}}` on `{{host}}` to understand the scope of the reconnaissance activity.
- Review the user's legitimate business role and determine if they have authorized reasons to access multiple privileged Active Directory objects.
- Check for subsequent authentication attempts or privilege escalation activities from the same user account following this reconnaissance.
- Analyze the timing and pattern of object access to distinguish between automated tools versus manual enumeration.
- Investigate whether the user account may have been compromised by reviewing recent authentication logs and unusual activity patterns.
