# Source: https://docs.datadoghq.com/security/default_rules/def-000-8gg.md

---
title: Cisco Duo administrator locked out after too many failed login attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Duo administrator locked out
  after too many failed login attempts
---

# Cisco Duo administrator locked out after too many failed login attempts
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect when a Duo administrator is locked out of their account due to failed login attempts.

## Strategy{% #strategy %}

This rule monitors administrator lockout events in Cisco Duo logs. While this could result from user error, an attacker trying to gain unauthorized access to an administrator's account may try to brute force authentications.

## Triage and Response{% #triage-and-response %}

1. Contact the user `{{@usr.name}}` to determine if they are aware of the failed authentication attempts.
1. If the user is unaware, investigate the authentication event, focusing on the IP address `{{@access_device.ip}}`, application `{{@application.name}}`, and user `{{@usr.name}}` involved.
1. If the event is deemed malicious, begin your organization's incident response process to contain the affected account or device.
