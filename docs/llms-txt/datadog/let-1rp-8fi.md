# Source: https://docs.datadoghq.com/security/default_rules/let-1rp-8fi.md

---
title: Java code injections attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Java code injections attempts
---

# Java code injections attempts
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect Java code injections attempts on web services executing OGNL expressions. Such security activity generally indicates that an attacker is trying to discover and exploit a potential OGNL code injection which can turn into a Remote Code Execution.

OGNL is an expression language that lets an application execute dynamic code in the application context. The expression starts as a string and can be made to execute. Upon execution, it is able to read or set access to Java objects available in its context, or call methods. OGNL injection is powerful and can achieve total takeover of an application.

### Strategy{% #strategy %}

Monitor application security events to detect OGNL payloads (`@appsec.rule_id:(dog-000-002 OR dog-000-003)`) or more generic Java code injection payloads (`@appsec.security_activity:attack_attempt.java_code_injection`) on distributed traces where OGNL expressions are compiled (`@_dd.appsec.enrichment.has_ognl:true`).

Generate an Application Security Signal with `MEDIUM` severity if the payload is OGNL specific, `LOW` if generic.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IPs temporarily to prevent them from reaching deeper parts of your production systems.
1. Investigate the context in which OGNL queries are being executed. Check if any user parameter is used to craft the expression.
