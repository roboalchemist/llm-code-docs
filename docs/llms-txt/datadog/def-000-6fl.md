# Source: https://docs.datadoghq.com/security/default_rules/def-000-6fl.md

---
title: Cisco Secure Endpoint rise in number of user login requests detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Endpoint rise in number of
  user login requests detected
---

# Cisco Secure Endpoint rise in number of user login requests detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect when there has been an anomalous number of logins to the Cisco Secure Endpoint Console.

## Strategy{% #strategy %}

This rule monitors the number of login attempts in the Cisco Secure Endpoint Console. Attackers may attempt to gain access to the console via a brute force attack.

## Triage and response{% #triage-and-response %}

1. Investigate the login requests by user `{{@usr.name}}`.
1. Implement immediate measures to block access of system for the user.
1. Inform IT security teams and management about the incident to take necessary actions.
