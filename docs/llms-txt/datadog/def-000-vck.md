# Source: https://docs.datadoghq.com/security/default_rules/def-000-vck.md

---
title: Local file inclusion exploited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Local file inclusion exploited
---

# Local file inclusion exploited
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
### Goal{% #goal %}

Detect successful exploits of the local file inclusion vulnerability.

Local file inclusion (also known as LFI) is the process of including files that are already locally present on the server, through the exploiting of file access code implemented in the application. This vulnerability occurs, for example, when a page receives the path to the file that has to be included and this path is not properly sanitized. This allows directory traversal characters (such as dot-dot-slash) to be injected and interpreted. Although most examples point to vulnerable PHP scripts, it is also common in other technologies such as JSP, ASP, and others.

### Strategy{% #strategy %}

This detection rule is based on our [Exploit Prevention](https://www.datadoghq.com/blog/datadog-exploit-prevention/) feature. This feature leverages the context from the application to detect LFI 0-days in real time, at a very high level of accuracy. For each file accessed by your application, the library reviews the user parameter for their presence in the path accessed. If it finds a match, it'll review whether the parameter defines an absolute path (`/etc/passwd`) or a relative path (`../../etc/passwd`). In case it does, the library will flag the access as exploited and prevent it (if it was configured in blocking mode). This detection can't be bypassed by obfuscating the payload or by using different encoding techniques, standard techniques to bypass WAFs.

The heuristic is controlled by rule `rasp-930-100`. When a match is detected, those specific requests are highlighted (`@appsec.security_activity:vulnerability_trigger.lfi`).

The severity of the signal is set to `Critical` when the exploit is found. Since this pattern is quite common in internal APIs, we lower the severity to Medium if the attempt comes from an internal IP (`-@api.security.traffic_stats.ip_type:public`).

### Triage and response{% #triage-and-response %}

1. Review the route and the file access. We saw cases where applications were vulnerable on purpose. If this is the case and the feature is properly hardened, you can introduce a passlist to ignore this vulnerability on this route.
1. If the attack isn't expected, consider switching the `rasp-930-100` rule to blocking mode to prevent exploitation.
1. Consider blocking the attacking IPs to slow down the further exploitation of your infrastructure.
1. Leverage the stack trace to determine the vulnerable codepaths, and fix the code by preventing users from accessing arbitrary or relative paths.
1. Review secrets that may already have leaked and rotate them if necessary.
