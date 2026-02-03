# Source: https://docs.datadoghq.com/security/default_rules/def-000-x6y.md

---
title: AWS SES discovery attempt by long term access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS SES discovery attempt by long term
  access key
---

# AWS SES discovery attempt by long term access key
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526) 
## Goal{% #goal %}

Detect when there is an attempt to determine the status of an organization's Amazon SES account.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when there is an attempt to determine the status of an organizations Amazon SES account. Attackers target the AWS SES service generally for the purpose of phishing. In order to determine the sending quota of an account or if the account is currently in a sandbox environment, the attacker may use the API call [`GetAccount`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetAccount.html) or [`GetAccountSendingEnabled`](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetAccountSendingEnabled.html).

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have been made by the user: `{{@userIdentity.arn}}` from this IP address: `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.

## Changelog{% #changelog %}

- 17 December 2024 - updated rule query.
- 25 April 2025 - updated rule query to include `GetAccountSendingEnabled`.
