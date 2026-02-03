# Source: https://docs.datadoghq.com/security/default_rules/def-000-jxj.md

---
title: Cisco Duo bypass code is used to authenticate user request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Duo bypass code is used to
  authenticate user request
---

# Cisco Duo bypass code is used to authenticate user request
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when a Duo bypass code is used to authenticate a user request.

## Strategy{% #strategy %}

This rule monitors successful authentication events in Cisco Duo logs where the reason is set to `bypass_user`.

## Triage and Response{% #triage-and-response %}

1. Contact the user `{{@usr.email}}` to confirm they used the bypass code.
1. If the user is unaware, investigate the authentication event, focusing on the IP address `{{@access_device.ip}}`, application `{{@application.name}}`, and user `{{@usr.email}}` involved.
1. If the event is deemed malicious, begin your organization's incident response process to contain the affected account or device.
