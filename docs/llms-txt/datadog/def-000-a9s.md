# Source: https://docs.datadoghq.com/security/default_rules/def-000-a9s.md

---
title: Temporary AWS security credentials generated for user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Temporary AWS security credentials
  generated for user
---

# Temporary AWS security credentials generated for user
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a set of temporary security credentials consisting of an access key ID, a secret access key, and a security token, are generated for a user.

## Strategy{% #strategy %}

This rule monitors CloudTrail and detects when any `@eventName` has a value of `GetFederationToken` and `@eventSource` has a value of `sts.amazonaws.com`. An adversary can maintain persistence within an AWS environment using credentials generated from `sts:GetFederationToken`, even if the original AWS access keys have been deleted.

## Triage & Response{% #triage--response %}

1. Determine if the user `{{@userIdentity.arn}}` intended to generate a federated token for the observed federated user(s).
1. If `{{@userIdentity.arn}}` didn't intend to generate the federated token:
   - Completely remove all permissions of the compromised IAM user, as simply disabling the access key used to issue the session is not enough for containment **OR**
   - Attach an explicit deny-all IAM policy to the compromised IAM user as this will take precedence over all allow statements.
   - Follow [AWS' recommendation](https://aws.amazon.com/blogs/security/how-to-revoke-federated-users-active-aws-sessions/) on `How to revoke federated users' active AWS sessions`.
1. Investigate other activities performed by the user `{{@userIdentity.arn}}` and the observed federated user(s) using the Cloud SIEM - User Investigation dashboard.
1. Begin your organization's incident response process and investigate.
1. Consider the usage of **temporary credentials** over long-lived credentials associated with IAM users. This prevents the usage of long-lived AWS Access keys which are [required](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html) for creating federated sessions from IAM users.

## Changelog{% #changelog %}

- 06 Nov 2024 - Rule query and severity updated.
