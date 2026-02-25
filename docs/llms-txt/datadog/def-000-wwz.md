# Source: https://docs.datadoghq.com/security/default_rules/def-000-wwz.md

---
title: AWS SES email sending enabled in current AWS region
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS SES email sending enabled in
  current AWS region
---

# AWS SES email sending enabled in current AWS region
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496)
## Goal{% #goal %}

Detect when email sending is enabled in your Amazon SES account for the current AWS region.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when email sending is enabled in your Amazon SES account for the current AWS region. Attackers target the AWS SES service generally for the purpose of phishing. To ensure the capbility to send email to their targets attackers will use the API calls [`UpdateAccountSendingEnabled`](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html) or [`PutAccountSendingAttributes`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountSendingAttributes.html) to enable email sending.

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have been made by the user: `{{@userIdentity.arn}}` from this IP address: `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM][3] for more information.
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.
