# Source: https://docs.datadoghq.com/security/default_rules/ldd-v8t-81e.md

---
title: Brute-forced user has assigned a role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Brute-forced user has assigned a role
---

# Brute-forced user has assigned a role
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Correlate a successful credential stuffing login with a user assumed a role.

## Strategy{% #strategy %}

Correlate the [Credential Stuffing Attack on Azure](https://docs.datadoghq.com/security/default_rules/azure_credential_stuffing_attack) and [Azure AD member assigned Global Administrator role](https://docs.datadoghq.com/security/default_rules/azure-ad-user-assigned-global-admin-role) signals based on the ARN: `{{@usr.id}}`.

## Triage and response{% #triage-and-response %}

1. Set signal triage state to `Under Review`.
1. Determine if the credential stuffing attack was successful.
   - If the login was not legitimate:
     - Investigate the user using the `User Investigation Dashboard`
     - Rotate credentials on the credential stuffed account
     - Enable MFA if it is not already enabled
   - If the login was legitimate:
     - Triage the signal as a false positive
