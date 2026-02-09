# Source: https://docs.datadoghq.com/security/default_rules/pk1-cvn-6t2.md

---
title: Log4j Scanner detected in user agent or referrer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Log4j Scanner detected in user agent or
  referrer
---

# Log4j Scanner detected in user agent or referrer
Classification:attackTactic:[TA0043-reconnaissance](https://attack.mitre.org/tactics/TA0043)Technique:[T1595-active-scanning](https://attack.mitre.org/techniques/T1595) 
## Goal{% #goal %}

This rule detects if your Apache or NGINX web servers are being scanned for the log4j vulnerability. The initial vulnerability was identified as [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228).

## Strategy{% #strategy %}

This signal evaluated that `jndi:(ldap OR rmi OR dns)` has been detected in the HTTP header fields `user agent` and `referrer` or `referer`.

## Triage and response{% #triage-and-response %}

1. Ensure you servers have the most recent version of log4j installed.
1. Check if the `Base64 was detected in an http.user_agent or http.referrer` rule was also triggered and follow the `Triage and response` steps in that rule.

Note: Datadog's `The Monitor` blog has an article published about ["The Log4j Logshell vulnerability: Overview, detection, and remediation"](https://www.datadoghq.com/blog/log4j-log4shell-vulnerability-overview-and-remediation/).
