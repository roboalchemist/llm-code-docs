# Source: https://docs.datadoghq.com/security/default_rules/def-000-nlb.md

---
title: AWS CreateIndex followed by ListResources via long term access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS CreateIndex followed by
  ListResources via long term access key
---

# AWS CreateIndex followed by ListResources via long term access key

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580) 
## Goal{% #goal %}

Detects coordinated AWS Resource Explorer reconnaissance activity where `CreateIndex` operations are followed by `ListResources` operations using long-term access keys. Identifies systematic resource discovery patterns indicative of attack preparation or unauthorized environment mapping.

## Strategy{% #strategy %}

This rule correlates two signals based on `@userIdentity.accessKeyId` and `@awsRegion` within a 24-hour window. It monitors for the sequence where a principal first creates a resource index using long-term access keys and subsequently performs resource listing operations using the same long-term credentials. This behavior pattern represents a systematic approach to AWS environment reconnaissance, where an attacker first establishes the capability to search resources by creating an index, then immediately leverages that index to enumerate available resources. The combination of both activities using long-term access keys suggests deliberate and potentially unauthorized infrastructure discovery efforts that exceed typical administrative workflows.

## Triage & Response{% #triage--response %}

- Examine the access key `{{@userIdentity.accessKeyId}}` and principal identity involved in both the `CreateIndex` and `ListResources` operations in region `{{@awsRegion}}`.
- Review the time sequence between index creation and resource listing to determine if the pattern indicates automated or manual reconnaissance.
- Investigate the scope and specificity of the `ListResources` queries to understand what resources the actor was targeting.
- Check for additional Resource Explorer API calls or other discovery-related AWS API activity from the same principal.
- Validate if the principal has legitimate business justification for both creating indexes and performing comprehensive resource enumeration.
- Analyze the source IP addresses and geographic locations for both activities to identify potential unauthorized access patterns.
- Determine if the access key has been recently compromised or shows other indicators of misuse beyond this specific activity sequence.
