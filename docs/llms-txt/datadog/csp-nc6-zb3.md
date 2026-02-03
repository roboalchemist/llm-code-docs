# Source: https://docs.datadoghq.com/security/default_rules/csp-nc6-zb3.md

---
title: SSRF attempts on routes executing network queries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SSRF attempts on routes executing
  network queries
---

# SSRF attempts on routes executing network queries
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
### Goal{% #goal %}

Detect Server-Side Request Forgery (SSRF) attempts on web services performing external HTTP requests. Such security activity generally indicates that an attacker is trying to discover and exploit a potential SSRF vulnerability.

Server-Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to deceive the application and make requests to an unintended location.

In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within an organization's infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems, potentially leaking sensitive data.

### Strategy{% #strategy %}

Monitor application security events to detect SSRF (`@appsec.security_activity:attack_attempt.ssrf`) on distributed traces where external HTTP requests are performed (`@_dd.appsec.enrichment.has_http_client:true`).

Generate an Application Security Signal with `MEDIUM` severity.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.
1. Check the `TARGETED URLS` to see if there is any suspicious call not intended by the application.
1. Investigate if the parameters are ending up in the HTTP call without sanitization. If they do, fix the code.
