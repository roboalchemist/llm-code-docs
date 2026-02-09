# Source: https://docs.datadoghq.com/security/default_rules/zih-1e3-b12.md

---
title: CQL injections attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > CQL injections attempts
---

# CQL injections attempts
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
### Goal{% #goal %}

Detect CQL injections attempts on web services accessing to data from Cassandra databases. Such security activity generally indicates that an attacker is trying to exploit a potential CQL injection vulnerability or steal sensitive data.

### Strategy{% #strategy %}

Monitor application security events to detect SQL (`@appsec.security_activity:attack_attempt.sql_injection`) & CQL (`@appsec.rule_id:dog-000-001`) injection attempts on distributed traces where external CQL queries are performed (`@_dd.appsec.enrichment.has_cassandra:true`).Also, look at SQL injection triggers because CQL syntax is similar enough to SQL syntax that the SQL patterns catch CQL injection payloads.

The signal severity is determined based on the underlying service behavior:

- `HIGH` Substantial rate of SQL/CQL injection attempts on services executing CQL queries, and resulting in Cassandra exceptions.
- `MEDIUM` High rate of SQL/CQL injection attempts on services executing CQL queries.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them from reaching deeper parts of your production systems.
1. Review the 5xx errors and the other application security events detected to assess the impact on the services.
1. Investigate if the parameters are ending up in the CQL query without sanitization. If they do, fix the code.
