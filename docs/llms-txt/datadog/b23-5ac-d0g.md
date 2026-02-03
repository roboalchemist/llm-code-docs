# Source: https://docs.datadoghq.com/security/default_rules/b23-5ac-d0g.md

---
title: Jumpcloud admin login without MFA
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Jumpcloud admin login without MFA
---

# Jumpcloud admin login without MFA
Classification:complianceTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)Framework:cis-awsControl:4.2 
## Goal{% #goal %}

Detect when a JumpCloud administrator authenticates without multi-factor authentication (MFA) enabled. This is not indicative of malicious activity, however as a best practice, administrator accounts should have MFA enabled.

## Strategy{% #strategy %}

This rule monitors JumpCloud audit logs to detect when an admin user successfully authenticates to JumpCloud and the log indicates that `@mfa` is `false`.

## Triage and response{% #triage-and-response %}

1. Reach out to the {{@usr.name}} to determine if the login was legitimate.
1. If the login was legitimate, request that the user enables MFA.
1. If the login wasn't legitimate, rotate the credentials, enable MFA and triage an actions uncovered from step 1.
1. Review all user accounts to ensure MFA is enabled.
