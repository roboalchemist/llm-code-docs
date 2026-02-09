# Source: https://docs.datadoghq.com/security/default_rules/def-000-ffs.md

---
title: Twilio account token promoted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Twilio account token promoted
---

# Twilio account token promoted
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a secondary token was promoted to primary.

## Strategy{% #strategy %}

This rule monitors for the promotion of an authentication token to primary status. An attacker may attempt this to escalate their privileges within the account.

## Triage and response{% #triage-and-response %}

1. Investigate the other actions performed by the account SID `{{@account_sid}}`.
1. Follow the [guidelines](https://help.twilio.com/articles/360021347073) provided by Twilio.
