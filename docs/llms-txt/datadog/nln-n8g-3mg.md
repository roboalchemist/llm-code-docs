# Source: https://docs.datadoghq.com/security/default_rules/nln-n8g-3mg.md

---
title: Spring4shell RCE attempts - CVE-2022-22963
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Spring4shell RCE attempts -
  CVE-2022-22963
---

# Spring4shell RCE attempts - CVE-2022-22963
Tactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
### Goal{% #goal %}

Detect attempts to exploit the spring4shell vulnerability (CVE-2022-22963).

### Strategy{% #strategy %}

Monitor payload matching the known patterns for the Spring core RCE known as Spring4shell (event rule: #dog-000-004) triggering on Java applications `@language:(jvm OR java)` and generate an Application Security signal with `Medium` severity.A backup condition that looks for existing rules (`@appsec.security_activity:attack_attempt.java_code_injection`) that trigger on the key that is used in the exploit (`@appsec.triggers.rule_matches.parameters.key_path:class.module.classLoader.*`).

### Response{% #response %}

Consider blocking the attacking IP(s) temporarily to prevent them to reach deeper parts of your production systems.

### Remediation{% #remediation %}

If you are using Spring framework (v5.3.0 to 5.3.17, 5.2.0 to 5.2.19, and older versions) on JDK9+ and packaged it as WAR on Apache Tomcat, there is a high chance that you are vulnerable and need to do one of the following.

- Upgrade to Spring Framework v5.3.18 and v5.2.20
- If you are unable to upgrade, Datadog recommends applying Spring's [workaround](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement#suggested-workarounds) to mitigate the risk of an exploit
