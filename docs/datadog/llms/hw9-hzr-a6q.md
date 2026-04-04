# Source: https://docs.datadoghq.com/security/default_rules/hw9-hzr-a6q.md

---
title: Log4shell vulnerability triggered (RCE) - CVE-2021-44228
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Log4shell vulnerability triggered (RCE)
  - CVE-2021-44228
---

# Log4shell vulnerability triggered (RCE) - CVE-2021-44228
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect successful exploits of the Log4shell vulnerability (CVE-2021-44228).

The vulnerability has [CVSS Score: 10.0 CRITICAL](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) and can lead to Remote Code Execution (RCE).

### Strategy{% #strategy %}

Monitor payloads matching known patterns for CVE-2021-44228 (event rule: #sqr-000-017 ) and lookup for HTTP requests to load a Java class.

Generate an Application Security signal with `CRITICAL` severity.

### Response{% #response %}

Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.

### Remediation{% #remediation %}

Considering the targeted application uses a vulnerable version of log4j and the default settings are disabled:

- Update log4j to the latest patched version immediately (>= 2.15.0)
- Disable lookups by setting `formatMsgNoLookups=true`. Only available from log4j >= 2.10 versions
- Use a non-vulnerable or empty implementation of the class `org.apache.logging.log4j.core.lookup.JndiLookup`
- Investigate the logs and the external class that is being called in the attack to check if the attacker successfully executed arbitrary code or not.
