# Source: https://docs.datadoghq.com/security/default_rules/7zj-fzr-45s.md

---
title: Resource enumeration detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Resource enumeration detected
---

# Resource enumeration detected

### Goal{% #goal %}

Detect attempts by an attacker to exfiltrate sensitive information using a [Resource Enumeration attack](https://owasp.org/www-community/attacks/Forced_browsing).

The attack is based on finding endpoints that return a resource when given an ID, and whose security relies on the ID being only known to authorized users. When such endpoints are found, the attacker can iterate over all possible ID values until finding valid ones and then leak sensitive information.

Such vulnerable endpoints are common since authentication is sometimes cumbersome to implement and the large range of possible IDs appear secure enough. Billing systems are a common example.

### Strategy{% #strategy %}

Monitor APM traces from REST endpoints expecting an ID. Traces coming from local IPs are discarded in order to passlist internal microservices traffic.

Traces left are aggregated in small groups sharing the same targeted service, source IP and endpoint. Status codes are then compared. If over 100 requests with 4xx status code are found and at least one request with a 200 code is also detected, the endpoint is deemed under attack by the IP. We interpret the 4xx requests as the unsuccessful scanning and the 200 request as a correctly guessed ID.

A `Low` signal is then generated.

### Triage and response{% #triage-and-response %}

1. Investigate the expected usage profile of the endpoint under attack.
   - If the endpoint is expecting this kind of traffic or requests are coming from an internal IP, create a suppression query.
1. Consider blocking the attacking IPs temporarily to prevent them from continuing their attack.
1. Investigate how to add authentication to the endpoint with your engineering team.
