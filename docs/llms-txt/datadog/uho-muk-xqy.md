# Source: https://docs.datadoghq.com/security/default_rules/uho-muk-xqy.md

---
title: Shell process created by Java application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Shell process created by Java
  application
---

# Shell process created by Java application
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
## What happened{% #what-happened %}

{{#is_exact_match "case_name" "confluence_server_spawned_shell_potential_rce"}}A Confluence server executed the command `{{ @process.comm }}`. The server may be vulnerable to one of several well-known remote-code execution (RCE) exploits.{{/is_exact_match}} {{#is_exact_match "case_name" "java_shell_execution_known_bad"}}A Java application executed the command `{{ @process.comm }}` with arguments associated with malicious behavior. This activity should never be executed legitimately.{{/is_exact_match}} {{#is_exact_match "case_name" "java_shell_execution_unusual"}}A Java application executed the command `{{ @process.comm }}` which is unusual. Review the process tree and associated process arguments.{{/is_exact_match}} {{#is_exact_match "case_name" "java_shell_execution_suspicious"}}A Java application executed the command `{{ @process.comm }}` which is suspicious. Review the process tree and associated process arguments.{{/is_exact_match}} {{#is_exact_match "case_name" "java_shell_execution"}}A Java process executed the command `{{ @process.comm }}` which may indicate the service is vulnerable to remote code execution (RCE).{{/is_exact_match}}

## Goal{% #goal %}

Detect attackers taking advantage of a flaw in a Java application to execute commands.

## Strategy{% #strategy %}

This detection monitors process executions and generates a signal when a process is spawned from Java. The severity of the signal is based on how closely the activity aligns with known malicious behavior.

## Triage and response{% #triage-and-response %}

- Java applications have a variety of uses. Determine the nature and purpose of the service.
- Determine whether there is an approved purpose for the Java process to execute `{{ @process.comm }}`. {{#if service}}Contacting the owner of the `{{service}}` service may be necessary.{{/if}}
- If this behavior is unexpected, attempt to contain the compromise.
- Investigate application logs or traces to identify the cause of the execution.
- Find and repair the root cause of the exploit. {{#is_exact_match "case_name" "confluence_server_spawned_shell_potential_rce"}}If a vulnerability in Confluence is the root cause, update the server to the latest version.{{/is_exact_match}}

## Changelog{% #changelog %}

- 26 September 2024 - Updated rule name and description

*Requires Agent version 7.27 or later*
