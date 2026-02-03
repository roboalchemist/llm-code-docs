# Source: https://docs.datadoghq.com/security/default_rules/def-000-onq.md

---
title: Cisco Duo user marked authentication request as fraudulent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Duo user marked authentication
  request as fraudulent
---

# Cisco Duo user marked authentication request as fraudulent
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when a user has marked a Duo push as fraudulent.

## Strategy{% #strategy %}

This rule monitors Cisco Duo logs for when a user marks a Duo push as fraudulent. If a user suspects that a Duo push is suspicious, such as an unusual location or application name, they will mark the push as fraudulent.

## Triage and Response{% #triage-and-response %}

1. Contact the user `{{@usr.email}}` to confirm why they thought the push was suspicious.
1. Investigate the push event, focusing on the IP address `{{@access_device.ip}}` and application `{{@application.name}}`.
1. If the event is deemed malicious, begin your organization's incident response process to contain the affected account or device.
