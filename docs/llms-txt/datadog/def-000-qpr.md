# Source: https://docs.datadoghq.com/security/default_rules/def-000-qpr.md

---
title: Indications of malicious trust anchor creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Indications of malicious trust anchor
  creation
---

# Indications of malicious trust anchor creation
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a trust anchor and profile are created using AWS IAM Roles Anywhere by the same identity.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail logs for `CreateTrustAnchor` and `CreateProfile` events using AWS IAM Roles Anywhere.

The IAM Roles Anywhere service allows workloads that do not run in AWS to assume roles by presenting a client-side X.509 certificate signed by a trusted certificate authority, represented as a trust anchor. An [attacker creating a trust anchor](https://stratus-red-team.cloud/attack-techniques/AWS/aws.persistence.rolesanywhere-create-trust-anchor/) can subsequently assume IAM roles that have a trust policy with IAM Roles Anywhere.

## Triage and response{% #triage-and-response %}

1. Determine if the user, `{{@userIdentity.arn}}`, should be generating a new trust anchor.
1. Investigate the user behavior and access information:
   - Review the user agent, IP address, and other identifying information for evidence of an abnormal access.
   - Look at additional events, such as `{{@userIdentity.arn}}` and `{{@userIdentity.accessKeyId}}` triggering `CreateSession` during the surrounding timeframe. The related events can be searched for in Roles Anywhere logs: `@eventSource:rolesanywhere.amazonaws.com`.
1. If the behavior is abnormal for the user and your environment:
   - Rotate the credentials.
   - Investigate if the same credentials took other unauthorized actions.
   - Begin your company's IR process and investigate.

## References{% #references %}
