# Source: https://docs.datadoghq.com/security/default_rules/1gv-r5k-jeb.md

---
title: Credential stuffing attack on Salesforce
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Credential stuffing attack on
  Salesforce
---

# Credential stuffing attack on Salesforce
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect an account take over (ATO) through credential stuffing attack against a Salesforce account.

A credential stuffing attack is used to gain initial access by compromising user accounts.

The attacker obtains a list of compromised usernames and passwords from a previous user database breach, phishing attempt, or other means. Then, they use the list of username and passwords to attempt to login to accounts on your application.

It is common for an attacker to use multiple IP addresses to target your application in order to distribute the attack load for load balancing purposes, to make it more difficult to detect, or make it more difficult to block.

## Strategy{% #strategy %}

**To determine a successful attempt:** Detect a high number of failed logins from at least ten unique users and at least one successful login for a user within a period of time from the same IP address.

**To determine an unsuccessful attempt:** Detect a high number of failed logins from at least ten unique users within a period of time from the same IP address.

## Triage and response{% #triage-and-response %}

1. Determine if it is a legitimate attack or a false positive.
1. Determine compromised users.
1. Remediate compromised user accounts.

## Changelog{% #changelog %}

- 5 January 2023 - Updated query, severity of cases, and group by values.
