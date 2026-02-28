# Source: https://docs.datadoghq.com/security/default_rules/def-000-wb9.md

---
title: GitHub critical resource enumeration activity via API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub critical resource enumeration
  activity via API
---

# GitHub critical resource enumeration activity via API
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526)
## Goal{% #goal %}

Detects mass access to secrets or workflow paths using an API request, which may represent critical data access.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for `api.request` events performed to URL paths for secrets or worfklow access.

The strategy involves tracking the token used by the actor's session to identify suspicious mass access patterns. This rule does not alert on GitHub labeled bot accounts.

## Triage & Response{% #triage--response %}

- Verify the identity of the actor (`{{@github.actor}}`) and determine if they have legitimate business reasons to access critical paths.
- Examine the specific access token used, including its creation date, permissions, and expiration.
- Review which secrets or worfklows were accessed and determine their sensitivity level.
- Analyze the actor's normal access patterns to identify deviations from typical behavior.
- Evaluate if the access occurred from unusual geographic locations or IP addresses.
- Revoke the access token immediately if activity is confirmed malicious.
- Rotate any secrets that might have been exposed in the viewed repositories.
