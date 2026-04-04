# Source: https://docs.datadoghq.com/security/default_rules/def-000-eg6.md

---
title: Potential rootkit compiled and then loaded
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Potential rootkit compiled and then
  loaded
---

# Potential rootkit compiled and then loaded
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1574-hijack-execution-flow](https://attack.mitre.org/techniques/T1574)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was used to load a recently compiled kernel module or shared object that could be a rootkit.

## Goal{% #goal %}

Detect malicious user or kernel modules being compiled and then loaded.

## Strategy{% #strategy %}

Attackers will attempt to use kernel or user mode rootkits for various purposes, to include privilege escalation, code execution, or defense evasion. Typically, the actors will have to first compile the module, and then load it with a dynamic linker or by loading the object directly.

## Triage and response{% #triage-and-response %}

1. Determine whether the compiled module is expected to be present on the system.
1. If this behavior is unexpected, attempt to contain the compromise (possibly by terminating the workload, depending on the stage of attack), and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the scope of the attack. Investigate whether the file was added to multiple containers around the same time, and whether the affected systems follow a pattern. For example, if a file was seen executing in multiple containers, do the containers share the same workload or base image? What other activity occurred directly before or after the file was compiled?
