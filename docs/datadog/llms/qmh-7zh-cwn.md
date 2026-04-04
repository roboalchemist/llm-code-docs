# Source: https://docs.datadoghq.com/security/default_rules/qmh-7zh-cwn.md

---
title: Python executed with suspicious arguments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Python executed with suspicious
  arguments
---

# Python executed with suspicious arguments
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059)
## What happened{% #what-happened %}

Python was executed on the command line, using the `-c` flag with suspicious keywords that could be used to establish a reverse shell.

## Goal{% #goal %}

Detect Python code being provided and executed on the command line using the `-c` flag.

## Strategy{% #strategy %}

Python code can be specified on the command line using the `-c` flag. Attackers may use this to run "one-liners" which establish communication with an attacker-run server, download additional malware, or otherwise advance their mission. Libraries such as `socket` and `subprocess` are commonly used in these attacks and are unlikely to have a legitimate purpose when used in this way.

## Triage and response{% #triage-and-response %}

1. Review the process tree and identify if the Python command is expected.
1. If the command is not expected, contain the host or container and roll back to a known good configuration.
1. Start the incident response process and determine the initial entry point.

*Requires Agent version 7.27 or greater*
