# Source: https://docs.datadoghq.com/security/default_rules/def-000-s0z.md

---
title: Okta temporary password granted and MFA reset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta temporary password granted and MFA
  reset
---

# Okta temporary password granted and MFA reset
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detects an administrator issuing a temporary password followed by the reset of all MFA factors for the Okta user.

## Strategy{% #strategy %}

This rule monitors Okta account recovery and factor administration events. Alerts when both `user.account.expire_password` and `user.mfa.factor.reset_all` succeed for the same account.

When an administrator expires a user password, there's an option to generate a temporary password for the user which can be used by an attacker to login and set their own. When factors are reset, an attacker can also add multi-factor authentication devices. The detailed behavior can represent an account takeover especially when activity occurs from uncommon geo-location or hosting provider IP addresses.

The rule severity is increased if Datadog detects the IP address is associated with a hosting provider.

## Triage & Response{% #triage--response %}

1. Identify the permissions of the affected user, `{{@target.alternateId}}`, including if they have administrator privileges within your Okta instance.
1. Review internal tickets for evidence this change was associated with a related request.
1. Examine the source IP `{{@network.client.ip}}`, geoâlocation, and associated domain.
1. If user activity is suspicious, begin your organization's incident response process and investigate for any account takeovers.
