# Source: https://docs.datadoghq.com/security/default_rules/def-000-thd.md

---
title: Forcepoint Secure Web Gateway abnormal number of blocked urls accessed by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Secure Web Gateway abnormal
  number of blocked urls accessed by user
---

# Forcepoint Secure Web Gateway abnormal number of blocked urls accessed by user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1102-web-service](https://attack.mitre.org/techniques/T1102)
## Goal{% #goal %}

Identify users who are attempting to access an unusually anomalous number of blocked URLs.

## Strategy{% #strategy %}

This rule analyzes Forcepoint SWG logs to detect an anomalous number of blocked URL access attempts by users.

## Triage and Response{% #triage-and-response %}

1. Review the Forcepoint SWG logs for user `{{@usr.name}}` associated with this abnormal number of blocked URL access attempts.
1. Engage with the user to understand the intent behind the blocked access attempts.
1. Reset the user's credentials immediately if a compromise is suspected.
1. Educate the user about acceptable browsing behavior and your organization's internet usage policy.
