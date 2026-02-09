# Source: https://docs.datadoghq.com/security/default_rules/def-000-qdw.md

---
title: Indications of malicious key pair creation by long term access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Indications of malicious key pair
  creation by long term access key
---

# Indications of malicious key pair creation by long term access key
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a key pair is created using a long-term access key that has a suspicious naming convention.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail logs for `CreateKeyPair` and `AuthorizeSecurityGroupIngress` or `CreateSecurityGroup` events that used a long-term access key.

Datadog's security research team has observed key pair naming conventions that include a common noun followed by a string of alphanumeric characters. The attack pattern can indicate that the long-term access key used has been compromised, `{{@userIdentity.accessKeyId}}`.

## Triage and response{% #triage-and-response %}

1. Determine if the user, `{{@userIdentity.arn}}`, should be generating a new key pair.
1. Investigate the user behavior and access information:
   - Review the user agent, IP address, and other identifying information for evidence of an abnormal access.
   - Look at additional events, such as `{{@userIdentity.arn}}` and `{{@userIdentity.accessKeyId}}` attaching a key pair to an EC2 instance during the surrounding timeframe. The related events can be searched for in EC2 logs: `@eventSource:ec2.amazonaws.com` and `@evt.name:ImportKeypair`.
1. If the behavior is abnormal for the user and your environment:
   - Rotate the credentials.
   - Investigate if the same credentials took other unauthorized actions.
   - Begin your company's IR process and investigate.
