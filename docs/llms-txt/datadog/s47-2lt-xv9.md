# Source: https://docs.datadoghq.com/security/default_rules/s47-2lt-xv9.md

---
title: Reflected XSS attempts on routes returning HTML
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Reflected XSS attempts on routes
  returning HTML
---

# Reflected XSS attempts on routes returning HTML
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
### Goal{% #goal %}

Detect Reflected Cross-Site Scripting (XSS) attempts on web services returning HTML. Such security activity generally indicates that an attacker is trying to exploit a potential XSS vulnerability or steal sensitive data.

### Strategy{% #strategy %}

Monitor reflected cross-site scripting attempts (`@appsec.security_activity:attack_attempt.xss`) on services returning HTML (`@http.response.headers.content-type:text\/html*`).Excludes requests that use the `HEAD` method (`-@http.method:HEAD`) because they don't return a body and are therefore not vulnerable.

Generate an Application Security Signal with `LOW` severity.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.
1. Investigate if the parameters are ending up in the HTML body without sanitization. If they do, fix the code.
