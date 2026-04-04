# Source: https://docs.datadoghq.com/security/default_rules/hzd-556-lum.md

---
title: Okta blocked numerous requests from a malicious IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta blocked numerous requests from a
  malicious IP
---

# Okta blocked numerous requests from a malicious IP
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detect when a request is blocked due to a block list rule (such as an IP network zone or location rule).

## Strategy{% #strategy %}

This rule lets you monitor the following Okta events to detect when a malicious IP address communicates with your Okta account:

- `security.request.blocked`

## Triage & Response{% #triage--response %}

1. Verify with the owner of `{{@usr.name}}` that they were attempting a request to `{{@target_app}}`.
1. If the request cannot be verified with the user, correlate with other log sources to see if the blocked IP in the `title` of `{{@title}}` has communicated elsewhere on the network.
