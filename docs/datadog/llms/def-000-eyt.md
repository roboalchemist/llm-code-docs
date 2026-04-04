# Source: https://docs.datadoghq.com/security/default_rules/def-000-eyt.md

---
title: Amazon SNS enumeration attempt by previously unseen user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon SNS enumeration attempt by
  previously unseen user
---

# Amazon SNS enumeration attempt by previously unseen user
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526)
## Goal{% #goal %}

Detect when the Amazon Simple Notification Service (SNS) is enumerated by a previously unseen user.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when the Amazon SNS has been enumerated with one of the following API calls:

- [GetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html)
- [GetSMSSandboxAccountStatus](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSSandboxAccountStatus.html)
- [ListOriginationNumbers](https://docs.aws.amazon.com/sns/latest/api/API_ListOriginationNumbers.html)
- [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html)
- [ListSubscriptions](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html)

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have been made by the user: `{{@userIdentity.arn}}` from this IP address : `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the action shouldn't have happened:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process as well as an investigation.
