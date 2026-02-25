# Source: https://docs.datadoghq.com/security/default_rules/def-000-o5y.md

---
title: >-
  Forcepoint Secure Web Gateway unusual spike found in requests for low
  reputation urls by users
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Forcepoint Secure Web Gateway unusual
  spike found in requests for low reputation urls by users
---

# Forcepoint Secure Web Gateway unusual spike found in requests for low reputation urls by users

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Identify an unusual spike in requests for low reputation URLs.

## Strategy{% #strategy %}

This rule analyzes Forcepoint SWG logs to identify an unusual spike in requests for low reputation URLs.

## Triage and Response{% #triage-and-response %}

1. Review the Forcepoint SWG logs to identify the [user`{{@usr.name](mailto:user%60%7b%7b@usr.name)}}`requesting a bad reputation URL`{{@http.url}}`.
1. Examine user activities and actions taken by Forcepoint SWG, focusing on fields like activity, action, and application.
1. Identify any potential sensitive data patterns in the DLP pattern field, if present, and analyze uploaded file details such as file type, size, and hash values, if available.
1. Reset user credentials if malicious intent is suspected.
1. Quarantine flagged files and ensure uploads are blocked if not already restricted.
1. Immediately block the bad reputed URL if not already blocked.
1. Notify and educate the user about safe browsing practices.
