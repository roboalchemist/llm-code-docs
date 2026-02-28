# Source: https://docs.datadoghq.com/security/default_rules/def-000-blm.md

---
title: Command injection exploited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Command injection exploited
---

# Command injection exploited
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect successful exploits of the command injection vulnerability.

Command injection is an attack in which the goal is execution of arbitrary commands on the host operating system through a vulnerable application. Command injection attacks are possible when an application passes unsafe user parameters to a system shell. In this attack, the attacker-supplied operating system commands are usually executed with the privileges of the vulnerable application. Command injection attacks are possible largely due to insufficient input validation.

### Strategy{% #strategy %}

This detection rule is based on our [Exploit Prevention](https://www.datadoghq.com/blog/datadog-exploit-prevention/) feature. This feature leverages the context from the application to detect command injection 0-days in real time, at a very high level of accuracy. For each command executed or shell called by your application, the library reviews the user parameter for their presence in the command executed. If it finds a match, it'll review whether the parameter changes how the command is parsed (i.e. does the parameter changes the meaning of the interpreted command). In case it does, the library will flag the command as exploited and prevent its execution (if it was configured in blocking mode). This detection can't be bypassed by obfuscating the payload or by using different encoding techniques, both standard techniques to bypass WAFs.

The heuristic is controlled by rule `rasp-932-100` and `rasp-932-110`. When a match is detected, those specific requests are highlighted (`@appsec.security_activity:vulnerability_trigger.command_injection`).

The severity of the signal is set to `Critical` when the exploit is found since the exploit is proven and the attacker may be taking over the underlying infrastructure.

### Triage and response{% #triage-and-response %}

1. Consider blocking the attacking IPs temporarily to slow down the further exploitation of your infrastructure.
1. Consider switching the WAF rule `rasp-932-100` to blocking mode to prevent exploitation.
1. Leverage traces to determine the vulnerable codepath, and fix the code.

### Triage and response{% #triage-and-response-1 %}

1. Review the route and the suspected injection. In some cases, applications are vulnerable on purpose. If this is the case and the feature is properly hardened, you can introduce a passlist to ignore this vulnerability on this route.
1. If the attack isn't expected, consider switching the `rasp-932-100` and `rasp-932-110` rule to blocking mode to prevent exploitation.
1. Consider blocking the attacking IPs to slow down the further exploitation of your infrastructure.
1. Leverage the stack trace to determine the vulnerable codepaths, and fix the code by preventing any unsanitized user input from being fed into a command.
1. Review the commands executed by the attacker perform damage control.
