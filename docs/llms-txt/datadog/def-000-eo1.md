# Source: https://docs.datadoghq.com/security/default_rules/def-000-eo1.md

---
title: Azure AD MFA disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure AD MFA disabled
---

# Azure AD MFA disabled
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556)
## Goal{% #goal %}

Detect when multi-factor authentication (MFA) is disabled for an Azure AD user.

## Strategy{% #strategy %}

This rule monitors the following Azure AD Audit Log event to detect when a user's MFA is disabled:

- `Disable Strong Authentication`

Disabling MFA makes an account more vulnerable to takeover. Attackers may attempt to disable MFA to gain access other user accounts or maintain persistence in an already-compromised account.

## Triage and response{% #triage-and-response %}

1. Determine if user `{{@properties.targetResources.userPrincipalName}}` was expected to have their MFA disabled.

1. If the change was not expected by the user:

   - Investigate other signals and suspicous behavior by `{{@properties.targetResources.userPrincipalName}}`.
   - Disable the affected user accounts.
   - Rotate user credentials.
   - Ensure MFA policies ares accurately enforced across your Azure AD tenant.
   - Begin your organization's incident response process and investigate.

1. If the change was made by the user:

   - Determine if the user was authorized to make that change.
   - If **Yes**, confirm the user is assigned MFA policies assigned in accordance with organizational requirements.
   - If **No**, verify there are no other signals or suspicious behavior from `{{@properties.targetResources.userPrincipalName}}`.
