# Source: https://docs.datadoghq.com/security/default_rules/def-000-oui.md

---
title: 1Password vault export attempt by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > 1Password vault export attempt by user
---

# 1Password vault export attempt by user
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1567-exfiltration-over-web-service](https://attack.mitre.org/techniques/T1567) 
## Goal{% #goal %}

Detect possible exfiltration attempts from 1Password through a vault export.

## Strategy{% #strategy %}

This rule monitors 1Password audit logs to determine when the [export](https://developer.1password.com/docs/events-api/item-usage-actions/#export) item usage action occurs on a vault. This could indicate exfiltration attempts from 1Password by downloading or exporting items within a vault.

## Triage & response{% #triage--response %}

1. Investigate the `{{@usr.email}}` attempting to download or export vault `{{@vault_uuid}}`.
1. If this action was unintended by the user:
   - Rotate the user's 1Password master password
   - Identify all the items within the vault that were exported and rotate the necessary authentication credentials
