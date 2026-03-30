# Source: https://docs.datadoghq.com/security/default_rules/def-000-6my.md

---
title: Primary email update request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Primary email update request
---

# Primary email update request
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when an API call is made to update the primary email address for an account.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when the API call [`StartPrimaryEmailUpdate`](https://docs.aws.amazon.com/accounts/latest/reference/API_StartPrimaryEmailUpdate.html) is called in an attempt to change the primary email of an AWS account.

## Triage and response{% #triage-and-response %}

1. Determine if the API call `{{@evt.name}}` should have been made by the user `{{@userIdentity.arn}}` from the IP address `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the action shouldn't have happened:
   - Contact the user (`{{@userIdentity.arn}}`) and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user (`{{@userIdentity.arn}}`) has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.
