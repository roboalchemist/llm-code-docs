# Source: https://docs.datadoghq.com/security/default_rules/59a-cl0-v2r.md

---
title: Okta User Attempted to Access Unauthorized App
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta User Attempted to Access
  Unauthorized App
---

# Okta User Attempted to Access Unauthorized App
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1526-cloud-service-discovery](https://attack.mitre.org/techniques/T1526)
## Goal{% #goal %}

Detect when a user is denied access to an app.

## Strategy{% #strategy %}

This rule lets you monitor the following Okta events to detect when a user is denied access to an app:

- `app.generic.unauth_app_access_attempt`

## Triage and response{% #triage-and-response %}

1. Determine whether or not the user should have access to this app.
1. Contact the user to determine whether they attempted to access this app or whether their account is compromised.
