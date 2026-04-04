# Source: https://docs.datadoghq.com/security/default_rules/def-000-7hq.md

---
title: Unauthorized activity detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Unauthorized activity detected
---

# Unauthorized activity detected
Tactic:[TA0004-privilege_escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1134-access-token-manipulation](https://attack.mitre.org/techniques/T1134)
### Goal{% #goal %}

Sensitive action that should be admin-only was performed by an unauthorized actor.

This may be caused either by incomplete integration of our SDK, or by a broken authentication flow in your system.

This may allow unauthorized actors to break your trust model and perform destructive actions, access sensitive data and otherwise break assumptions you have on what a user is allowed to do.

### Strategy{% #strategy %}

Compare the `role` provided when [tagging the user](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability) with the `required_role` metadata set in `activity.sensitive` [user events](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces).

If the `required_role` is set to admin but no user is provided or the provided user doesn't have `role` set to `admin`, a `Medium` signal is generated.

The rule only match against hard-coded values, rather than directly compare the two fields. If you wish to use another (or multiple) values for either field, you can clone the rule and update it.

Do note that this rule require `role` to be set if a user is provided. The lack of a `role` metadata won't trigger this signal.

### Triage and response{% #triage-and-response %}

1. Investigate the user activity to validate that it was authorized.
1. Investigate the route where the signal triggered to understand if the issue is caused by an authentication bug, or an incorrect integration.
1. Consider blocking the malicious IPs until you can update the route.
