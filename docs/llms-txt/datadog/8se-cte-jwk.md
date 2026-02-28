# Source: https://docs.datadoghq.com/security/default_rules/8se-cte-jwk.md

---
title: SSRF exploited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SSRF exploited
---

# SSRF exploited
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect successful exploitation attempts of the SSRF vulnerability.

Server-Side Request Forgery (SSRF) is a web security vulnerability that allows an attacker to deceive the application and make requests to an unintended location.

In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within an organization's infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems, potentially leaking sensitive data.

### Strategy{% #strategy %}

This detection rule is based on our [Exploit Prevention](https://www.datadoghq.com/blog/datadog-exploit-prevention/) feature. This feature leverages the context from the application to detect SSRF 0-days in real time, at a very high level of accuracy. For each outbound network request performed by your application, the library reviews the user parameter for their presence in the URL. If it finds a match, it'll review whether the parameter changes the meaning of the URL and whether the change appear unexpected. In case it does, the library will flag the request as exploited and prevent it (if it was configured in blocking mode). This detection can't be bypassed by obfuscating the payload or by using different encoding techniques, both standard techniques to bypass WAFs.

A fallback capability in the backend runs when the library isn't compatible or when rules are too outdated.The backend feature monitors SSRF patterns and network queries in App & API Protection's traces. It tries to guess whether the request was tampered with by the payload captured by the WAF pattern. This approach isn't as reliable as the library-based detection due to the lack of visibility on payloads missed by the WAF.

When a match is detected, those specific requests are highlighted (`@appsec.security_activity:vulnerability_trigger.ssrf`).

The detection heuristics are as follows:

- Analyze the external HTTP requests which are performed by the application to look for suspicious calls

  - Is the URL ambiguous? Such URLs may not be parsed in the same way by all network libraries and therefore enable bypasses (eg. `bla.db.internal:6379:1324/?q=nice`)
  - Is the tampered URL leading to a sensitive domain/IP (eg. instance metadata)?

- Check if the user inputs is manipulating or tampering those requests

  - Does the user input appear to be changing the destination domain in an unexpected way?
  - Does the user input change the schema to a uncommon (non HTTP/FTP) schema?
  - Does the user input introduce new URL parameters?

The severity of the signal is lowered to `High` when the application threw an exception during execution, indicating they might not have succeeded at impacting the system.

### Triage and response{% #triage-and-response %}

1. Review the route and the suspected URL. We saw cases where applications were vulnerable on purpose. If this is the case and the feature is properly hardened, you can introduce a passlist to ignore this vulnerability on this route.
1. If the attack isn't expected, consider switching the `rasp-934-100` rule to blocking mode to prevent exploitation.
1. Consider blocking the attacking IPs to slow down the further exploitation of your infrastructure.
1. Leverage the stack trace to determine the vulnerable codepaths, and fix the code by preventing any user from making unsupervised external HTTP requests. You may also decide to isolate the services performing those requests.
1. Investigate the domains and IP addresses accessed by this SSRF attack to scope the impact of the attack.
