# Source: https://docs.datadoghq.com/security/default_rules/def-000-l7a.md

---
title: Creation of new AWS Bedrock long term access key with no expiration date
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Creation of new AWS Bedrock long term
  access key with no expiration date
---

# Creation of new AWS Bedrock long term access key with no expiration date
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1552-unsecured-credentials](https://attack.mitre.org/techniques/T1552)
## Goal{% #goal %}

Detects when a [long term API key for AWS Bedrock](https://www.wiz.io/blog/a-new-type-of-long-lived-key-on-aws-bedrock-api-keys) is created without an expiration date

## Strategy{% #strategy %}

This rule monitors CloudTrail and detects when any `@eventName` has a value of `CreateServiceSpecificCredential`, `@responseElements.serviceSpecificCredential.serviceName:bedrock.amazonaws.com` has a value of `bedrock.amazonaws.com`, and the expiration date begins with `21` (indicating an expiration date 100 years in the future). Long term access keys are vulnerable to compromise by infostealers and credential leaks, and a lack of an expiration date significantly increases the change of compromise.

## Triage & Response{% #triage--response %}

1. Determine if the user `{{@userIdentity.arn}}` intended to generate a Bedrock token with no expiration date.
1. If `{{@userIdentity.arn}}` didn't intend to generate the Bedrock token with no expiration date or the token is not compliant with your organization's policies:
   - Delete the token `{{@responseElements.serviceSpecificCredential.serviceSpecificCredentialId}}` by calling `DeleteServiceSpecificCredential` or deactivate it using `UpdateServiceSpecificCredential`
1. Investigate calls made by the key's associated IAM User `{{@responseElements.serviceSpecificCredential.userName}}` for signs of malicious activity.
1. Begin your organization's incident response process and investigate.
1. Consider creating an [IAM policy condition](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html) with the condition `iam:ServiceSpecificCredentialAgeDays` to require expiration dates.
1. Consider the usage of **temporary credentials** over long-lived credentials associated with IAM users.
