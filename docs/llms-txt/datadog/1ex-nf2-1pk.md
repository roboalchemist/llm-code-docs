# Source: https://docs.datadoghq.com/security/default_rules/1ex-nf2-1pk.md

---
title: SQL injections attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SQL injections attempts
---

# SQL injections attempts
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect SQL injection attempts on web services executing SQL queries. Such security activity generally indicates that an attacker is trying to exploit potential SQL injection vulnerability or steal sensitive data.

### Strategy{% #strategy %}

Monitor application security events to detect SQL injection attempts (`@appsec.security_activity:attack_attempt.sql_injection`) on distributed traces where SQL queries are executed (`@_dd.appsec.enrichment.has_sql:true`).

The signal severity is determined based on the underlying service behavior:

- `HIGH` Substantial rate of SQL injection attempts on services executing SQL queries, and resulting in 5xx HTTP errors or SQL exceptions.
- `MEDIUM` High rate of SQL injection attempts on services executing SQL queries.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.
1. Review the 5xx errors and the other application security events detected to assess the impact on the services.
1. Investigate if the parameters are ending up in the SQL query without sanitization. If they do, fix the code.
