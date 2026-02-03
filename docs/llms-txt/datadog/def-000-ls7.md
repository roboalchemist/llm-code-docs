# Source: https://docs.datadoghq.com/security/default_rules/def-000-ls7.md

---
title: Windows password change on directory service restore account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows password change on directory
  service restore account
---

# Windows password change on directory service restore account

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects password changes to the Directory Service Restore Mode (DSRM) account.

## Strategy{% #strategy %}

This rule monitors for Windows event ID `4794`, which is generated when the password of the DSRM account is changed. The DSRM account is a built-in local administrator account on domain controllers that's used for recovery operations when Active Directory is not functioning properly.

The DSRM account has complete access to the Active Directory database and can be used to modify or extract sensitive directory information when booted into recovery mode. Because of its powerful capabilities, password changes for this account should be infrequent and strictly controlled.

Password changes to the DSRM account outside of documented maintenance windows are suspicious. Attackers who gain administrative access to a domain controller may modify the DSRM password to establish persistence that survives domain credential resets. This technique allows an attacker to regain control of a domain controller even after remediation efforts.

## Triage & Response{% #triage--response %}

- Verify which administrator account initiated the DSRM password change on `{{host}}`.
- Determine if the password change was part of scheduled maintenance or an approved administrative task.
- Check the authentication logs for the admin account that performed the change to verify it wasn't compromised.
- Review other administrative actions taken by the same account around the time of the password change.
- Examine domain controller security logs for additional suspicious activities.
- Verify no unauthorized access to the DSRM account occurred following the password change.
- Document the current DSRM password and reset it.
- Reset credentials for any potentially compromised administrative accounts.
