# Source: https://docs.datadoghq.com/security/default_rules/re3-xfr-z60.md

---
title: SQL injection exploited
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SQL injection exploited
---

# SQL injection exploited
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect successful exploits of the SQL injection vulnerability.

A SQL injection attack consists of the insertion or "injection" of a SQL query in the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system, and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into a user parameter in order to affect the execution of predefined SQL commands. (See [the OWASP documentation](https://owasp.org/www-community/attacks/SQL_Injection).)

### Strategy{% #strategy %}

This detection rule is based on our [Exploit Prevention](https://www.datadoghq.com/blog/datadog-exploit-prevention/) feature. This feature leverages the context from the application to detect SQL injection 0-days in real time, at a very high level of accuracy. For each SQL query executed by your application, the library reviews the user parameter for their presence in the SQL query. If it finds a match, it'll review whether the parameter changes how the SQL query is parsed (in other words, whether the parameter changes the meaning of the query). In case it does, the library will flag the query as exploited and prevent it (if it was configured in blocking mode). This detection can't be bypassed by obfuscating the payload or by using different encoding techniques, both standard techniques to bypass WAFs.

A fallback capability in the backend runs when the library isn't compatible or when rules are too outdated.The backend feature monitors SQL injection patterns and SQL queries executed in App & API Protection's traces. It tries to guess whether the query was tampered with by the payload captured by the WAF pattern. This approach isn't as reliable as the library-based detection due to the SQL query being obfuscated before reaching the backend, and the lack of visibility on payloads missed by the WAF.

When a match is detected, those specific requests are highlighted (`@appsec.security_activity:vulnerability_trigger.sql_injection`).

The signal severity is determined based on whether the application threw an error when processing the SQL queries.

- `CRITICAL` An SQL injection vulnerability was exploited and has impacts on the system. The attackers might have exfiltrated data, tampered with your databases, or taken over the server.
- `HIGH` An SQL injection vulnerability has been triggered. However, the application threw a SQL exception during execution indicating they might not have succeeded at impacting the system.

### Triage and response{% #triage-and-response %}

1. Review the route and the injected query. In some cases, applications are vulnerable on purpose. If this is the case and the feature is properly hardened, you can introduce a passlist to ignore this vulnerability on this route.
1. If the attack isn't expected, consider switching the `rasp-942-100` rule to blocking mode to prevent exploitation.
1. Consider blocking the attacking IPs to slow down the further exploitation of your infrastructure.
1. Leverage the stack trace to determine the vulnerable queries, and fix the code.
1. Investigate your database servers' logs to figure out the extent of the exploitation.
