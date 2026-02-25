# Source: https://docs.datadoghq.com/security/default_rules/wn5-psv-go1.md

---
title: Shell command history modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Shell command history modified
---

# Shell command history modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1070-indicator-removal](https://attack.mitre.org/techniques/T1070)
## What happened{% #what-happened %}

The shell history file `{{ @file.path }}` was modified by `{{ @process.comm }}`, potentially to hide evidence.

## Goal{% #goal %}

Detect the tampering of shell command history on a host or container.

## Strategy{% #strategy %}

Commands used within a terminal are contained within a local file so users can review applications, scripts, or processes that were previously executed. Adversaries tamper with the integrity of the shell command history by deletion, truncation, or the linking of `/dev/null` by use of a symlink. This allows adversaries to obfuscate their actions and delay the incident response process.

## Triage and response{% #triage-and-response %}

1. Review the tampering action taken against the shell command history files.
1. Review the user or process that performed the action against the shell command history.
1. Determine whether or not this is expected behavior.
1. If this activity is not expected, contain the host or container, and roll back to a known good configuration.

*Requires Agent version 7.27 or greater*
