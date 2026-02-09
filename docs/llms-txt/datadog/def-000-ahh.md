# Source: https://docs.datadoghq.com/security/default_rules/def-000-ahh.md

---
title: Additional AWS regions enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Additional AWS regions enabled
---

# Additional AWS regions enabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1535-unused-or-unsupported-cloud-regions](https://attack.mitre.org/techniques/T1535) 
## Goal{% #goal %}

Detect when additional AWS regions have been enabled.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when additional AWS regions have been enabled. Attackers may enable additional regions to allow for the creation of a greater number of resources like EC2 instances or ECS clusters for the purpose of cryptomining.

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have been made by the user: `{{@userIdentity.arn}}` from this IP address: `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM][3] for more information.
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, initiate your company's incident response process, as well as an investigation.
