# Source: https://docs.datadoghq.com/security/default_rules/im7-3xo-xff.md

---
title: OneLogin user locked out
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > OneLogin user locked out
---

# OneLogin user locked out
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect when a OneLogin user is locked out. This may be common if the user is repeatedly failing to log in. This rule is most useful when correlated with other anomalous activity for the user.

## Strategy{% #strategy %}

This rule lets you monitor the following OneLogin events to when a user is locked out:

- `@evt.name:USER_LOCKED`

## Triage and response{% #triage-and-response %}

1. Determine whether the user (`{{@usr.name}}`) was legitimately trying to authenticate and was locked out.
1. If the activity was not legitimate, review all activity from the IP (`{{@network.client.ip}}`) associated with this signal.
