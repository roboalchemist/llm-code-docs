# Source: https://docs.datadoghq.com/security/default_rules/593-vps-crp.md

---
title: Cassandra injection vulnerability triggered
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cassandra injection vulnerability
  triggered
---

# Cassandra injection vulnerability triggered
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect successful exploits of the CQL injection vulnerability.

### Strategy{% #strategy %}

Monitor CQL injection patterns and Cassandra queries executed.When a match is detected (that is, when the malicious pattern is found in a query as functional tokens: `@appsec.security_activity:vulnerability_trigger.cassandra`), those specific requests are highlighted.

The signal severity is determined based on whether the application threw an error when processing the CQL queries.

- `CRITICAL` An CQL injection vulnerability was exploited and impacts the system. The attackers might have exfiltrated data, tampered with your databases, or taken over the server.
- `HIGH` An CQL injection vulnerability has been triggered. However, the application threw a CQL exception during execution indicating they might not have succeeded at impacting the system.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IPs temporarily to slow down the further exploitation of your infrastructure.
1. Leverage traces to determine the vulnerable queries, and fix the code.
1. Investigate your database servers' logs to figure out the extent of the exploit.
