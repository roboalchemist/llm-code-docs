# Source: https://docs.datadoghq.com/security/default_rules/80l-dwm-pi6.md

---
title: Dynamic linker hijacking attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Dynamic linker hijacking attempt
---

# Dynamic linker hijacking attempt
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1574-hijack-execution-flow](https://attack.mitre.org/techniques/T1574)
## What happened{% #what-happened %}

{{#is_exact_match "case_name" "dynamic_linker_config_unlink"}}The file which configures dynamically linked libraries was deleted. Program functions may have been overridden to hide processes or files and evade detection.{{/is_exact_match}} {{#is_exact_match "case_name" "dynamic_linker_config_write"}}The file which configures dynamically linked libraries was modified. Program functions may have been overridden to hide processes or files and evade detection.{{/is_exact_match}} {{#is_exact_match "case_name" "ld_preload_unusual_library_path"}}The `LD_PRELOAD` environment variable was configured to load libraries from an unusual location. Program functions may have been overridden to hide processes or files and evade detection.{{/is_exact_match}}

## Goal{% #goal %}

Detect attempts to evade detection by loading a malicious library. These libraries often hide processes or files from commands such as `ps` or `ls`.

## Strategy{% #strategy %}

After an attacker's initial intrusion into a victim container or host (for example, through a web shell exploit), they may attempt to escalate privileges, evade defenses, or establish persistence by hijacking environment variables such as `LD_PRELOAD`, or configuration files such as `/etc/ld.so.preload/`, which the dynamic linker uses to load shared libraries.

## Triage and response{% #triage-and-response %}

1. Determine whether or not this is expected behavior.{{#is_match "case_name" "dynamic_linker_config"}} Retrieve the file content and review it for unexpected entries.{{/is_match}}{{#is_exact_match "case_name" "ld_preload_unusual_library_path"}} Review the value of the `LD_PRELOAD` environment variable for unexpected file paths.{{/is_exact_match}}
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack) and look for indications of initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and utilities involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

## Changelog{% #changelog %}

- 26 September 2024 - Updated rule name, severity, and description

*Requires Agent version 7.39 or later*
