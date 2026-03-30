# Source: https://docs.datadoghq.com/security/default_rules/def-009-aa7.md

---
title: Azure Bastion shareable link created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Bastion shareable link created
---

# Azure Bastion shareable link created

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an Azure Bastion public link is created. Azure Bastion public links can allow remote access to Azure VMs from untrusted networks. Public links generated for an Azure Bastion can allow VM network access to anyone with the generated URL.

## Strategy{% #strategy %}

Monitor Azure Monitor activity logs for `MICROSOFT.NETWORK/BASTIONHOSTS/GETSHAREABLELINKS/ACTION` or `MICROSOFT.NETWORK/BASTIONHOSTS/CREATESHAREABLELINKS/ACTION` where `@evt.outcome` is `Success`.

## Triage and response{% #triage-and-response %}

1. Verify the legitimacy of the public link creation:

   - Review the Azure activity logs to confirm if the user or process responsible for generating the Bastion public link had a valid business reason.
   - Cross-check with stakeholders or the requesting team to validate whether the action aligns with any approved workflows or maintenance activities.

1. Investigate suspicious or unexpected link creation:

   - Review related logs to identify the IP address and user identity responsible for generating the public link. Look for unusual IPs (for example, foreign or untrusted locations) or unexpected user accounts.
   - Examine the timeline of activities around the event. This includes checking for failed login attempts, access requests from unknown sources, or other suspicious behavior before and after the link creation.

1. Mitigate unauthorized public link creation:

   - If unauthorized, immediately revoke the public link and disable any further access through it.
   - Consider disabling shareable links for Azure Bastion to prevent future unauthorized public link creations.
