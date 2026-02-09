# Source: https://docs.datadoghq.com/security/default_rules/def-000-su2.md

---
title: Amazon SES enumeration attempt by previously unseen user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon SES enumeration attempt by
  previously unseen user
---

# Amazon SES enumeration attempt by previously unseen user
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526) 
## Goal{% #goal %}

Detect when the Amazon Simple Email Service (SES) is enumerated by a previously unseen user.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when the Amazon SES has been enumerated with one of the following API calls:

- [GetAccount](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_GetAccount.html)
- [GetAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetAccountSendingEnabled.html)
- [ListIdentities](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html)
- [ListEmailIdentities](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListEmailIdentities.html)
- [GetSendQuota](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html)
- [ListServiceQuotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListServiceQuotas.html)
- [GetIdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html)

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have been made by the user: `{{@userIdentity.arn}}` from this IP address : `{{@network.client.ip}}` .
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If it shouldn't have been made:
   - Contact the user: `{{@userIdentity.arn}}` and see if they made the API call.
   - Use the Cloud SIEM - User Investigation dashboard to see if the user `{{@userIdentity.arn}}` has taken other actions.
   - Use the Cloud SIEM - IP Investigation dashboard to see if there's more traffic from the IP `{{@network.client.ip}}`.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process as well as an investigation.
