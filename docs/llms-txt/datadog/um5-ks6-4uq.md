# Source: https://docs.datadoghq.com/security/default_rules/um5-ks6-4uq.md

---
title: Mongo injections attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Mongo injections attempts
---

# Mongo injections attempts
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
### Goal{% #goal %}

Detect MongoDB injection attempts on web services accessing data from Mongo databases. Such security activity generally indicates that an attacker is trying to exploit a potential MongoDB injection vulnerability or steal sensitive data.

### Strategy{% #strategy %}

Monitor application security events to detect NoSQL (`@appsec.rule_id:(sqr-000-007 OR crs-942-290)`) injection attempts on distributed traces where external MongoDB queries are performed (`@_dd.appsec.enrichment.has_mongo:true`).

The signal severity is determined based on the underlying service behavior:

- `HIGH` Substantial rate of MongoDB injection attempts on services executing MongoDB queries, and resulting in Mongo exceptions.
- `MEDIUM` High rate of SQL/CQL injection attempts on services executing MongoDB queries.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them from reaching deeper parts of your production systems.
1. Review the 5xx errors and the other application security events detected to assess the impact on the services.
1. Investigate if the parameters are ending up in the MongoDB query without sanitization. If they do, fix the code.
