# Source: https://docs.datadoghq.com/security/default_rules/def-000-gfb.md

---
title: Windows active directory replication from non machine account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows active directory replication
  from non machine account
---

# Windows active directory replication from non machine account

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detects an instance where a non-machine account is attempting to perform Active Directory (AD) replication.

## Strategy{% #strategy %}

This detection monitors Windows Security event logs for occurrences of Event ID 4662 (An operation was performed on an object) with specific Access Mask and Properties values that indicate directory replication attempts. The detection looks for access mask `0x100` (Control Access) and targeted directory service replication GUIDs. The detection excludes normal machine accounts (which end with '$') and Microsoft Online accounts (starting with 'MSOL_') as these are legitimate service accounts expected to perform replication.

DCSync is a technique commonly used in identity-based attacks where an adversary with sufficient privileges requests account data from a domain controller using the AD replication protocol.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` domain controller that recorded the AD replication event.
- Examine the account that performed the replication by reviewing the `SubjectUserName` field in the event data.
- Validate whether the account has legitimate permissions to perform AD replication operations.
- Review authentication logs for the account in question, looking for suspicious logon events around the same time period.
- Check for surrounding suspicious events such as Event ID 4625 (Failed Logon) or Event ID 4648 (Logon with Explicit Credentials).
- Look for LSASS memory access events indicating credential theft attempts.
- Review any PowerShell execution events around the same time frame that might indicate credential dumping scripts.
- Determine if the account was recently added to privileged groups or given specific replication permissions.
- If unauthorized, disable the account immediately and force a password reset for affected domain accounts.
- Remove any unauthorized replication permissions from the account.
