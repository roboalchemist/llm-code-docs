# Source: https://docs.datadoghq.com/security/default_rules/def-000-yyo.md

---
title: Windows shimcache flush
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows shimcache flush
---

# Windows shimcache flush

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1112-modify-registry](https://attack.mitre.org/techniques/T1112) 
## Goal{% #goal %}

Detects attempts to flush the Windows shimcache.

## Strategy{% #strategy %}

This rule monitors for command lines involving two specific shimcache flushing techniques. Windows shimcache (also known as AppCompatCache) is a registry artifact that tracks application execution for compatibility purposes and is valuable for digital forensics.

The query searches `@Event.EventData.Data.CommandLine` for instances of `rundll32` used with either `apphelp.dll` (calling `ShimFlushCache` or `#250`) or `kernel32.dll` (calling `BaseFlushAppcompatCache` or `#46`).

These specific command patterns represent deliberate attempts to flush the shimcache registry keys. The shimcache contains evidence of program execution, including timestamps and file paths of programs that have been run on the system. Clearing this cache is not part of normal system administration and is almost exclusively performed as an anti-forensic measure.

Attackers use these techniques to hide evidence of malicious executables they've run on the system, complicating forensic analysis during incident response.

## Triage & Response{% #triage--response %}

- Identify the user account that executed the shimcache flush command on `{{host}}`.
- Review process creation events before and after the shimcache flush for suspicious activity.
- Check for additional anti-forensic techniques being used around the same timeframe.
- Examine recently executed programs using alternative artifacts such as prefetch files or USN journal.
- Look for unauthorized access to the account that performed the shimcache flush.
- Analyze the parent process that spawned the `rundll32` command for context.
- Search for unusual network connections or data transfers before the anti-forensic activity.
- Determine if any malware cleaning tools might have legitimately triggered the shimcache flush.
- Reset credentials for any accounts involved in the suspicious activity.
