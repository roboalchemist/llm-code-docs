# Source: https://docs.datadoghq.com/security/default_rules/def-000-vqw.md

---
title: Okta OPA server account password changed out of band
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta OPA server account password
  changed out of band
---

# Okta OPA server account password changed out of band
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detects when a server account password is altered by a method other than Okta Privileged Access (OPA) scheduled rotation.

[Okta Privileged Access](https://help.okta.com/en-us/content/topics/privileged-access/pam-accounts.htm) allows Okta users to access servers through a local server account. These individual user accounts are managed and created by Okta on each server.

## Strategy{% #strategy %}

This rule monitors Okta for successful `pam.server_account.password_change.out_of_band` events. It focuses on password changes performed outside standard rotation workflows or approved change processes for server accounts managed by OPA. Adversaries may attempt to bypass OPA based server access controls.

This detection has been adopted from rules published by the [Okta team](https://github.com/okta/customer-detections/).

## Triage & Response{% #triage--response %}

1. Identify the target server account, resource, and actor who initiated the request.
1. Verify if a legitimate change request or ticket exists.
1. Review the source IP `{{@network.client.ip}}` and geoâlocation for the actor and determine whether they align with normal administrative patterns.
1. Check OPA policy configuration to confirm the account's rotation schedule and whether this change bypassed documented rotation workflows.
1. Analyze subsequent authentications using the server account after the change to detect abnormal access or lateral movement.
1. If user activity is suspicious, begin your organization's incident response process and investigate for any account takeovers.
