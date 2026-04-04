# Source: https://docs.datadoghq.com/security/default_rules/def-000-vn6.md

---
title: Windows active directory user backdoors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows active directory user backdoors
---

# Windows active directory user backdoors

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detects Active Directory user account backdoor configurations through delegation settings and LDAP attribute modifications.

## Strategy{% #strategy %}

This rule monitors Active Directory user account modifications related to delegation permissions and service principal names. The detection tracks user account modifications through event ID `4738` when delegation permissions are modified, and event ID `5136` for LDAP attribute changes including `msDS-AllowedToDelegateTo`, `msDS-AllowedToActOnBehalfOfOtherIdentity`, and `servicePrincipalName` attributes. These modifications can enable unauthorized access and impersonation capabilities within the Active Directory environment.

## Triage & Response{% #triage--response %}

- Examine the modified user account properties and determine if the delegation permissions were authorized by reviewing the `{{@usr.id}}` making the changes.
- Validate if the service principal name changes on the affected user accounts align with legitimate business requirements.
- Review the delegation targets specified in `AllowedToDelegateTo` attributes to ensure they are authorized services.
- Analyze authentication patterns for the modified accounts to identify any suspicious delegation or impersonation activity.
- Restrict delegation permissions to only necessary service accounts.
