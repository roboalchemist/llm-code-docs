# Source: https://docs.datadoghq.com/security/default_rules/def-000-yax.md

---
title: AWS SES add verified identity followed by the deletion of the identity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS SES add verified identity followed
  by the deletion of the identity
---

# AWS SES add verified identity followed by the deletion of the identity
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1070-indicator-removal](https://attack.mitre.org/techniques/T1070)
## Goal{% #goal %}

Detect when there is an attempt to add an email address to your Amazon SES account followed by the deletion of that address in a short time period.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when there is an attempt to add an email address to your Amazon SES account followed by the deletion of that address in a short time period. Attackers target the AWS SES service generally for the purpose of phishing. To avoid detection, an attacker may add an email address to the SES account for a short period to perform a phishing attack and then remove it shortly after.

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have been made by the user: `{{@userIdentity.arn}}` from this IP address: `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM][3] for more information.
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.
