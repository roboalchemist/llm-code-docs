# Source: https://docs.datadoghq.com/security/default_rules/def-000-df3.md

---
title: Unauthenticated activity detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Unauthenticated activity detected
---

# Unauthenticated activity detected
Tactic:[TA0004-privilege_escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1134-access-token-manipulation](https://attack.mitre.org/techniques/T1134) 
### Goal{% #goal %}

Sensitive action that should be admin-only was performed by an unauthenticated actor.

This may be caused either by incomplete integration of our SDK, or by a broken authentication flow in your system.

This may allow unauthorized actors to break your trust model and perform destructive actions, access sensitive data, and otherwise break assumptions you have on what a user is allowed to do.

### Strategy{% #strategy %}

Ensure a [user is tagged](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability) when a `activity.sensitive` [user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) is emitted.

If no user is provided , a `Medium` signal is generated.

### Triage and response{% #triage-and-response %}

1. Investigate the route where the signal triggered to understand if the issue is caused by an authentication bug, or an incorrect integration.
1. Consider blocking the malicious IPs until you can update the route.
