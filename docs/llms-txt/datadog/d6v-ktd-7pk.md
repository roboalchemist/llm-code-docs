# Source: https://docs.datadoghq.com/security/default_rules/d6v-ktd-7pk.md

---
title: Vault root token
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Vault root token
---

# Vault root token
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when a vault root token is used. Root tokens can perform any activity and have the highest level of privileges in Vault and should only be used in emergencies.

## Strategy{% #strategy %}

This rule monitors Vault Audit Logs (`source:vault`) to detect when `root` is seen in:

- auth policy (`@auth.policies`)

This rule also monitors the API endpoint `/sys/generate-root` which is used to create new root keys.

## Triage & Response{% #triage--response %}

1. Determine who created the root token and when. You can get token creation time using the token accessor with `vault token lookup -accessor <accessor>`.
1. Inspect the requests made with the root token and ensure that its usage is valid.
1. Ensure that after the root token is no longer needed, it is revoked (`vault token revoke -accessor <token>`).

## Change Log{% #change-log %}

- 29 June 2022 - Updated queries to reduce noise levels. Replaced initial query with token creation detection.
- 17 October 2022 - Updated queries and cases.
- 13 December 2023 - Updated group by values.
- 23 September 2024 - Reduce severity of cases to Medium.
