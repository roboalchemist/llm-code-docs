# Source: https://docs.datadoghq.com/security/default_rules/jhe-xm6-xdm.md

---
title: Base64 was detected in an http.user_agent or http.referrer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Base64 was detected in an
  http.user_agent or http.referrer
---

# Base64 was detected in an http.user_agent or http.referrer
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1027-obfuscated-files-or-information](https://attack.mitre.org/techniques/T1027) 
## Goal{% #goal %}

This rule detects if your Apache or NGINX web servers are being exploited using the log4j vulnerability. The initial vulnerability was identified as [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228).

## Strategy{% #strategy %}

This signal evaluated that `Base64` has been detected in the HTTP header fields `user agent` and `referrer` or `referer`.

## Triage and response{% #triage-and-response %}

1. Ensure you servers have the most recent version of log4j installed.
1. If you are not patched, decode the base64 string and look for any successful traffic to the malicious server.
1. If a connection was successful to the malicious server, begin your company's IR procedures to remediate.

Note: Datadog's `The Monitor` blog has an article published about ["The Log4j Logshell vulnerability: Overview, detection, and remediation"](https://www.datadoghq.com/blog/log4j-log4shell-vulnerability-overview-and-remediation/).
