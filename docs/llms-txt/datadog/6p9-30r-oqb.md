# Source: https://docs.datadoghq.com/security/default_rules/6p9-30r-oqb.md

---
title: Microsoft 365 - Modification of Trusted Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Microsoft 365 - Modification of Trusted
  Domain
---

# Microsoft 365 - Modification of Trusted Domain
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detects when a user creates or modifies a trusted domain object in Microsoft 365.

## Strategy{% #strategy %}

Monitor Azure AD Audit logs for the following `@evt.name`:

- `Set federation settings on domain`
- `Set domain authentication`

Monitor Microsoft 365 Audit logs for the following `@evt.name`:

- `Set federation settings on domain.`
- `Set domain authentication.`

An attacker can create a new attacker-controlled domain as federated or modify the existing federation settings for a domain by configuring a new, secondary signing certificate. Both of these techniques would allow the attacker to authenticate as any user bypassing authentication requirements like a valid password or MFA.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.id}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:
   - Remove the suspicious domain or settings.
   - Begin your organization's Incident Response (IR) process.
1. If the API call was made by the user:
   - Ensure the change was authorized.
