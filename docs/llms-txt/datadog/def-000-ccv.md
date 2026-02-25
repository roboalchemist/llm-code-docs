# Source: https://docs.datadoghq.com/security/default_rules/def-000-ccv.md

---
title: Oracle Cloud user failed login followed by success
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Oracle Cloud user failed login followed
  by success
---

# Oracle Cloud user failed login followed by success

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect potentially successful bruteforce attempt.

## Strategy{% #strategy %}

This rule monitors logs from OCI to detect successful bruteforce attempts. A signal is generated after 5 or more failed attempts for a specific user are followed by a successful login for the same user.

## Triage and response{% #triage-and-response %}

1. Review the logs associated with this signal. Determine if the user `{{ @usr.name }}` is expected to authenticate from the IP address `{{ @network.client.ip }}`.
1. Review audit logs for suspicious actions taken by the user after authenticating.
1. Rotate credentials for the affected account.

## Changelog{% #changelog %}

- 25 September 2025 - Updated query successful login.
