# Source: https://docs.datadoghq.com/security/default_rules/def-000-az2.md

---
title: Command injection attempt detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Command injection attempt detected
---

# Command injection attempt detected
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect Command Injection attempts on web services executing shell commands. Such security activity generally indicates that an attacker is trying to exploit a potential command injection vulnerability and execute malicious code on your server.

### Strategy{% #strategy %}

Monitor command injection attempts (`@appsec.security_activity:attack_attempt.command_injection`) on routes executing shell commands (`@_dd.appsec.enrichment.has_shell:true`). Excludes 404 due to excessive noise found during testing. Monitor the presence of errors tied to command execution (`@_dd.appsec.enrichment.spans_with_error:system`) to detect potential failed exploits.

Generate an Application Security Signal with `Medium` severity if attacks on routes executing commands are found.Raise the severity to `High` if errors were generated on the same trace.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.
1. Investigate if the parameters are ending up in shell commands executed without sanitization. If they do, fix the code.
1. Investigate if the host was compromised.
