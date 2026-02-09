# Source: https://docs.datadoghq.com/security/default_rules/def-000-3zd.md

---
title: JWT authentication bypass attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > JWT authentication bypass attempt
---

# JWT authentication bypass attempt
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
### Goal{% #goal %}

Detect when a web service is subject to processing insecure, unsigned JWT tokens. Such security activity generally indicates an attacker is tampering tokens to gain unauthorized access to protected resources or impersonate another user.

### Strategy{% #strategy %}

Monitor application security events to detect JWT authentication bypass (`@appsec.rule_id:dog-920-001`). Also, look at SQL injection triggers because CQL syntax is similar enough to SQL syntax that the SQL patterns catch CQL injection payloads.

The signal severity is determined based on the underlying service behavior:

- `HIGH`: The application is determining a valid user, this could indicate impact.
- `MEDIUM`: The application is successfully responding to a substantial number of requests containing unsecured tokens.
- `LOW`: High rate of unsuccessful requests containing unsecured tokens are being sent to the application.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IPs temporarily to prevent them from reaching deeper parts of your production systems.
1. Review if any user or role was effectively impersonated to assess the impact on the services.
1. Validate if the application accepts unsigned JWT tokens. If it does, fix the code.
