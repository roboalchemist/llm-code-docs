# Source: https://docs.datadoghq.com/security/default_rules/g6h-rq4-3y9.md

---
title: Credential stuffing attack on Jumpcloud
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Credential stuffing attack on Jumpcloud
---

# Credential stuffing attack on Jumpcloud
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect an account take over (ATO) through credential stuffing attack against a Jumpcloud account.

## Strategy{% #strategy %}

**To determine a successful attempt:** Detect a high number of failed logins from at least seven unique users and at least one successful login for a user within a period of time from the same IP address.

**To determine an unsuccessful attempt:** Detect a high number of failed logins from at least seven unique users within a period of time from the same IP address.

## Triage and response{% #triage-and-response %}

1. Determine if it is a legitimate attack or a false positive.
1. Determine compromised users.
1. Remediate compromised user accounts.
