# Source: https://docs.datadoghq.com/security/default_rules/def-000-qu2.md

---
title: Twilio account geographic permissions updated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Twilio account geographic permissions
  updated
---

# Twilio account geographic permissions updated
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an update was made to the Geographic Permissions in a Twilio account.

## Strategy{% #strategy %}

This rule monitors when a change is made to the [Geographic Permissions](https://help.twilio.com/articles/223180168-What-Are-Geographic-Permissions-and-Why-do-They-Exist-) in an account. Attackers may leverage this for voice and messaging usage, leading to unexpectedly high costs.

## Triage and response{% #triage-and-response %}

1. Investigate if the change was expected.
1. Follow the [guidelines](https://help.twilio.com/articles/360021347073) provided by Twilio.
