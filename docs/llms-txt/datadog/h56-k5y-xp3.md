# Source: https://docs.datadoghq.com/security/default_rules/h56-k5y-xp3.md

---
title: >-
  Google Cloud Service Account Impersonation activity using access token
  generation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Cloud Service Account
  Impersonation activity using access token generation
---

# Google Cloud Service Account Impersonation activity using access token generation
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect Google Cloud service account impersonation activity through the use of access tokens.

## Strategy{% #strategy %}

Monitor Google Cloud Admin Activity audit logs for event `@evt.name:GenerateAccessToken`:

- Successful Attempts: `@data.protoPayload.authorizationInfo.granted:true`
- Failed Attempts: `@evt.outcome:PERMISSION_DENIED`

## Triage & Response{% #triage--response %}

1. Investigate if the user `{{@usr.id}}` from IP address:`{{@network.client.ip}}` intended to perform this activity.
1. If unauthorized:
   - Revoke access of compromised user and service account.
   - Investigate other activities performed by the user `{{@usr.id}}` using the Cloud SIEM - User Investigation dashboard.
   - Investigate other activities performed by the IP `{{@network.client.ip}}` using the Cloud SIEM - IP Investigation dashboard.
