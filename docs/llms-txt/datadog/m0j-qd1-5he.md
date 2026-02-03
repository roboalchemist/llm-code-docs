# Source: https://docs.datadoghq.com/security/default_rules/m0j-qd1-5he.md

---
title: New AWS account seen assuming a role into AWS account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > New AWS account seen assuming a role
  into AWS account
---

# New AWS account seen assuming a role into AWS account
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199) 
## Goal{% #goal %}

Detect when an attacker accesses your AWS account from their AWS Account.

## Strategy{% #strategy %}

This rule lets you monitor AssumeRole (`@evt.name:AssumeRole`) CloudTrail API calls to detect when an external AWS account (`@userIdentity.accountId`) assumes a role into your AWS account (`account`). It does this by learning all AWS accounts from which the AssumeRole call occurs within a 7-day window. Newly detected accounts after this 7-day window will generate security signals.

## Triage and response{% #triage-and-response %}

1. Determine if the `@userIdentity.accountId` is an AWS account is managed by your company.
1. If not, try to determine who is the owner of the AWS account.
1. Inspect the role the account is assuming. Determine who created this role and who allowed this AWS account to assume this role.

## Changelog{% #changelog %}

7 April 2022 - Updated rule query and signal message.
