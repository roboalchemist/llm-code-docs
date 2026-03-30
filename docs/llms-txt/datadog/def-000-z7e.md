# Source: https://docs.datadoghq.com/security/default_rules/def-000-z7e.md

---
title: Possible AWS backup resource enumeration by long term access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Possible AWS backup resource
  enumeration by long term access key
---

# Possible AWS backup resource enumeration by long term access key
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580)
## Goal{% #goal %}

Detects AWS backup service enumeration activities performed across multiple regions using long-term access keys.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail events for backup service enumeration API calls including `ListProtectedResources`, `ListBackupSelections`, `ListBackupPlans`, and `ListBackupVaults` when performed by long-term access keys across multiple regions.

AWS Backup enumeration is a discovery technique that enables attackers to map an organization's infrastructure, identify backed-up resources, understand backup retention policies, and discover the breadth of services in use. This approach is particularly valuable for attackers as it provides comprehensive visibility into production resources without requiring enumeration of individual AWS services, which may be more heavily monitored.

## Triage & Response{% #triage--response %}

- Verify if `{{@userIdentity.arn}}` has legitimate business reasons to enumerate AWS backup resources across multiple regions and determine if this represents authorized administrative activity.
- Examine the timeline of backup enumeration calls to identify if the activity follows suspicious patterns such as rapid successive calls or unusual timing outside business hours.
- Review other API calls made by the same access key to identify additional reconnaissance activities or attempts to access discovered resources.
- Check if the enumerated backup resources have been accessed, modified, or if any backup policies have been changed following the enumeration activity.
- Analyze the source IP addresses and user agent strings associated with these API calls to determine if they originate from expected administrative locations or tools.
