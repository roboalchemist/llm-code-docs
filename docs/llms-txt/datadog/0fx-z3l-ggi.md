# Source: https://docs.datadoghq.com/security/default_rules/0fx-z3l-ggi.md

---
title: Okta Impersonation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Okta Impersonation
---

# Okta Impersonation
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1199-trusted-relationship](https://attack.mitre.org/techniques/T1199)
## Goal{% #goal %}

Detect an Okta session impersonation.

## Strategy{% #strategy %}

This rule lets you monitor the following Okta events to detect a user session impersonation:

- `user.session.impersonation.initiate`
- `user.session.impersonation.end`
- `user.session.impersonation.grant`
- `user.session.impersonation.extend`
- `user.session.impersonation.revoke`

These events indicate that the user: `{{@usr.email}}` has the effective permissions of the impersonated user. This is likely to occur through [Okta support access](https://support.okta.com/help/s/article/Granting-Access-to-Okta-Support?language=en_US). This [blog](https://blog.cloudflare.com/cloudflare-investigation-of-the-january-2022-okta-compromise/) illustrates the potential impact an attacker can cause by impersonation session.

## Triage and response{% #triage-and-response %}

1. Contact your Okta administrator to ensure the user: `{{@usr.email}}` is authorized to impersonate a user session.
1. If the user impersonation session is not legitimate:
   - Task your Okta administrator to end the impersonation session.
   - Investigate the actions taken by the user `{{@usr.email}}` during the session and revert back to the last known good state.
   - Begin your company's incident response process and investigate.
