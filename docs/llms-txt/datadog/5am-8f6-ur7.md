# Source: https://docs.datadoghq.com/security/default_rules/5am-8f6-ur7.md

---
title: Security scanner detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Security scanner detected
---

# Security scanner detected
Tactic:[TA0043-reconnaissance](https://attack.mitre.org/tactics/TA0043)Technique:[T1595-active-scanning](https://attack.mitre.org/techniques/T1595) 
### Goal{% #goal %}

Detect when a security scanner is performed on your organization's services.

### Strategy{% #strategy %}

Monitor application security events to detect security scanners activity on web services.

The Application Security Signal severity is determined based or whether the scan is targeted, based on the HTTP response status codes:

- `MEDIUM` The attack attempts triggered `5XX` errors on the underlying web service.
- `LOW` The attack attempts hit real routes of the underlying web service, or was logged in.
- `INFO` A random security scanner. Logged for audibility and not requiring any follow-up actions.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IP(s) temporarily to prevent them from reaching deeper parts of your production systems.
1. Review the `5xx` errors and the other application security events detected to assess the impact on the services.
