# Source: https://docs.datadoghq.com/security/default_rules/ypt-ydt-obj.md

---
title: Spring RCE post-exploitation activity attempted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Spring RCE post-exploitation activity
  attempted
---

# Spring RCE post-exploitation activity attempted
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
## Goal{% #goal %}

This rule detects attempted post-exploitation activity of [CVE-2022-22965](https://tanzu.vmware.com/security/cve-2022-22965) with an HTTP GET parameter.

## Strategy{% #strategy %}

This rule looks for `@http.url_details.path` = <RANDOM_FILE_NAME>.jsp, `@http.url_details.queryString.pwd` = `*`, and `@http.url_details.queryString.cmd` = <RANDOM_CMD_EXECUTION>. If found, it indicates web shell activity observed with successful Spring RCE exploitation.

## Triage and response{% #triage-and-response %}

Check your host to see if the {{@http.url_details.queryString.cmd}} command ran successfully. If so,

- Refer to your company's Incident Response process since this is detection post-exploitation activity.
- Refer to the vendor's [advisory](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement) for remediation of this Remote Code Execution (RCE) vulnerability.

## Changelog{% #changelog %}

- 06 June 2022 - The severity has been lowered due to rule fidelity on just log telemetry.
- 31 March 2022 - Rule added in response to [CVE-2022-22965](https://tanzu.vmware.com/security/cve-2022-22965)
