# Source: https://docs.datadoghq.com/security/default_rules/6a7-df6-9aa.md

---
title: Credential stuffing attack on Auth0
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Credential stuffing attack on Auth0
---

# Credential stuffing attack on Auth0
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect Account Take Over (ATO) through credential stuffing attack.

## Strategy{% #strategy %}

**To determine a successful attempt:** Detect a high number of failed logins from at least ten unique users and at least one successful login for a user. This generates a `HIGH` severity signal.

**To determine an unsuccessful attempt:** Detect a high number of failed logins from at least ten unique users. This generates an `INFO` severity signal.

## Triage and response{% #triage-and-response %}

1. Inspect the logs to see if this was a valid login attempt.
1. See if 2FA was authenticated
1. If the user was compromised, rotate user credentials.

## Changelog{% #changelog %}

13 June 2022 - Updated Keep Alive window and evaluation window to reduce rule noise.
