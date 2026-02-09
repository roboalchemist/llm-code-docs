# Source: https://docs.datadoghq.com/security/default_rules/clw-d08-ehj.md

---
title: Credential stuffing attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Credential stuffing attack
---

# Credential stuffing attack
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect Account Take Over (ATO) through credential stuffing attack.

A credential stuffing attack is used to gain initial access by compromising user accounts.

The attacker obtains a list of compromised usernames and passwords from a previous user database breach, phishing attempt, or other means. Then, they use the list of username and passwords to attempt to login to accounts on your application.

It is common for an attacker to use multiple IP addresses to target your application in order to distribute the attack load for load balancing purposes, to make it more difficult to detect, or make it more difficult to block.

## Strategy{% #strategy %}

**To determine a successful attempt:** Detect a high number of failed logins from at least 25 unique users and at least one successful login for a user within a period of time from the same IP address.

**To determine an unsuccessful attempt:** Detect a high number of failed logins from at least ten unique users within a period of time from the same IP address.

## Triage and response{% #triage-and-response %}

Use [this Datadog runbook](https://app.datadoghq.com/notebook/credentialstuffingrunbook) to assist in your investigation.

1. Determine if it is a legitimate attack or a false positive
1. Determine compromised users
1. Remediate compromised user accounts
