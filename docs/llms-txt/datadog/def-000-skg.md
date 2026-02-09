# Source: https://docs.datadoghq.com/security/default_rules/def-000-skg.md

---
title: Keeper records export detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Keeper records export detected
---

# Keeper records export detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detect possible exfiltration attempts from Keeper.

## Strategy{% #strategy %}

This rule monitors Keeper logs to determine when the export record occurs. This could indicate exfiltration attempts from Keeper by downloading or exporting items.

## Triage & response{% #triage--response %}

- Investigate the user with email : `{{@usr.email}}` in enterprise id : `{{@enterprise_id}}` attempting to export.
- If this action was unintended by the user:
  - Rotate the user's Keeper password
  - Identify all the items within the vault that were exported and rotate the necessary authentication credentials
