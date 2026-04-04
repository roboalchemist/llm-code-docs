# Source: https://docs.datadoghq.com/security/default_rules/def-000-1sc.md

---
title: AWS ListResources executed by new principal identity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS ListResources executed by new
  principal identity
---

# AWS ListResources executed by new principal identity

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1580-cloud-infrastructure-discovery](https://attack.mitre.org/techniques/T1580)
## Goal{% #goal %}

Detects first-time execution of `ListResources` operations by previously unseen AWS principal identities. Identifies potential unauthorized resource discovery activity from new or compromised accounts.

## Strategy{% #strategy %}

This rule analyzes AWS CloudTrail logs for `ListResources` events from the `resource-explorer-2.amazonaws.com` service, using a new value detection on `@userIdentity.principalId`. It establishes a baseline of principals who have previously executed `ListResources` operations and triggers an alert when a principal identity is observed performing this action for the first time. Since the `ListResources` API in AWS Resource Explorer enables broad visibility into resources across accounts and regions, its use by a new principal could signal account compromise, privilege escalation, or unauthorized access, in addition to legitimate administrative activity.

## Triage & Response{% #triage--response %}

- Examine the principal identity `{{@userIdentity.principalId}}` to determine if it represents a legitimate user, role, or service account.
- Review the account creation date and recent access patterns to identify if this is a newly provisioned legitimate account.
- Investigate the authentication method and source location of the `ListResources` calls to detect potential unauthorized access.
- Check for additional AWS API calls from the same principal to understand the full scope of their activity.
- Validate if the principal has appropriate IAM permissions for Resource Explorer operations and if these permissions were recently granted.
- Determine if the timing of the first `ListResources` execution correlates with known onboarding activities or role assignments.
